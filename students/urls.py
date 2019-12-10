from django.urls import path
from students.views import AdmissionCreateView, AdmissionDetailView, AdmissionListView

app_name = "student"


urlpatterns = [
    path("", AdmissionCreateView.as_view(), name="admission_create"),
    path("admission-details/<int:pk>/", AdmissionDetailView.as_view(), name="admission_detail"),
    path("admission-list/", AdmissionListView.as_view(), name="admission_list"),
]


