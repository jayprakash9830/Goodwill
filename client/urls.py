from django.urls import path
from . import views

urlpatterns = [
       path('',views.index,name="index"),
    path('.',views.index,name="index"),
    path('about',views.about,name="about"),
    path('teacher',views.tutorRegister,name="teacher"),
    path('student',views.studentRegister,name="student"),
    path('contact',views.contact,name="contact"),
    path('success',views.submit,name="submit")
]