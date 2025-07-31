from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from base.permissions import IsAdmin, IsAdminOrStaff,SAFE_METHODS
from drf_spectacular.utils import extend_schema

# Create your views here.

class BaseView(APIView):
    model = None
    serializer_class = None

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]

        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsAdmin()]

        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return [IsAuthenticated(), IsAdminOrStaff()]


    @extend_schema(
            description="**This is used to get item or items**"
    )
    def get(self, request,  **kwargs):
        obj_id = kwargs.get("id")
        if obj_id:
            obj = self.model.objects.get_obj_by_id(obj_id)
            if obj:
                serializer = self.serializer_class(obj)
                return Response({"message":serializer.data})
            return Response({"message": "No obj Found"})
        else:
            queryset = self.model.objects.get_all()
            serializer = self.serializer_class(queryset, many=True)
            return Response({"message":serializer.data})

    @extend_schema(
            description="**This is used to create new item**"
    )        
    def post(self, request,**kwargs):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            obj = self.model.objects.create_obj(**serializer.validated_data)
            return Response({"message":self.serializer_class(obj).data})
        return Response(serializer.errors)
    
    @extend_schema(
            description="**This is used to update an item**"
    )
    def put(self,request ,**kwargs):
        obj_id = kwargs.get('id')
        if not obj_id:
            return Response({"message":"Id needed for update"})
        obj = self.model.objects.get_obj_by_id(obj_id)
        if not obj:
            return Response({"message":"valid Id neded for update"})
        serializer = self.serializer_class(obj ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"item has been updated"})
    
    @extend_schema(
            description="**This is used to partially update an item**"
    )
    def patch(self,request ,**kwargs):
        obj_id = kwargs.get('id')
        if not obj_id:
            return Response({"message":"Id needed for update"})
        obj = self.model.objects.get_obj_by_id(obj_id)
        if not obj:
            return Response({"message":"valid Id neded for update"})
        serializer = self.serializer_class(obj ,data = request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"item has been updated"})
    
    @extend_schema(
            description="**This is used to delete an item**"
    )
    def delete(self,request, **kwargs):
        obj_id = kwargs.get("id")
        if not obj_id:
            return Response({"error": "ID required for deletion"}, status=400)
        if obj_id:
            self.model.objects.delete_obj(obj_id)
            return Response({"message":"Successfully deleted"})