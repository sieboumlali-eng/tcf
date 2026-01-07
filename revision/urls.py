from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('api/exam/<int:exam_id>/question/<int:question_num>/', views.question_api, name='question_api'),
]
