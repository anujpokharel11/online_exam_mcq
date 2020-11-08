from time import strptime

from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datetime_safe import strftime
from online_exam.models.MCQ_models import MCQ
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from online_exam.forms.StudentTestCreateForm import StudentTestCreateForm
import sweetify

from online_exam.services.StudentTest_services import addTest

from online_exam.models.StudentTest_models import StudentTest, StudentRank
import simplejson as json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import pytz
from django.utils import timezone


def exam_homepage(request):
    if request.method == 'GET':
        display_question = MCQ.objects.all()
        # paginator = Paginator(display_question, 2)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        Np_time = pytz.timezone('Asia/Kathmandu')
        current_date = datetime.datetime.now(Np_time)
        current_date = current_date.strftime("%H-%M-%S")
        print(current_date)

        if current_date >= '1   0 - 00 - 00' and current_date <= '12 - 00 - 00':
            show = True
        else:
            show = False

        # context = {'page_obj': page_obj, 'show': show}
        context = {'show': show, 'questions': display_question}

        return render(request, 'online_exam/exam_homepage.html', context)

    if request.method == 'POST':
        try:
            student_id = request.POST.get('student_id')
            test_question_id = request.POST.getlist('question_id')
            test_answer = request.POST.getlist('answer')
            correct_answer = request.POST.getlist('correct_ans')

            for i in range(len(test_answer)):
                StudentTestInstance = StudentTest()
                StudentTestInstance.student_id = student_id
                StudentTestInstance.test_question_id = test_question_id[i]
                StudentTestInstance.correct_answer = correct_answer[i]
                StudentTestInstance.test_answer = test_answer[i]
                if test_answer[i].strip() == correct_answer[i].strip():
                    StudentTestInstance.score = 1
                else:
                    StudentTestInstance.score = 0
                StudentTestInstance.save()

            StudentRanKInstance = StudentRank()
            total_score = StudentTest.objects.filter(student_id=request.user.id).aggregate(Sum('score'))
            StudentRanKInstance.student_id = student_id
            StudentRanKInstance.total_score = total_score.get('score__sum')
            StudentRanKInstance.save()

            # if test_answer[i].strip() == correct_answer[i].strip():
            #     StudentScoreDetailInstance = StudentScoreDetail()
            #     StudentScoreDetailInstance.student_id = student_id
            #     StudentScoreDetailInstance.score = 1
            #     StudentScoreDetailInstance.test_question_id = test_question_id[i]
            #     StudentScoreDetailInstance.save()
            #
            # else:
            #     StudentScoreDetailInstance = StudentScoreDetail()
            #     StudentScoreDetailInstance.student_id = student_id
            #     StudentScoreDetailInstance.test_question_id = test_question_id[i]
            #     StudentScoreDetailInstance.save()

            rank = StudentRank.objects.all().order_by('-total_score')
            for i in range(len(rank)):
                rank[i].Rank = i + 1
                rank[i].save()

            sweetify.success(request, 'Thanks for appearing in exam.Your paper has been submitted.', persistent='Close')
        except Exception as e:

            sweetify.error(request, 'Something Went Wrong', text=str(e), persistent='Close')
        return redirect('/result/')


def scoreDetail(request):
    tests = StudentTest.objects.filter(student_id=request.user.id)
    total_score = StudentTest.objects.filter(student_id=request.user.id).aggregate(Sum('score'))
    stu_rank = StudentRank.objects.filter(student_id=request.user.id)

    # rank = StudentRank.objects.all().order_by('-total_score')
    # count = 0
    # for i in range(len(rank)):
    #     rank[i].Rank = i+1
    #     rank[i].save()
    #     print(rank[i])
    #

    context = {'tests': tests, 'total_score': total_score, 'stu_rank': stu_rank}
    return render(request, 'online_exam/result_page.html', context)
