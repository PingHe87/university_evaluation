from django.db import models

# Create your models here.

class Degree(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)

    class Meta:
        unique_together = (('name', 'level'),)
        verbose_name_plural = "Degrees"

class Course(models.Model):
    course_number = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    section_number = models.IntegerField()
    enrollment_count = models.IntegerField()
    SEMESTER_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]
    def __str__(self):
        return f"{self.course.name} - {self.semester} {self.year}"

class LearningObjective(models.Model):
    code = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class Evaluation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    objective = models.ForeignKey(LearningObjective, on_delete=models.CASCADE)
    assessment_method = models.CharField(max_length=255)
    performance_A = models.IntegerField()
    performance_B = models.IntegerField()
    performance_C = models.IntegerField()
    performance_F = models.IntegerField()
    improvement_suggestions = models.TextField()

class DegreeCourse(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_core = models.BooleanField()

    class Meta:
        unique_together = (('degree', 'course'),)

class CourseObjective(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    objective = models.ForeignKey(LearningObjective, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'objective'),)
