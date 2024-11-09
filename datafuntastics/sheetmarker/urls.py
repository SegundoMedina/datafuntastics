from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reportes_xls", views.v_reportes_xls, name="v_reporte_xls"),
]