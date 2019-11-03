from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Search_Courses-Home'),
    path('about/', views.about, name='Search_Courses-about'),
    path('find_tutors/', views.find_tutors, name='Search_Courses-find_tutors'),
    path('for_teachers/', views.for_teachers, name='Search_Courses-for_teachers'),
    #path('submit/', views.submit, name='for_teachers-find_tutors')
]