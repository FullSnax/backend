import profile
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from core.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import *
import base64
from . import views
from django.contrib.auth.models import User
from datetime import timedelta

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class BlacklistRefreshView(APIView):
    
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def EndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

def RegisterPage(request):
    return render(request, 'RegisterPage')

class ProfileView(APIView):

    serializer_class = ProfileSerializer

    def get(self, request):
        user = [
            {
                "username": profile.user.username,
                "created_date": profile.created_date,
                "address": profile.address,
                "first_name": profile.user.first_name,
                "last_name": profile.user.last_name,
                "email": profile.user.email,
            }
            for profile in Profile.objects.all()
        ]
        return Response(user)
    
class MenuItemView(APIView):

    serializer_class = MenuItemSerializer
    # image_data = tf.gfile.FastGFile(filename, 'rb').read()

    def get(self, request):
        menu_items = [
            {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                # "image": item.image,
                "qty": item.qty,
            }
            for item in MenuItem.objects.all()
        ]
        return Response(menu_items)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class OrderView(APIView):

    serializer_class = OrderSerializer

    def get(self, request):
        order = [
            {
                # "profile": profile_id.user.order,
                "date": order.date,
                "menu_items": order.menu_items,
                # "courier": order.courier,
                "tax": order.tax,
                "tip": order.tip,
                "total": order.total,
            }
            for order in Order.objects.all()
        ]
        return Response(order)

