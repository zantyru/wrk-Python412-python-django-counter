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


class CounterListView(APIView):  # было в скобках generics.ListAPIView

    def get(self, request, login=None):

        if login:
            counter = get_object_or_404(Counter, user__username=login)
            data = CounterSerializer(counter).data
        else:
            all_counters = Counter.objects.all()
            data = CounterSerializer(all_counters, many=True).data

        return Response(data)


class CounterDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterIncreaseView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):

        counter = get_object_or_404(Counter, pk=pk)
        counter.value += 1
        counter.save()

        return Response(
            {
                "action": "increase",
                "isComplete": True,
                "counter": CounterSerializer(counter).data,
            }
        )


class CounterDecreaseView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):

        counter = get_object_or_404(Counter, pk=pk)
        counter.value -= 1
        counter.save()

        return Response(
            {
                "action": "decrease",
                "isComplete": True,
                "counter": CounterSerializer(counter).data,
            }
        )
