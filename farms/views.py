from rest_framework.views import Request, Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from farms.models import Farm