from django.urls import path
from .views import *
urlpatterns = [
    path('home/', homepage,name="home"),
    # path('login/',login, name="login"),
    path('login/', Login_user, name='login'),
    path('searchProf/', searchProf, name="searchProf"),
    path('searchEtud/', searchEtud, name="searchEtud"),
    path('etudiants/', etudiant_list, name='etudiant_list'),
    path('students/',DisplayStudentsList, name="students_list"),
    path('prof/',prof_list, name="prof_list"),
    path('excel/', excel_view, name='excel_view'),
    path('chart/', chart_view, name='chart_view'),
]