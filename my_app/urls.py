from django.urls import path
from .views import Home, scheduler, delete_task, cv, addEdu, addWork, addSkill, new_cv, pdfCv, html_to_pdf_view

urlpatterns = [
    path('', Home, name="home"),
    path('scheduler', scheduler, name='scheduler'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('cv', cv, name='cv'),
    path('addEdu', addEdu, name='addEdu'),
    path('addWork', addWork, name='addWork'),
    path('addSkill', addSkill, name='addSkill'),
    path('new_cv/<int:id>/', new_cv, name='new_cv'),
    path("pdfcv", pdfCv, name="pdfcv"),
    path("html_to_pdf_view", html_to_pdf_view, name="html_to_pdf_view"),
]