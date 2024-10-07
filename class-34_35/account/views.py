from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, UserLoginSerializer, UserUpdateSerializer
from .models import CustomUser
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSerializer


class ResendVerificationEmail(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if email:
            user = CustomUser.objects.filter(email=email).first()

            if not user:
                return Response({
                    "details" : "User with this email doesn't exist!",
                }, status=status.HTTP_404_NOT_FOUND)
            
            if user.is_verified:
                return Response({
                    "details" : "Email already verified!",
                }, status=status.HTTP_400_BAD_REQUEST)
            

            user.verification_token = get_random_string(length=32)
            user.save()

            # Prepare things for sending mail
            verification_link = request.build_absolute_uri(
                reverse(
                    viewname='verify_email',
                    kwargs = {'token' : user.verification_token}
                ),
            )


            # Render the email template
            subject = 'Verify you email'
            html_content = render_to_string('emails/verification_email.html', {
                "user": user.username,
                "verification_link" : verification_link
            })

            # create an email message

            email = EmailMultiAlternatives(
                subject,
                "This is a plain text version of the email",
                "from@example.com",
                [user.email]
            )

            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)

            return Response({
                    "details" : "Verfication email sent!",
                }, status=status.HTTP_200_OK)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request , token):
        user = CustomUser.objects.filter(verification_token=token).first()

        if user:
            if user.is_verified:
                return Response({
                    "details" : "Email already verified!",
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user.is_verified = True
            user.verification_token = None
            user.save()

            return Response({
                "details" : "Successfully verified!",
            }, status=status.HTTP_200_OK)
        
        return Response({
            "details" : "Invalid token",
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user:
            matched_password = user.check_password(password)

            if matched_password:
                if not user.is_verified:
                    return Response({
                        "details" : "Email is not verified yet!",
                    }, status=status.HTTP_401_UNAUTHORIZED)
                
                refresh = RefreshToken.for_user(user)

                return Response({
                    "refresh_token" : str(refresh),
                    "access_token" : str(refresh.access_token)
                })
        
        return Response({
            "details" : "Invalid credentials",
        }, status=status.HTTP_401_UNAUTHORIZED)
    


class RetrieveUpdateProfile(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def get_serializer_class(self):
        if self.request.method in ['PUT' , 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer