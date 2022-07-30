# import profile
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from .models import *
# from rest_framework import status
# from rest_framework import generics
# from rest_framework import renderers
# from core.serializer import (
#     MyTokenObtainPairSerializer,
#     RegisterSerializer,
#     UserSerializer,
# )
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes, action
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .serializer import *
# import base64
# from . import views
# from django.contrib.auth.models import Profile
# from datetime import timedelta

# # Create your views here.


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data["refresh"] = str(refresh)
#         data.pop("refresh", None)  # remove refresh from the payload
#         data["access"] = str(refresh.access_token)

#         # Add extra responses here
#         data["username"] = self.user.username
#         data["email"] = self.user.email
#         data["first_name"] = self.user.first_name
#         data["last_name"] = self.user.last_name
#         # data["created_date"] = datetime.date.today()
#         return data


# class BlacklistRefreshView(APIView):
#     def post(self, request):
#         token = RefreshToken(request.data.get("refresh"))
#         token.blacklist()
#         return Response("Success")


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer


# def getRoutes(request):
#     routes = [
#         "/api/token/",
#         "/api/register/",
#         "/api/token/refresh/",
#         "/api/prediction/",
#     ]
#     return Response(routes)

#     @api_view(["GET", "POST"])
#     def EndPoint(request):
#         if request.method == "GET":
#             data = (
#                 f"Congratulation {request.user}, your API just responded to GET request"
#             )
#             return Response({"response": data}, status=status.HTTP_200_OK)
#         elif request.method == "POST":
#             text = request.POST.get("text")
#             data = f"Congratulation your API just responded to POST request with text: {text}"
#             return Response({"response": data}, status=status.HTTP_200_OK)
#             print(data)
#         return Response({}, status.HTTP_400_BAD_REQUEST)


# def RegisterPage(request):
#     return render(request, "RegisterPage")


# class LoginView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = MyTokenObtainPairSerializer

#     @api_view(["GET", "POST"])
#     def LoginAPI(request):
#         if request.method == "GET":
#             data = (
#                 f"Congratulation {request.user}, your API just responded to GET request"
#             )
#             return Response({"response": data}, status=status.HTTP_200_OK)
#         elif request.method == "POST":
#             text = request.POST.get("text")
#             data = f"Congratulation your API just responded to POST request with text: {text}"
#             return Response({"response": data}, status=status.HTTP_200_OK)
#             print(data)
#         return Response({}, status.HTTP_400_BAD_REQUEST)


# class ProfileView(APIView):

#     serializer_class = ProfileSerializer

#     def get(self, request):
#         user = [
#             {
#                 "username": profile.user.username,
#                 "created_date": profile.created_date,
#                 "address": profile.address,
#                 "first_name": profile.user.first_name,
#                 "last_name": profile.user.last_name,
#                 "email": profile.user.email,
#             }
#             for profile in Profile.objects.all()
#         ]
#         return Response(user)


# class MenuItemView(APIView):

#     serializer_class = MenuItemSerializer
#     # image_data = tf.gfile.FastGFile(filename, 'rb').read()

#     def get(self, request):
#         menu_items = [
#             {
#                 "name": item.name,
#                 "description": item.description,
#                 "price": item.price,
#                 # "image": item.image,
#                 "qty": item.qty,
#             }
#             for item in MenuItem.objects.all()
#         ]
#         return Response(menu_items)

#     def post(self, request):
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# class OrderView(APIView):

#     serializer_class = OrderSerializer

#     def get(self, request):
#         order = [
#             {
#                 # "profile": profile_id.user.order,
#                 "date": order.date,
#                 "menu_items": order.menu_items,
#                 # "courier": order.courier,
#                 "tax": order.tax,
#                 "tip": order.tip,
#                 "total": order.total,
#             }
#             for order in Order.objects.all()
#         ]
#         return Response(order)


# # def post(self, request, format=None):
# #     data = request.data
# #     username = data["username"]
# #     # email = data['email']
# #     password = data["password"]
# #     try:
# #         if User.objects.filter(username=username).exists():
# #             return Response(
# #                 {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
# #             )
# #         else:
# #             if len(password) < 3:
# #                 return Response(
# #                     {"error": "Password must be at least 3 characters"},
# #                     status=status.HTTP_400_BAD_REQUEST,
# #                 )
# #             else:
# #                 user = User.objects.create_user(
# #                     username=username, password=password, email=email
# #                 )
# #                 user.save()
# #                 profile = Profile(user=user)
# #                 profile.save()
# #                 # login user
# #                 login(request, user)
# #                 return Response({"success": "User created successfully"})
# #     except Exception as e:
# #         print(e)
# #         return Response(
# #             {"error": "Something went wrong during resgistration"},
# #             status=status.HTTP_500_INTERNAL_SERVER_ERROR,
# #         )
