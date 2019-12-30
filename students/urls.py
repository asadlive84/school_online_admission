from django.urls import path
from students.views import views, update, std_barcode
from students.views import create_views
from students.views import weasypdf
from students.views import create_pdf_admission
from students.views import create_html_pdf

# from wkhtmltopdf.views import PDFTemplateView


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
    path("std-admission-create/<int:pk>/", weasypdf.student_admit_card_receipt, name="admission_pdf_create"),
    path("school_info_create/", create_views.SchoolInfoCrateView.as_view(), name="school_info_create"),
    path("admission-appoval-view/<int:std_id>/", create_views.AdmissionApprovalView.as_view(),
         name="admission_approval"),

    path("std-admission-create/", create_pdf_admission.render_pdf_view, name="admission_pdf_create1"),

    path("section-create/", create_views.SectionCreateView.as_view(), name="section_create"),
    path("admission-create/", create_views.AdmissionCreateView.as_view(), name="admission_create"),
    path("student-details/<int:pk>/", views.AdmissionDetailView.as_view(), name="admission_detail"),
    path("admission-list/", views.AdmissionListView.as_view(), name="admission_list"),
    path("my-profile/", views.UserProfileView.as_view(), name="my_profile"),
    path("no-permission-error/", views.NoPermissionError.as_view(), name="no_permission_error"),
    path('student_view/<int:pk>/', update.StudentUpdateView.as_view(), name="student_update_view"),
    path("admission-card/<int:pk>/", create_html_pdf.StudentAdmissionPdf.as_view(), name="student_pdf"),
    path('barcode/', std_barcode.barcode, name="barcode"),
]
