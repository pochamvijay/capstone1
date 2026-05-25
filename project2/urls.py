from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index),

    path('insert/', views.insertdata),

    path('delete/<id>/', views.deleteData),

    path('edit/<id>/', views.editData),

    path('update/<id>/', views.updateData),

]