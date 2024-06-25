from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all),
    path('view/<int:todo_id>/', views.view_individual),
]
