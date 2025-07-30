from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from base.permissions import IsAdmin
from rest_framework.authtoken.models import Token
from orders.models import Order
from orders.serializers import OrderSerializer
from django.contrib.auth import authenticate, logout
from drf_spectacular.utils import extend_schema 
# from drf_spectacular.types import OpenApiTypes
# Create your views here.

class RegisterView(APIView):
    model = Account
    serializer_class = AccountSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args,**kwargs):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = self.model.objects.create_user(**serializer.validated_data)
            return Response({"message":self.serializer_class(user).data})
        return Response(serializer.errors)

class AdminView(APIView):
    permission_classes =[IsAuthenticated, IsAdmin]

    def get(self, request):
        data =[]
        users = Account.objects.all()

        for user in users:
            orders = Order.objects.filter(user =user)
            data.append({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role
                },
                "orders": OrderSerializer(orders, many=True).data
            })
        return Response(data)

class CreateStaffView(APIView):
    model = Account
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, IsAdmin] 

    @extend_schema(
            request=AccountSerializer,
            responses=AccountSerializer
    )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = self.model.objects.create_user(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                role='staff' 
            )
            return Response({"message": f"Staff user {user.username} created successfully"})
        return Response(serializer.errors, status=400)

class DeleteStaffView(APIView):
    serializer_class = AccountSerializer
    permission_classes =[IsAuthenticated,IsAdmin]

    def delete(self, request , **kwargs):
        username = kwargs.get('username')
        if username:
            user = Account.objects.filter(username = username).first()
            if not user:
                return Response({"message":"enter correct creds"})
            if user.role =='staff':
                user.delete()
                return Response({"message":"staff user has been deleted"})
            return Response({"message":"Provide correct user"})
        return Response({"messsage":"provide username of the staff user"}) 
    
class LoginView(APIView):
    permission_classes =[AllowAny]

    @extend_schema(
        description="Login with email and password to receive token.",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'example': 'admin@example.com'},
                    'password': {'type': 'string', 'example': 'password123'},
                },
                'required': ['email', 'password']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Login Successful'},
                    'id': {'type': 'integer', 'example': 1},
                    'email': {'type': 'string', 'example': 'admin@example.com'},
                    'username': {'type': 'string', 'example': 'adminuser'},
                    'token': {'type': 'string', 'example': 'f3b8c3e5b...'},
                    'role': {'type': 'string', 'example': 'admin'}
                }
            }
            
        })

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response("Email and password is requieed")
        user = authenticate(request , email = email , password = password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        token = Token.objects.get(user =user)
        return Response(
            
            {
                "message":"Login Successfull",
                "id" : user.id,
                "email" : email,
                "username": user.username,
                "token" : token.key,
                "role":user.role
            }
        )
    
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message":"successfully Logged out"})


