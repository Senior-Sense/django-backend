from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes
from api.serializers import RegistrationSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication



class RegisterUserView(generics.CreateAPIView) :
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self , request ) :
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"Success" : "Now you can login"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def user_info(request) :
    user = request.user
    return Response({
        'username' : user.username,
        'email' : user.email,
        'first_name' : user.first_name,
        'last_name' : user.last_name
    })
