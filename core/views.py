import profile
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from authentication.serializer import *
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
import base64
from . import views
from django.contrib.auth import get_user_model
from datetime import timedelta


# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


@api_view(["GET", "POST"])
def EndPoint(request):
    if request.method == "GET":
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({"response": data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = request.POST.get("text")
        data = (
            f"Congratulation your API just responded to POST request with text: {text}"
        )
        return Response({"response": data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


class LoginView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

    @api_view(["GET", "POST"])
    def LoginAPI(request):
        if request.method == "GET":
            data = (
                f"Congratulation {request.user}, your API just responded to GET request"
            )
            return Response({"response": data}, status=status.HTTP_200_OK)
        elif request.method == "POST":
            text = request.POST.get("text")
            data = f"Congratulation your API just responded to POST request with text: {text}"
            return Response({"response": data}, status=status.HTTP_200_OK)
        #     serializer = ProfileSerializer(**validated_data)
        # if serializer.is_valid():
        #     Profile = serializer.save()
        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)

class MenuItemView(APIView):

    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]
    # image_data = tf.gfile.FastGFile(filename, 'rb').read()

    def get(self, request):
        menu_items = [
            {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "image2": item.image2,
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
