from ckeditor.fields import RichTextField
from django.db import models
from signup_login.models import User

from online_exam.models.MCQ_models import MCQ
from django.db.models import Sum, Count


class StudentTest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_student')
    test_question = models.ForeignKey(MCQ, on_delete=models.CASCADE, related_name='std_test_question')
    test_answer = RichTextField(config_name='answer')
    correct_answer = models.CharField(max_length=300, null=True)
    score = models.IntegerField(default=0, null=True)

    def get_total_score(self):
        total_score = self.StudentTest.aggregate(Sum('score'))
        return total_score


class StudentRank(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_rank')
    total_score = models.IntegerField(default=0, null=True)
    Rank = models.IntegerField(default=0, null=True)

    def ranking(self):
        aggregate = StudentRank.objects.filter(total_score__lt=self.score).aggregate(ranking=Count('total_score'))
        return aggregate['ranking'] + 1

