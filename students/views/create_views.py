from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from adminTools.models import BloodGroup, SchoolClass, StudentGroup, AcademicSection, AcademicSession, Zilla, Upazilla, \
    Union, WordNo
from students.forms import StudentFrom
from students.models import Student


class AdmissionCreateView(generic.CreateView):
    model = Student
    form_class = StudentFrom
    template_name = "students/create/admission_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse("student:admission_detail", args=[str(self.object.id)]))

    def get_initial(self, *args, **kwargs):
        initial = super(AdmissionCreateView, self).get_initial(**kwargs)
        initial['created_by'] = self.request.user
        return initial


class BloodGroupCreateView(generic.CreateView):
    model = BloodGroup
    fields = "__all__"
    template_name = "students/create/create_blood_group.html"
    success_url = reverse_lazy('student:blood_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = BloodGroup.objects.all()
        return context


class ClassCreateView(generic.CreateView):
    model = SchoolClass
    fields = "__all__"
    template_name = "students/create/create_std_class.html"
    success_url = reverse_lazy('student:class_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = SchoolClass.objects.all()
        return context


class DepartmentCreateView(generic.CreateView):
    model = StudentGroup
    fields = "__all__"
    template_name = "students/create/create_std_group.html"
    success_url = reverse_lazy('student:department_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = StudentGroup.objects.all()
        return context


class SectionCreateView(generic.CreateView):
    model = AcademicSection
    fields = "__all__"
    template_name = "students/create/create_academic_section.html"
    success_url = reverse_lazy('student:section_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = AcademicSection.objects.all()
        return context


class SessionCreateView(generic.CreateView):
    model = AcademicSession
    fields = "__all__"
    template_name = "students/create/create_academic_session.html"
    success_url = reverse_lazy('student:session_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = AcademicSession.objects.all()
        return context


class ZillaCreateView(generic.CreateView):
    model = Zilla
    fields = "__all__"
    template_name = "students/create/create_zilla.html"
    success_url = reverse_lazy('student:zilla_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Zilla.objects.all()
        return context


class UpazillaCreateView(generic.CreateView):
    model = Upazilla
    fields = "__all__"
    template_name = "students/create/create_upazilla.html"
    success_url = reverse_lazy('student:upazilla_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Upazilla.objects.all()
        return context


class UnionCreateView(generic.CreateView):
    model = Union
    fields = "__all__"
    template_name = "students/create/create_union.html"
    success_url = reverse_lazy('student:union_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Union.objects.all()
        return context


class WordCreateView(generic.CreateView):
    model = WordNo
    fields = "__all__"
    template_name = "students/create/create_word.html"
    success_url = reverse_lazy('student:word_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = WordNo.objects.all()
        return context


class AdmissionPDFCreate(generic.CreateView):
    model = Student
    fields = "__all__"
    template_name = "students/create/create_admission_pdf.html"
    #success_url = reverse_lazy('student:admission_pdf_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Student.objects.all()
        return context
