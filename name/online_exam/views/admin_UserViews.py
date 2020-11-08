from django.shortcuts import render
from signup_login.models import User
from django.http import HttpResponseRedirect
from online_exam.forms.UserForm import UserRegistrationForm


###################### User Detail View ###########################
def showUser(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            register = User(name=name, email=email,
                            password=password)
            register.save()
            form = UserRegistrationForm()

    studentshow = User.objects.all()
    context = {'form': form, 'studentshow': studentshow}
    return render(request, 'online_exam/admin/add_show.html', context)


def adminHome(request):
    return render(request, 'online_exam/admin/adminhome.html')


# fro delete

def delete(request, id):
    if request.method == 'POST':
        del_record = User.objects.get(pk=id)
        del_record.delete()
    return HttpResponseRedirect('/showUser/')


def edit(request, id):
    if request.method == 'POST':
        edit_record = User.objects.get(pk=id)
        form = UserRegistrationForm(request.POST,
                                    instance=edit_record)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect('/showUser/')
    else:
        edit_record = User.objects.get(pk=id)
        form = UserRegistrationForm(
            instance=edit_record)
    return render(request, 'online_exam/admin/edit.html', {'form': form})
