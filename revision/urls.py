from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('api/exam/<int:exam_id>/question/<int:question_num>/', views.question_api, name='question_api'),
    path('api/exam/<int:exam_id>/questions/all/', views.all_questions_api, name='all_questions_api'),
    
    # Exam Ecrit URLs
    path('exam/ecrit/<int:exam_id>/', views.exam_ecrit_detail, name='exam_ecrit_detail'),
    path('api/exam/ecrit/<int:exam_id>/question/<int:question_num>/', views.question_ecrit_api, name='question_ecrit_api'),
    path('api/exam/ecrit/<int:exam_id>/questions/all/', views.all_questions_ecrit_api, name='all_questions_ecrit_api'),
]
