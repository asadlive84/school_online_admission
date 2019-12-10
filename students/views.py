from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from students.models import Student
from students.forms import StudentFrom


class AdmissionListView(generic.ListView):
    model = Student
    template_name = "students/admission_list.html"


class AdmissionDetailView(generic.DetailView):
    model = Student
    template_name = "students/admission_detail_view.html"


class AdmissionCreateView(generic.CreateView):
    model = Student
    form_class = StudentFrom
    template_name = "students/admission_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect("/")

    def get_initial(self, *args, **kwargs):
        initial = super(AdmissionCreateView, self).get_initial(**kwargs)
        initial['created_by'] = self.request.user
        return initial
