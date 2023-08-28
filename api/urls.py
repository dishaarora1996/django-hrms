from django.urls import path
from .views import *

urlpatterns = [
    path('holiday_list/', HolidayListView.as_view(), name="holiday_list"),
    path('hr_employee_list/', HREmployeeListView.as_view(), name="hr_employee_list"),
    path('onboarding_list/', HROnboardingListView.as_view(), name="onboarding_list"),
    path('hr_compensation_list/', HRCompensationListView.as_view(), name="hr_compensation_list"),
    path('hr_project_list/', HRProjectListView.as_view(), name="hr_project_list"),
    path('compensation_detail/', CompensationDetailView.as_view(), name="compensation_detail"),
    path('project_list/', ProjectListView.as_view(), name="project_list"),
    path('client_list/', ClientListView.as_view(), name="client_list"),
    path('manager_employee_list/', ManagerEmployeeListView.as_view(), name="manager_employee_list"),
]
