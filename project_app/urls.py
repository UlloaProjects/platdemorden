from django.urls import path
from project_app import views

app_name = 'project_app'

urlpatterns = [
    path('register', views.register, name='register'),
    path('upload/', views.upload_files, name='uploads'),
    path('user_login/', views.user_login, name='user_login'),

]
