from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views


app_name = "api"

urlpatterns = [
    path("api/token-auth/", obtain_auth_token, name="token_auth"),
    path("api/hello/", views.HelloAPIView.as_view(), name="hello"),
    path("api/counters/", views.CounterListView.as_view(), name="counter_list"),
    path("api/counters/login/<login>/", views.CounterListView.as_view(), name="counter_list_by_login"),
    path("api/counters/id/<pk>/", views.CounterDetailView.as_view(), name="counter_detail"),
    path("api/counters/id/<pk>/increase/", views.CounterIncreaseView.as_view(), name="counter_increase"),
    path("api/counters/id/<pk>/decrease/", views.CounterDecreaseView.as_view(), name="counter_decrease"),
]
