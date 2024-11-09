from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name = "index"),
    path("reporte_png", views.v_reportes_png, name = "reporte_png"),
]