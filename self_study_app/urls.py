from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('module/<int:pk>/', views.ModuleDetailView.as_view(), name="module"),
    path('course/<int:course_pk>/', views.TestListView.as_view(), name="course_test"),

]
