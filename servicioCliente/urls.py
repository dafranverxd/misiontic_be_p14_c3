from django.urls import path
from .views import SoporteListCreate, SoporteUpdateDelete, PQRListCreate, PQRpdateDelete

urlpatterns = [
    path('soporte/' , SoporteListCreate.as_view()),
    path('soporte/<pk>/', SoporteUpdateDelete.as_view()),
    path('pqr', PQRListCreate.as_view()),
    path('pqr/<pk>/', PQRpdateDelete.as_view()),
]