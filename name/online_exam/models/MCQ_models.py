from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class MCQ(models.Model):
    question_no = models.TextField(null=True, max_length=300)
    question = RichTextField(config_name='question')

    option_1 = RichTextField(config_name='mcq_answer', null=True)
    option_2 = RichTextField(config_name='mcq_answer', null=True)
    option_3 = RichTextField(config_name='mcq_answer', null=True)
    option_4 = RichTextField(config_name='mcq_answer', null=True)

    correct_ans = RichTextField(config_name='mcq_answer', null=True)

    score = models.IntegerField(default=0)
    status = models.IntegerField(default=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def get_short_name(self):
        return self.names




