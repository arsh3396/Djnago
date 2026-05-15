from django.urls import path

from . import views

urlpatterns = [
    path('<int:emp_id>/', views.employee_detail, )
]