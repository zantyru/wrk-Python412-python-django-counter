from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app_counter.models import Counter
from app_counter.serializers import CounterSerializer


class HelloAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        content = {
            "message": "Hello, world!"
        }

        return Response(content)


class CounterListView(generics.ListAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterDetailView(generics.RetrieveAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterIncreaseView(APIView):

    def get(self, request, pk, format=None):  # А вообще нужен post

        counter = get_object_or_404(Counter, pk=pk)
        counter.value += 1
        counter.save()

        return Response(
            {
                "action": "increase",
                "isComplete": True,
            }
        )
