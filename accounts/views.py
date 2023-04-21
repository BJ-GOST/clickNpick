from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from knox.auth import TokenAuthentication

from .serializers import ReaderSerializer

@api_view(['POST'])
@csrf_exempt
def register(request):
    serializer = ReaderSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reader_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        _, token = AuthToken.objects.create(user)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return Response({'token': token}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def reader_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'success': 'User successfully logged out.'})
