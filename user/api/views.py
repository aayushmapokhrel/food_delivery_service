from rest_framework import viewsets, status
from django.contrib.auth import login
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from user.api.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserBalanceSerializer,
)
from user.models import User, UserBalance
from django.http import JsonResponse
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin


class RegisterViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "errors": serializer.errors})

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if "password" in request.data:
                user.set_password(request.data["password"])
                user.save()
            return JsonResponse({"success": True, "user": serializer.data})
        return JsonResponse(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return JsonResponse({"success": True}, status=status.HTTP_204_NO_CONTENT)


class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "errors": serializer.errors})

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            if "password" in request.data:
                user.set_password(request.data["password"])
                user.save()
            return JsonResponse({"success": True, "user": serializer.data})
        return JsonResponse(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)

        user.delete()
        return JsonResponse({"success": True}, status=status.HTTP_204_NO_CONTENT)


class UserBalanceViewSet(viewsets.GenericViewSet, CreateModelMixin, UpdateModelMixin):
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_balance, created = UserBalance.objects.update_or_create(
                user=serializer.validated_data["user"],
                defaults={"balance": serializer.validated_data["balance"]},
            )
            return Response(
                {
                    "success": True,
                    "user_balance": UserBalanceSerializer(user_balance).data,
                },
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, *args, **kwargs):
        user_balance = self.get_object()
        serializer = self.get_serializer(user_balance, data=request.data, partial=True)
        if serializer.is_valid():
            user_balance = serializer.save()
            return Response(
                {
                    "success": True,
                    "user_balance": UserBalanceSerializer(user_balance).data,
                }
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
