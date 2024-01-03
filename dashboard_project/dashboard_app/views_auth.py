from django.contrib.auth.models import User
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
    # User Registration
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    # User Login and Token Generation
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    
    if user.check_password(password):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)