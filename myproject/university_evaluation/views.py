from django.shortcuts import render, redirect
from .forms import CourseForm, DegreeForm, InstructorForm, LearningObjectiveForm, SectionForm, EvaluationForm, DegreeCourseForm, CourseObjectiveForm
from .models import Course, Degree, Instructor, LearningObjective, Section, Evaluation, DegreeCourse, CourseObjective

def course_list(request):
    # 获取所有课程对象
    courses = Course.objects.all()
    # 将课程对象传递给模板
    return render(request, 'course_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage or any other desired URL
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

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
