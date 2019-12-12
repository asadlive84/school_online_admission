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


class HomePage(generic.TemplateView):
    template_name = "students/home.html"


class UserProfileView(generic.UpdateView):

    # template_name = "students/my_profile.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        return render(request, "students/my_profile.html", {'user': user})


class AdmissionListView(generic.ListView):
    model = Student
    template_name = "students/admission_list.html"


class AdmissionDetailView(generic.DetailView):
    model = Student
    template_name = "students/admission_detail_view.html"


