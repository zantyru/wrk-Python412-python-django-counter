from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views


app_name = "api"

urlpatterns = [
    path("api/token-auth/", obtain_auth_token, name="token_auth"),
    path("api/hello/", views.HelloAPIView.as_view(), name="hello"),
    path("api/counters/", views.CounterListView.as_view(), name="counter_list"),
    path("api/counters/<pk>/", views.CounterDetailView.as_view(), name="counter_detail"),
    path("api/counters/<pk>/increase/", views.CounterIncreaseView.as_view(), name="counter_increase"),
]
