from django.shortcuts import render

from .models import ExamOrale

from django.shortcuts import render, get_object_or_404
from .models import ExamOrale

def exam_list(request):
    exams = ExamOrale.objects.all()
    return render(request, 'revision/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(ExamOrale, pk=exam_id)
    questions = exam.questions.all().order_by('num_qst')
    
    context = {
        'exam': exam,
        'questions': questions
    }
    return render(request, 'revision/index.html', context)
