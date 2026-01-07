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
        'has_audio': bool(question.audio_qst),
        'choice_a': question.choice_a,
        'choice_b': question.choice_b,
        'choice_c': question.choice_c,
        'choice_d': question.choice_d,
        'score': question.score,
        'solution_qst': question.solution_qst,
    }
    return JsonResponse(data)

    return JsonResponse(data)

def question_audio_api(request, exam_id, question_num):
    """API endpoint to fetch just the audio data as binary stream"""
    import base64
    from django.http import HttpResponse

    question = get_object_or_404(
        QuestionOrale, 
        exam_id=exam_id, 
        num_qst=question_num
    )
    
    if not question.audio_qst:
        return HttpResponse("", status=404)

    # Clean base64 string
    audio_data = question.audio_qst
    if "base64," in audio_data:
        audio_data = audio_data.split("base64,")[1]
    
    try:
        binary_data = base64.b64decode(audio_data)
        response = HttpResponse(binary_data, content_type='audio/mpeg')
        response['Content-Length'] = len(binary_data)
        response['Accept-Ranges'] = 'bytes'
        return response
    except Exception as e:
        print(f"Error decoding audio: {e}")
        return HttpResponse("Error decoding audio", status=500)

def all_questions_api(request, exam_id):
    """Fetch all questions for an exam without audio data"""
    questions = QuestionOrale.objects.filter(exam_id=exam_id).order_by('num_qst')
    data = []
    for q in questions:
        data.append({
            'num_qst': q.num_qst,
            'text_qst': q.text_qst,
            'image_qst': q.image_qst or '',
            'has_audio': bool(q.audio_qst),
            'choice_a': q.choice_a,
            'choice_b': q.choice_b,
            'choice_c': q.choice_c,
            'choice_d': q.choice_d,
            'score': q.score,
            'solution_qst': q.solution_qst,
        })
    return JsonResponse({'questions': data})
