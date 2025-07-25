from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from base.permissions import IsSuperUser
# Create your views here.


class BaseView(APIView):
    model = None
    serializer_class = None

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUser()]
        return [AllowAny()]

    def get(self, request, *args, **kwargs):
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
            
    def post(self, request, *args,**kwargs):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            obj = self.model.objects.create_obj(**serializer.validated_data)
            return Response({"message":self.serializer_class(obj).data})
        return Response(serializer.errors)
    
    def delete(self,request, *args, **kwargs):
        obj_id = kwargs.get("id")
        if obj_id:
            self.model.objects.delete_obj(obj_id)
            return Response({"message":"Successfully deleted"})