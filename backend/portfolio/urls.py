from django.urls import path
from .views import ProgettoList, ProgettoDetail

urlpatterns = [
    path('progetti/', ProgettoList.as_view(), name='progetto-list'),
    path('progetti/<int:pk>/', ProgettoDetail.as_view(), name='progetto-detail'),
]