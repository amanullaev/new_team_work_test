from django.shortcuts import render
from rest_framework import generics
from .models import New
from .serializers import NewSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from config.permissions import AdminPermission, UserPermission


class CreateNewView(generics.CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializers
    permission_classes = (AdminPermission,)


class GetAllNewsView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializers
    permission_classes = (UserPermission,)


class DetailNewView(APIView):
    def get(self, request, *args, **kwargs):
        news = get_object_or_404(New, title=kwargs['title'])
        serializers = NewSerializers(news)
        permission_classes = (UserPermission,)
        return Response(serializers.data)


class UpdateNewView(APIView):
    def patch(self, request, *args, **kwargs):
        news = get_object_or_404(New, id=kwargs['id'])
        serializer = NewSerializers(news, data=request.data, partial=True)
        if serializer.is_valid():
            permission_classes = (AdminPermission,)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteNewView(APIView):
    def delete(self, request, *args, **kwargs):
        news = get_object_or_404(New, id=kwargs['id'])
        news.delete()
        permission_classes = (AdminPermission,)
        return Response({'msg':'deleted'})