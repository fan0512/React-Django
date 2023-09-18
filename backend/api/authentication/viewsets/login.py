from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from api.authentication.serializers import LoginSerializer


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    # http_method_names = ["post"]
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
        
