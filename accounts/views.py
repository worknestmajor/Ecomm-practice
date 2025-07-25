from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterView(APIView):
    model = Account
    serializer_class = AccountSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args,**kwargs):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = self.model.objects.create_user(**serializer.validated_data)
            # token, _ = Token.objects.get_or_create(user=user)
            return Response({"message":self.serializer_class(user).data})
        return Response(serializer.errors)
    
class InfoView(APIView):
    def get(self,request):
        return Response({"message":request.user.username})

