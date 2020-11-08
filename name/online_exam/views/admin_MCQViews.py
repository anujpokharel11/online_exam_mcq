from django.shortcuts import render, redirect
from online_exam.forms.MCQCreationForm import MCQForm
from online_exam.services.MCQ_services import addMCQ
from online_exam.models.MCQ_models import MCQ
import sweetify


def createMCQ(request):
    if request.method == 'GET':
        total_question = MCQ.objects.all().count()
        form = MCQForm()
        context = {'form': form,'total_que':total_question}
        return render(request, 'online_exam/backend/create_mcq.html', context)

    data = request.POST
    form = MCQForm(data)

    if form.is_valid():
        try:
            addMCQ(form)

            sweetify.success(request, 'Question created successfully', persistent='Close')

        except Exception as e:
            sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
        return redirect('create_mcq')
    else:
        if form.errors:
            for field in form:
                for error in field.errors:
                    sweetify.error(request, 'Something Went Wrong', text=error, persistent='Close')
                for error in form.non_field_errors():
                    sweetify.error(request, 'Something Went Wrong', text=error, persistent='Close')
        return redirect('create_mcq')
