from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from roadmap.serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('LoginView_post')
        print(serializer.validated_data)
        access_token = serializer.validated_data.get('access')
        refresh_token = serializer.validated_data.get('refresh')
        user = serializer.validated_data.get('user')
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # Add more fields if necessary
        }

        response = Response({'message': 'Login successful', 'user': user_data}, status=status.HTTP_200_OK)
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,  # A süti csak HTTP kéréseken keresztül elérhető (védett XSS ellen)
            secure=True,  # Csak HTTPS kapcsolaton keresztül működik
            samesite='Lax',  # Cross-site támadások ellen védekezik
            max_age=36000000,
        )
        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,  # A süti csak HTTP kéréseken keresztül elérhető (védett XSS ellen)
            secure=True,  # Csak HTTPS kapcsolaton keresztül működik
            samesite='Lax',  # Cross-site támadások ellen védekezik
            max_age=36000000,
        )
        return response


        # return Response(serializer.validated_data, status=status.HTTP_200_OK)
