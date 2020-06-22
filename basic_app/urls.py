from django.contrib import admin
from django.urls import path,include
from basic_app import views

urlpatterns = [
    path('quiz/',views.quiz,name="quiz"),
    path('answer/',views.answer,name='answer'),
    path('leader/',views.leader,name='leader')
]
