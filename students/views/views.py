from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from students.models import Student
from students.forms import StudentFrom
from users.models import CustomUser
from django.contrib.auth import logout, authenticate
from adminTools.models import BloodGroup, \
    StudentGroup, \
    AcademicSession, \
    SchoolClass, \
    Upazilla, \
    Union, \
    WordNo, \
    AcademicSection, \
    SchoolClass, \
    Zilla


class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = "students/home.html"
    login_url = "user/login/"


class UserProfileView(LoginRequiredMixin, generic.UpdateView):

    # template_name = "students/my_profile.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        return render(request, "students/my_profile.html", {'user': user})


class AdmissionListView(PermissionRequiredMixin, generic.ListView):
    model = Student
    template_name = "students/admission_list.html"
    permission_required = ("student.add_student",)


class AdmissionDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Student
    template_name = "students/admission_detail_view.html"
    permission_required = ("student.add_student",)


class NoPermissionError(generic.TemplateView):
    template_name = "students/no_permission_error.html"
