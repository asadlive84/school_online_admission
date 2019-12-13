from django.contrib import admin
from students.models import Student
from users.models import CustomUser
from adminTools.models import \
    SchoolClass, \
    StudentGroup, \
    AcademicSection, \
    AcademicSession, \
    Zilla, \
    Union, \
    Upazilla, \
    WordNo, \
    BloodGroup, SchoolInformation, AdmissionApproval

admin.site.register(Student)
admin.site.register(SchoolClass)
admin.site.register(StudentGroup)
admin.site.register(AcademicSection)
admin.site.register(AcademicSession)

admin.site.register(Zilla)
admin.site.register(Upazilla)
admin.site.register(Union)
admin.site.register(WordNo)
admin.site.register(BloodGroup)
admin.site.register(SchoolInformation)
admin.site.register(AdmissionApproval)
admin.site.register(CustomUser)
