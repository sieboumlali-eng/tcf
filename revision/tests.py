from django.test import TestCase, Client
from django.urls import reverse
from .models import ExamOrale, QuestionOrale

class RevisionViewTests(TestCase):
    def setUp(self):
        self.exam = ExamOrale.objects.create(number_exam_orale=1, description_exam_orale="Test Exam")
        self.question = QuestionOrale.objects.create(
            exam=self.exam,
            num_qst=1,
            text_qst="Test Question",
            solution_qst="A",
            audio_qst="raw_base64_string"
        )
    
    def test_audio_property(self):
        # Check that prefix is added
        self.assertEqual(self.question.audio_data_url, "data:audio/mpeg;base64,raw_base64_string")
        
        # Check that prefix is not duplicated
        self.question.audio_qst = "data:audio/wav;base64,existing_prefix"
        self.question.save()
        self.assertEqual(self.question.audio_data_url, "data:audio/wav;base64,existing_prefix")

    def test_exam_list(self):
        client = Client()
        response = client.get(reverse('exam_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Exam 1')
        self.assertContains(response, 'Oral Exams')

    def test_exam_detail(self):
        client = Client()
        response = client.get(reverse('exam_detail', args=[self.exam.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Question 1')
        # Check that we don't have 39 placeholders if only 1 question
        self.assertNotContains(response, '39')
        # Check for audio element base structure (class real-audio or similar if used)
        # Note: In test environment, population script didn't run, so audio_qst might be empty unless we set it in setUp
