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
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
import base64
from . import views
from django.contrib.auth import get_user_model
from datetime import timedelta
from authentication.serializer import *
Profile = get_user_model()


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
   

    def get(self, request):
        menu_items = [
            {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "image": item.image
                
            }
            for item in MenuItem.objects.all()
        ]
        return Response(menu_items)

class MenuItemDetailView(APIView):
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, id, *args, **kwargs):
        data = request.data
        user = request.user
       
        menu_item = MenuItem.objects.get(id=id)
        
        
        if not menu_item:
            return Response(
                {"res": "Object with menuItem id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer_class = MenuItemSerializer(menu_item)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
      
    def delete(self, request, id, *args, **kwargs):
        permission_classes = [IsAdminUser]
      
        data = request.data
        user = request.user
        menu_item = MenuItem.objects.get(id=id)
        menu_item.delete()
        if not menu_item:
            return Response(
                {"res": "Object with menuItem id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer_class = MenuItemSerializer(menu_item)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class OrderView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    
    

    def get(request, id):
        Profile = get_user_model()
        # user = request.user
        # id = request.user.id
        # print(id)
        data = Profile.objects.all(id=request.user.id)
        print(data)
        
        # print(data.email)
        # if no cart for the user, just create one
        # order, created = Order.objects.get_or_create(Profile=Profile)
        # # get all cart items for this cart
        # myorderItems = OrderItem.objects.filter(order=order)
        # result = [{'order_item': MenuItemSerializer(item.menu_items).data,
        #            'qty': item.qty
        #            } 
        #           for item in myorderItems
        #         ]
        # return Response(result)
        # print(result)
       
     
       
        
        serializer = MenuItemSerializer
        result = [{
            'item': item.name,
            'quantity': item.quantity,
            'price': item.price,
            'image': item.image,
            'qty': item.qty
            }
                  for item in order
                  ]
        # cart = [{'user': cart.user, 'product': cart.product,'quantity': cart.quantity, 'id': cart.id, } for cart in Cart.objects.all()]
        return Response(result)
