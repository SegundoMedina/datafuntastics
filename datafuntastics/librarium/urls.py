from django.urls import path

from . import views
urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reportes_pdf", views.v_reportes_pdf, name="v_reporte_pdf"),
]