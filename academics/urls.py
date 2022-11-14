from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('programs/<int:code>', program, name='programs'),
    path('facilities/', facility, name='facility'),
    path('scholarships/', scholarship, name='scholarship'),
    path('contact-us/', contact_us, name="contact_us"),
    path('about-us/',about_us, name="about_us"),
    path('grades/',grades, name="grades"),
    path('attendance/',attendance, name="attendance"),
    path('classes/',classes, name="classes"),
]
