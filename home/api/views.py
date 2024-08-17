from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import render
from home.models import Home
from home.api.serializers import HomePageSerializer


class HomePageViewSet(viewsets.GenericViewSet):
    serializer_class = HomePageSerializer

    def list(self, request, *args, **kwargs):
        home = Home.objects.first()
        context = {"home": home}
        return render(request, "home/index.html", context)

    def retrieve(self, request, *args, **kwargs):
        home = Home.objects.first()
        data = {
            "image": home.image.url,
            "message": "Welcome to the Home Page!",
        }
        serializer = self.get_serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
