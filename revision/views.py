from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ExamOrale, QuestionOrale

def exam_list(request):
    exams = ExamOrale.objects.all()
    return render(request, 'revision/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(ExamOrale, pk=exam_id)
    # Only get question numbers, not the heavy data
    questions = exam.questions.all().order_by('num_qst').values('num_qst', 'score')
    
    context = {
        'exam': exam,
        'questions': list(questions),
        'total_questions': exam.questions.count()
    }
    return render(request, 'revision/index.html', context)

def question_api(request, exam_id, question_num):
    """API endpoint to fetch a single question's data"""
    question = get_object_or_404(
        QuestionOrale, 
        exam_id=exam_id, 
        num_qst=question_num
    )
    
    data = {
        'num_qst': question.num_qst,
        'text_qst': question.text_qst,
        'image_qst': question.image_qst or '',
        'audio_url': question.audio_url or '',
        'has_audio': bool(question.audio_url),
        'choice_a': question.choice_a,
        'choice_b': question.choice_b,
        'choice_c': question.choice_c,
        'choice_d': question.choice_d,
        'score': question.score,
        'solution_qst': question.solution_qst,
    }
    return JsonResponse(data)


def all_questions_api(request, exam_id):
    """Fetch all questions for an exam with audio URL"""
    questions = QuestionOrale.objects.filter(exam_id=exam_id).order_by('num_qst')
    data = []
    for q in questions:
        data.append({
            'num_qst': q.num_qst,
            'text_qst': q.text_qst,
            'image_qst': q.image_qst or '',
            'audio_url': q.audio_url or '',
            'has_audio': bool(q.audio_url),
            'choice_a': q.choice_a,
            'choice_b': q.choice_b,
            'choice_c': q.choice_c,
            'choice_d': q.choice_d,
            'score': q.score,
            'solution_qst': q.solution_qst,
        })
    return JsonResponse({'questions': data})
