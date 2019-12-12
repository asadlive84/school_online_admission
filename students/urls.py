from django.urls import path
from students.views import views
from students.views import create_views
from students.views import create_pdf_admission


app_name = "student"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("blood-create/", create_views.BloodGroupCreateView.as_view(), name="blood_create"),
    path("class-create/", create_views.ClassCreateView.as_view(), name="class_create"),
    path("department-create/", create_views.DepartmentCreateView.as_view(), name="department_create"),
    path("session-create/", create_views.SessionCreateView.as_view(), name="session_create"),
    path("zilla-create/", create_views.ZillaCreateView.as_view(), name="zilla_create"),
    path("upazilla-create/", create_views.UpazillaCreateView.as_view(), name="upazilla_create"),
    path("union-create/", create_views.UnionCreateView.as_view(), name="union_create"),
    path("word-create/", create_views.WordCreateView.as_view(), name="word_create"),
    path("std-admission-create/<int:pk>/", create_pdf_admission.Pdf.as_view(), name="admission_pdf_create"),

    path("section-create/", create_views.SectionCreateView.as_view(), name="section_create"),
    path("admission-create/", create_views.AdmissionCreateView.as_view(), name="admission_create"),
    path("student-details/<int:pk>/", views.AdmissionDetailView.as_view(), name="admission_detail"),
    path("admission-list/", views.AdmissionListView.as_view(), name="admission_list"),
    path("my-profile/", views.UserProfileView.as_view(), name="my_profile"),
]
