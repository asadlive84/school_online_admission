from adminTools.models import SchoolInformation, AdmissionApproval
from students.models import Student
from django import forms


class SchoolInfoFormCrateView(forms.ModelForm):
    class Meta:
        model = SchoolInformation
        fields = ("name", "description", "contact", "logo",)


class StudentFrom(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('full_name_bn',
                  'full_name_en',
                  'photo',
                  'gender',
                  'blood_group',
                  'religion',
                  'father_name_bn',
                  'father_name_en',
                  'mother_name_bn',
                  'mother_name_en',
                  'date_of_birth',
                  'mobile_number',
                  'optional_mobile_number',
                  'email_field',
                  'last_school',
                  'class_name',
                  'std_group',
                  'academic_section',
                  'academic_session',
                  'zilla',
                  'upazilla',
                  'union',
                  'word_no',
                  'address',
                  'address_opt',)

        exclude = ('created_by', 'std_id',)

        def __init__(self, *args, **kwargs):
            super(StudentFrom, self).__init__(*args, **kwargs)


class AdmissionApprovalStatusForm(forms.ModelForm):
    class Meta:
        model = AdmissionApproval
        fields = ("status", "message")
