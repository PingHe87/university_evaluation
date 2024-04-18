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

class SectionQueryForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, label='Course')
    year = forms.ChoiceField(choices=[(year, year) for year in range(2024, 2027)], required=True, label='Year')
    semester = forms.ChoiceField(choices=Section.SEMESTER_CHOICES, required=True, label='Semester')

    def __init__(self, *args, **kwargs):
        super(SectionQueryForm, self).__init__(*args, **kwargs)
        self.fields['course'].label_from_instance = lambda obj: "%s (%s)" % (obj.name, obj.course_number)

