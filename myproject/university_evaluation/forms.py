# university_evaluation/forms.py
from django import forms
from .models import Course, Degree, Instructor, LearningObjective, Section, Evaluation, DegreeCourse, CourseObjective

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'name']  # Include only the fields from the Course model

class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['name', 'level']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name']

class LearningObjectiveForm(forms.ModelForm):
    class Meta:
        model = LearningObjective
        fields = ['code', 'title', 'description']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['course', 'year', 'semester', 'section_number', 'enrollment_count', 'instructor']

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['section', 'objective', 'assessment_method', 'performance_A', 'performance_B', 'performance_C', 'performance_F', 'improvement_suggestions']

class DegreeCourseForm(forms.ModelForm):
    class Meta:
        model = DegreeCourse
        fields = ['degree', 'course', 'is_core']

class CourseObjectiveForm(forms.ModelForm):
    class Meta:
        model = CourseObjective
        fields = ['course', 'objective']
