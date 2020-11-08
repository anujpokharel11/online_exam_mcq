from django.urls import path
from online_exam.views import admin_UserViews,admin_MCQViews,online_exam_views

urlpatterns = [
    path('adminhome/', admin_UserViews.adminHome, name='adminhome'),
    path('delete/<int:id>/',admin_UserViews.delete,name='delete'), # <int:id> => this gives id when delete button press.
    path('edit/<int:id>/', admin_UserViews.edit, name='edit'),
    path('showUser/', admin_UserViews.showUser, name='showUser'),

    path('create_mcq/', admin_MCQViews.createMCQ, name='create_mcq'),
    path('result/', online_exam_views.scoreDetail, name='result'),
]


