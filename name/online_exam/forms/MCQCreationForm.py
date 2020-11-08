from django import forms
from online_exam.models.MCQ_models import MCQ
from ckeditor.fields import RichTextField


class MCQForm(forms.ModelForm):
    question = RichTextField(error_messages={"required": "Question is required"})
    question_no = forms.CharField(max_length=254, required=True, error_messages={"required": "Question no is required"})
    score = forms.CharField(max_length=300, required=False, error_messages={"required": "Score is required"})
    order = forms.CharField(max_length=300, required=False, error_messages={"required": "Order is required"})
    option_1 = RichTextField(error_messages={"required": "Option_1 is required"})
    option_2 = RichTextField(error_messages={"required": "Option_2 is required"})
    option_3 = RichTextField(error_messages={"required": "Option_3 is required"})
    option_4 = RichTextField(error_messages={"required": "Option_4 is required"})

    correct_ans = RichTextField(error_messages={"required": "Correct answer is required"})

    class Meta:
        model = MCQ
        fields = (
            'question', 'question_no', 'score', 'order', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_ans')
