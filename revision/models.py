from django.db import models

class ExamOrale(models.Model):
    number_exam_orale = models.IntegerField(unique=True)
    description_exam_orale = models.TextField()

    def __str__(self):
        return f"Exam {self.number_exam_orale}"

class QuestionOrale(models.Model):
    exam = models.ForeignKey(ExamOrale, on_delete=models.CASCADE, related_name='questions')
    num_qst = models.IntegerField()
    image_qst = models.TextField(blank=True, null=True, help_text="Base64 encoded image")
    audio_url = models.URLField(blank=True, null=True, help_text="URL to audio file (CDN)")
    text_qst = models.TextField()
    choice_a = models.TextField(default="Option A")
    choice_b = models.TextField(default="Option B")
    choice_c = models.TextField(default="Option C")
    choice_d = models.TextField(default="Option D")
    solution_qst = models.TextField()
    score = models.IntegerField(default=1)

    def __str__(self):
        return f"Question {self.num_qst} for Exam {self.exam.number_exam_orale}"

class ExamEcrit(models.Model):
    number_exam_ecrit = models.IntegerField(unique=True)
    description_exam_ecrit = models.TextField()

    def __str__(self):
        return f"Exam Ecrit {self.number_exam_ecrit}"

class QuestionEcrit(models.Model):
    exam = models.ForeignKey(ExamEcrit, on_delete=models.CASCADE, related_name='questions')
    num_qst = models.IntegerField()
    image_qst = models.TextField(blank=True, null=True, help_text="Base64 encoded image")
    text_qst = models.TextField()
    choice_a = models.TextField(default="Option A")
    choice_b = models.TextField(default="Option B")
    choice_c = models.TextField(default="Option C")
    choice_d = models.TextField(default="Option D")
    solution_qst = models.TextField()
    score = models.IntegerField(default=1)

    def __str__(self):
        return f"Question {self.num_qst} for Exam Ecrit {self.exam.number_exam_ecrit}"
