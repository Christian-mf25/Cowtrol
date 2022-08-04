from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from django.shortcuts import render

from areas.models import Area

class AreaView(generics.ListCreateAPIView):
	authentication_classes = [TokenAuthentication]

	queryset = Area.objects.all()
	serializer_class = 
