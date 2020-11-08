from ckeditor.fields import RichTextField
from django import forms
from online_exam.models.StudentTest_models import StudentTest


class StudentTestCreateForm(forms.ModelForm):
    class Meta:
        model = StudentTest
        fields = ['test_question','test_answer','correct_answer',]
