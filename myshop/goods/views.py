from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Good

from .serializers import CategorySerializer, GoodsSerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects_first_level.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Category.objects.filter(parent=kwargs['pk'])
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodsSerializer
