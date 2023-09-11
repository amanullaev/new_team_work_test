from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from config.permissions import AdminPermission, UserPermission


class CreateCoachView(generics.CreateAPIView):
    queryset = TrenerModel.objects.all()
    serializer_class = TrenerSerializer
    permission_classes = (AdminPermission,)


class GetAllCoachesView(generics.ListAPIView):
    queryset = TrenerModel.objects.all()
    serializer_class = TrenerSerializer
    permission_classes = (UserPermission,)


class DetailCoachView(APIView):
    def get(self, request, *args, **kwargs):
        coach = get_object_or_404(TrenerModel, first_name=kwargs['first_name'])
        serializers = TrenerSerializer(coach)
        permission_classes = (UserPermission,)
        return Response(serializers.data)


class UpdateCoachView(APIView):
    def patch(self, request, *args, **kwargs):
        coach = get_object_or_404(TrenerModel, id=kwargs['id'])
        serializer = TrenerSerializer(coach, data=request.data, partial=True)
        if serializer.is_valid():
            permission_classes = (AdminPermission,)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteCoachView(APIView):
    def delete(self, request, *args, **kwargs):
        coach = get_object_or_404(TrenerModel, id=kwargs['id'])
        coach.delete()
        permission_classes = (AdminPermission,)
        return Response({'msg':'deleted'})