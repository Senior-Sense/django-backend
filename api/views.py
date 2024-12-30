from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from api.serializers import RegistrationSerializer , PasswordChangeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import status


class RegisterUserView(generics.CreateAPIView) :
    permission_classes = [AllowAny]
    authentication_classes = []
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

class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password has been successfully updated."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
