from django.urls import path
from api import views

urlpatterns = [
    path("emp/<str:id>/", views.EmployeeAPIView.as_view()),
    path("emp/", views.EmployeeAPIView.as_view()),
    path("stu/<str:id>/",views.StudentAPIView.as_view()),
    path("stu/",views.StudentAPIView.as_view()),
]
