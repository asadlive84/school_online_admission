from django.db import models


class SchoolClass(models.Model):
    """
    School class name Model with word and numeric
    """
    class_name = models.CharField('Class Name', unique=True, max_length=50)
    class_name_numeric = models.PositiveIntegerField('Class Name - Numeric', unique=True)

    def __str__(self):
        return f"{self.class_name}"


class AcademicSection(models.Model):
    """
    School Academic Section
    """
    section_name = models.CharField("Section Name", max_length=100)

    def __str__(self):
        return f"{self.section_name}"


class AcademicSession(models.Model):
    """
    School Academic Session
    """
    year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.year} - {self.year + 1}'


class StudentGroup(models.Model):
    """
    Student Group Name
    """
    group_name = models.CharField('Group Name', max_length=100, unique=True)

    def __str__(self):
        return f'{self.group_name}'


class Zilla(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Upazilla(models.Model):
    zilla = models.ForeignKey(Zilla, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.zilla.name}"


class Union(models.Model):
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.upazilla.zilla.name}-{self.upazilla.name}"


class WordNo(models.Model):
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    name = models.CharField("Word Name", max_length=100)
    name_of_numeric = models.PositiveIntegerField('Word No')

    def __str__(self):
        return f"{self.name}, {self.name_of_numeric} {self.union.name} {self.union.upazilla.name}"


class BloodGroup(models.Model):
    blood_group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.blood_group_name
