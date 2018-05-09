from django.urls import path
from project_app import views

app_name = 'my_app'
urlpatterns = [
    path('upload/<int:pk>', views.UserUpdateView.as_view(), name='upload'),
    path('user_detail/<int:pk>', views.UserDetailView.as_view(), name='details'),
    path('file_upload', views.Inputfiles, name='inputfiles'),
    path('imprimir_archivo', views.proc_dem_file, name="imprimir"),
    path('suavizar', views.funcion_demandas, name="suavizar"),
]
