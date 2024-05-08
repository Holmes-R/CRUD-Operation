from django.contrib import admin
from django.urls import path,include
from Myapp import views
urlpatterns = [
    path('',views.home), 
    path('info/',views.apiOverview),
    path('read/', views.read, name="read"),
    path('detail/<str:pk>/', views.details, name="details"),
    path("update/<str:pk>/", views.update, name="update"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("user/", views.User.as_view(), name="user"),
]