
from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from models import location
from .serializer import review_serializer, location_serializer
from rest_framework.response import Response
from .models import places
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.db.models import Q
from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView

# Create your views here.
class user_review(APIView):
    permissions = [permissions.IsAuthenticated]
    def post(self,request):
        data=request.data
        # if("picture" in data):
        #     serializer_data={
        #         "address": data["address"],
        #         "name":data["name"],
        #         "user":request.user,
        #         "picture":data["picture"]
        #     }
        # else:
        #     serializer_data={
        #         "address": data["address"],
        #         "name":data["name"],
        #         "user":request.user
        #     }
        serializer = review_serializer(data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)

class add_location_api(APIView):
    def post(self,request):
        data=request.data
        serializer = location_serializer(data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
