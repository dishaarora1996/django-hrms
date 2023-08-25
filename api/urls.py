from django.urls import path
from .views import *

urlpatterns = [
    path('holiday_list/', HolidayListView.as_view(), name="holiday_list"),
    path('hr_employee_list/', HREmployeeListView.as_view(), name="hr_employee_list"),
]
