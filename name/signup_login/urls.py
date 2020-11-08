from django.urls import path
from . import views
from online_exam.views import online_exam_views
from online_exam.views import admin_UserViews


urlpatterns = [
    path('', views.user_login, name='login'),

    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_changepass, name='changepass'),

    path('homepage/', online_exam_views.exam_homepage, name='clienthome'),
    path('adminhome/', admin_UserViews.adminHome, name='adminhome'),

]





