from django.shortcuts import render, redirect
from .forms import CourseForm, DegreeForm, SectionQueryForm, LearningObjectiveForm, SectionForm, EvaluationForm, DegreeCourseForm, CourseObjectiveForm
from .models import Course, Degree, Instructor, LearningObjective, Section, Evaluation, DegreeCourse, CourseObjective

def course_list(request):
    # 获取所有课程对象
    courses = Course.objects.all()
    # 将课程对象传递给模板
    return render(request, 'university_evaluation/course_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage or any other desired URL
    else:
        form = CourseForm()
    return render(request, 'university_evaluation/create_course.html', {'form': form})

def create_degree(request):
    if request.method == 'POST':
        form = DegreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DegreeForm()
    return render(request, 'create_degree.html', {'form': form})

# Repeat similar create views for other models...

def home(request):
    # Add logic to fetch data or perform any other operations
    return render(request, 'home.html')


def query_sections(request):
    if request.method == 'POST':
        form = SectionQueryForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']

            sections = Section.objects.filter(
                course=course,
                year=year,
                semester=semester
            )

            return render(request, 'university_evaluation/sections_result.html', {'sections': sections})
    else:
        form = SectionQueryForm()

    return render(request, 'university_evaluation/query.html', {'form': form})
