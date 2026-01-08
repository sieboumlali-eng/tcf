import os
import django
import base64

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from revision.models import ExamOrale, QuestionOrale, ExamEcrit, QuestionEcrit

def populate():
    # Clear existing data
    ExamOrale.objects.all().delete()
    ExamEcrit.objects.all().delete()
    
    # Create Exam
    exam = ExamOrale.objects.create(
        number_exam_orale=1,
        description_exam_orale="B2 French Exam Practice"
    )
    
    # Read the existing hero image as a base64 string for the sample
    try:
        with open('revision/static/revision/hero.png', 'rb') as img_file:
            img_b64 = "data:image/png;base64," + base64.b64encode(img_file.read()).decode('utf-8')
    except:
        img_b64 = ""

    # Create Question 1
    QuestionOrale.objects.create(
        exam=exam,
        num_qst=1,
        image_qst=img_b64,
        audio_url="https://testtcf.b-cdn.net/Compr%C3%A9hension%20Orale/Compr%C3%A9hension%20Orale%20test%201/Q1.mp3",
        text_qst="Écoutez les 4 propositions, choisissez celle qui correspond à l'image",
        choice_a="A",
        choice_b="B",
        choice_c="C",
        choice_d="D",
        solution_qst="A",
        score=2
    )

    # Create Question 2
    QuestionOrale.objects.create(
        exam=exam,
        num_qst=2,
        image_qst=img_b64, 
        audio_url="https://testtcf.b-cdn.net/Compr%C3%A9hension%20Orale/Compr%C3%A9hension%20Orale%20test%2021/Q19.mp3",
        text_qst="Écoutez le dialogue et répondez : Où se passe la scène ?",
        choice_a="À la boulangerie",
        choice_b="À la gare",
        choice_c="Au cinéma",
        choice_d="À la piscine",
        solution_qst="A",
        score=3
    )

    print("Oral Exam populated.")

    # Create Written Exam
    exam_ecrit = ExamEcrit.objects.create(
        number_exam_ecrit=1,
        description_exam_ecrit="B2 Written Exam Practice"
    )

    # Create Question 1 for Written Exam
    QuestionEcrit.objects.create(
        exam=exam_ecrit,
        num_qst=1,
        image_qst=img_b64,
        text_qst="Lisez le texte et répondez à la question.",
        choice_a="Option A",
        choice_b="Option B",
        choice_c="Option C",
        choice_d="Option D",
        solution_qst="A",
        score=2
    )
    
    print("Database populated successfully.")

if __name__ == '__main__':
    populate()
