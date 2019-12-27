from datetime import date

from django.db import models
from django.urls import reverse
from django.utils import timezone
from adminTools.models import Zilla, \
    Upazilla, \
    Union, \
    WordNo, \
    SchoolClass, \
    AcademicSession, \
    StudentGroup, \
    AcademicSection, \
    BloodGroup
from django.conf import settings

MALE = 'M'
FEMALE = 'F'

GENDER = [
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
]

ISLAM = 'I'
HINDU = 'H'

RELIGION = [
    (ISLAM, 'Islam'),
    (HINDU, 'Hindu'),
]


def increment_unique_student_id():
    tz = str(timezone.now().year)[2:4]
    last_std = Student.objects.all().order_by('id').last()
    if not last_std:
        return 'FSS' + str(tz) + '1001'
    std_no = last_std.std_id
    new_std_int = int(std_no.split('FSS' + str(tz))[-1]) + 1
    new_std_id = 'FSS' + str(tz) + str(new_std_int)
    return new_std_id


class Student(models.Model):
    """
    This Model Design for student of school
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    full_name_bn = models.CharField('Full Name of Student - BN', max_length=100)
    full_name_en = models.CharField('Full Name of Student - EN', max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    std_id = models.CharField('Student ID',
                              max_length=100,
                              unique=True,
                              default=increment_unique_student_id,
                              null=True,
                              blank=True,
                              editable=False, )
    gender = models.CharField('Gender', choices=GENDER, default=MALE, max_length=1)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    religion = models.CharField('Religion', choices=RELIGION, default=ISLAM, max_length=1)
    father_name_bn = models.CharField('Father Name - BN', max_length=100)
    father_name_en = models.CharField('Father Name - EN', max_length=100)
    mother_name_bn = models.CharField('Mother Name - BN', max_length=100)
    mother_name_en = models.CharField('Mother Name - EN', max_length=100)
    date_of_birth = models.DateField('Date of Birth of Student')
    mobile_number = models.PositiveIntegerField('Mobile Number')
    optional_mobile_number = models.PositiveIntegerField('Mobile Number',
                                                         blank=True,
                                                         null=True)
    email_field = models.EmailField(unique=True, blank=True, null=True)
    std_status = models.BooleanField(default=False)
    last_school = models.CharField(max_length=300, blank=True, null=True)
    class_name = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    std_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    academic_section = models.ForeignKey(AcademicSection, on_delete=models.CASCADE)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    zilla = models.ForeignKey(Zilla, on_delete=models.CASCADE)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    word_no = models.ForeignKey(WordNo, on_delete=models.CASCADE)
    address = models.CharField("Address", blank=True, null=True, max_length=200)
    address_opt = models.TextField("Address", blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name_en} - {self.std_id}"

    def get_absolute_url(self):
        return reverse('student:admission_detail', args=[str(self.id)])

    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))