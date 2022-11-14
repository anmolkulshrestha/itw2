from django.urls import path
from .views import *

urlpatterns = [
    path('student-home/', student_home, name='student_home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]