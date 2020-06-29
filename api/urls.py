from django.urls import path
from api import views

urlpatterns = [
    path("emp/<str:id>/", views.EmployeeAPIView.as_view()),
    path("emp/", views.EmployeeAPIView.as_view()),
]
