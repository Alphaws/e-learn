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
        print('--------------------------------')
        access_token = serializer.validated_data.get('token')
        refresh_token = serializer.validated_data.get('refresh_token')
        user = serializer.validated_data.get('user')
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'token': access_token,
            'refresh_token': refresh_token,
            'language': user.profile.language,
            'phone_number': user.profile.phone_number,
            # Add more fields if necessary
        }

        response = Response({
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user_data
        }, status=status.HTTP_200_OK)
        # response.set_cookie(
        #     key='access_token',
        #     value=access_token,
        #     httponly=True,  # A süti csak HTTP kéréseken keresztül elérhető (védett XSS ellen)
        #     secure=True,  # Csak HTTPS kapcsolaton keresztül működik
        #     samesite='Lax',  # Cross-site támadások ellen védekezik
        #     max_age=36000000,
        # )
        # response.set_cookie(
        #     key='refresh_token',
        #     value=refresh_token,
        #     httponly=True,  # A süti csak HTTP kéréseken keresztül elérhető (védett XSS ellen)
        #     secure=True,  # Csak HTTPS kapcsolaton keresztül működik
        #     samesite='Lax',  # Cross-site támadások ellen védekezik
        #     max_age=36000000,
        # )
        return response


        # return Response(serializer.validated_data, status=status.HTTP_200_OK)
