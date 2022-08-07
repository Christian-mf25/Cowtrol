from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from farms.serializers import FarmSerializer, LoginSerializer
from rest_framework.views import Request, Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import status
from dotenv import load_dotenv

from farms.models import Farm

load_dotenv()


class FarmView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


@api_view(["POST"])
def login(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    farm = authenticate(
        username=serializer.validated_data["email"],
        password=serializer.validated_data["password"],
    )

    if not farm:
        return Response(
            {"message": "Invalid password or e-mail address"},
            status.HTTP_401_UNAUTHORIZED,
        )

    token, _ = Token.objects.get_or_create(user=farm)

    return Response(
        {"token": token.key},
        status.HTTP_200_OK
    )