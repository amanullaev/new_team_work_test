from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from config.permissions import AdminPermission, UserPermission


class CreateGymView(generics.CreateAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers
    permission_classes = (AdminPermission,)


class GetAllGymView(generics.ListAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers
    permission_classes = (UserPermission,)


class DetailGymView(APIView):
    def get(self, request, *args, **kwargs):
        gym = get_object_or_404(GymModel, name=kwargs['name'])
        serializers = GymSerializers(gym)
        permission_classes = (UserPermission,)
        return Response(serializers.data)


class UpdateGymView(APIView):
    def patch(self, request, *args, **kwargs):
        gym = get_object_or_404(GymModel, id=kwargs['id'])
        serializer = GymSerializers(gym, data=request.data, partial=True)
        if serializer.is_valid():
            permission_classes = (AdminPermission,)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteGymView(APIView):
    def delete(self, request, *args, **kwargs):
        gym = get_object_or_404(GymModel, id=kwargs['id'])
        gym.delete()
        permission_classes = (AdminPermission,)
        return Response({'msg':'deleted'})