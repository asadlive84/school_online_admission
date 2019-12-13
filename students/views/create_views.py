from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from adminTools.models import BloodGroup, SchoolClass, StudentGroup, AcademicSection, AcademicSession, Zilla, Upazilla, \
    Union, WordNo, SchoolInformation, AdmissionApproval
from students.forms import StudentFrom, SchoolInfoFormCrateView, AdmissionApprovalStatusForm
from students.models import Student


class AdmissionCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Student
    form_class = StudentFrom
    template_name = "students/create/admission_create.html"
    permission_denied_message = "You dont have access"
    permission_required = ("student.add_student",)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse("student:admission_detail", args=[str(self.object.id)]))

    def get_initial(self, *args, **kwargs):
        initial = super(AdmissionCreateView, self).get_initial(**kwargs)
        initial['created_by'] = self.request.user
        return initial


class BloodGroupCreateView(PermissionRequiredMixin, generic.CreateView):
    model = BloodGroup
    fields = "__all__"
    template_name = "students/create/create_blood_group.html"
    success_url = reverse_lazy('student:blood_create')
    permission_required = ("bloodgroup.add_bloodgroup",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = BloodGroup.objects.all()
        return context


class ClassCreateView(PermissionRequiredMixin, generic.CreateView):
    model = SchoolClass
    fields = "__all__"
    template_name = "students/create/create_std_class.html"
    success_url = reverse_lazy('student:class_create')
    permission_required = ("schoolclass.add_schoolclass", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = SchoolClass.objects.all()
        return context


class DepartmentCreateView(PermissionRequiredMixin, generic.CreateView):
    model = StudentGroup
    fields = "__all__"
    template_name = "students/create/create_std_group.html"
    success_url = reverse_lazy('student:department_create')
    permission_required = ("studentgroup.add_studentgroup", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = StudentGroup.objects.all()
        return context


class SectionCreateView(PermissionRequiredMixin, generic.CreateView):
    model = AcademicSection
    fields = "__all__"
    template_name = "students/create/create_academic_section.html"
    success_url = reverse_lazy('student:section_create')
    permission_required = ("academicsection.add_academicsession", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = AcademicSection.objects.all()
        return context


class SessionCreateView(PermissionRequiredMixin, generic.CreateView):
    model = AcademicSession
    fields = "__all__"
    template_name = "students/create/create_academic_session.html"
    success_url = reverse_lazy('student:session_create')
    permission_required = ("academicsession.add_academicsection", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = AcademicSession.objects.all()
        return context


class ZillaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Zilla
    fields = "__all__"
    template_name = "students/create/create_zilla.html"
    success_url = reverse_lazy('student:zilla_create')
    permission_required = ("academicsession.add_academicsection",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Zilla.objects.all()
        return context


class UpazillaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Upazilla
    fields = "__all__"
    template_name = "students/create/create_upazilla.html"
    success_url = reverse_lazy('student:upazilla_create')
    permission_required = ("upazilla.add_upazilla",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Upazilla.objects.all()
        return context


class UnionCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Union
    fields = "__all__"
    template_name = "students/create/create_union.html"
    success_url = reverse_lazy('student:union_create')
    permission_required = ("union.add_union")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Union.objects.all()
        return context


class WordCreateView(LoginRequiredMixin, generic.CreateView):
    model = WordNo
    fields = "__all__"
    template_name = "students/create/create_word.html"
    success_url = reverse_lazy('student:word_create')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = WordNo.objects.all()
        return context


class SchoolInfoCrateView(PermissionRequiredMixin, generic.CreateView):
    model = SchoolInformation
    form_class = SchoolInfoFormCrateView
    template_name = "students/create/school_info_create.html"
    success_url = reverse_lazy('student:school_info_create')
    permission_required = ("schoolinformation.add_schoolinformation",)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse("student:school_info_create"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = SchoolInformation.objects.all()
        return context


class AdmissionPDFCreate(PermissionRequiredMixin, generic.CreateView):
    model = Student
    fields = "__all__"
    template_name = "students/create/create_admission_pdf.html"
    permission_required = ("student.add_student", 'student.view_student')

    # success_url = reverse_lazy('student:admission_pdf_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Student.objects.all()
        return context


class AdmissionApprovalView(PermissionRequiredMixin, generic.CreateView):
    model = AdmissionApproval
    form_class = AdmissionApprovalStatusForm
    template_name = "students/create/create_admission_permission.html"
    permission_required = ("admissionapproval.add_admissionapproval",)

    def form_valid(self, form):
        std = Student.objects.get(pk=self.kwargs['std_id'])
        form.instance.student = std
        form.instance.status_by = self.request.user
        form.instance.save()
        return HttpResponseRedirect(reverse("student:admission_detail", args=[str(std.pk)]))
