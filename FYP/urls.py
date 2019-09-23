"""FYP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from depart import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('departments/', views.departmentPage, name='departments'),
    path('departments/<int:pk>/', views.department_details, name='department_details'),
    path('add_department/', views.addDepartmentPage, name='add_departments'),
    path('upload/', views.upload, name= 'upload'),
    path('books/', views.book_list, name= 'book_list'),
    path('books/upload/', views.upload_book, name= 'upload_book'),
    path('add_department_form_submission/', views.adddepartmentformsubmission, name='add_department_form_submission'),
 
    path('admin/', admin.site.urls),
]
