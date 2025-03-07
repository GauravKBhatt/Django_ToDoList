from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import Item
from .serializers import ItemSerializer

class GetRoutes(APIView):
    def get(self, request, *args, **kwargs):
        routes=[
            'GET /api',
            'GET /api/items',
            'GET /api/items/:id'
        ]
        return Response(routes)

class GetItems(APIView):
    def get(self, request, *args, **kwargs):
        items=Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)