from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('detail/<int:question_id>', views.detail_view, name="detail"),
    path('list/', views.view_list, name="view_list"),
    path('', views.index, name="index"),
]