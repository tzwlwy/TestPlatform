from django.urls import path
from .views import ConnectionManager

urlpatterns = [
    path('connections/', ConnectionManager.as_view()),
    path('connections/<str:user_id>/', ConnectionManager.as_view()),
]
