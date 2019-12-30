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
    photo = models.ImageField(upload_to='images/', blank=True, default='images/std_images.png')
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

    # Python program to calculate range

    def findAge(self):
        today = date.today()
        current_date = date.today()
        current_year = int(date.today().year)
        current_month = int(date.today().month)
        birth_date = self.date_of_birth.day
        birth_month = int(self.date_of_birth.month)
        birth_year = int(self.date_of_birth.year)

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if birth_date > current_date.month:
            current_month = today.month - 1
            current_date = (today.day + month[birth_month - 1])
        else:
            current_date = current_date.day
        if birth_month > current_month:
            current_year = current_year - 1
            current_month = current_month + 12

        # calculate date, month, year
        print(f"XXXX {current_date} - - {birth_date}")
        calculated_date = current_date - birth_date
        calculated_month = current_month - birth_month
        calculated_year = current_year - birth_year

        # print present age
        return f"Year:{calculated_year}, Month:{calculated_month}, Days:{calculated_date}"

    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
