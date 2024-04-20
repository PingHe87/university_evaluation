from django.shortcuts import render, redirect # type: ignore
from .forms import CourseForm, DegreeForm, DegreeQueryForm, InstructorForm, InstructorQueryForm, LearningObjectiveForm, SectionForm, EvaluationForm, DegreeCourseForm, CourseObjectiveForm, SectionQueryForm
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
    return render(request, 'university_evaluation/homepage.html')


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


def instructor_sections(request):
    if request.method == 'POST':
        form = InstructorQueryForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']
            instructor = form.cleaned_data['instructor']

            sections_taught = Section.objects.filter(
                instructor=instructor,
                year=year,
                semester=semester
            )

            return render(request, 'university_evaluation/instructor_sections_result.html', {'sections': sections_taught})
    else:
        form = InstructorQueryForm()

    return render(request, 'university_evaluation/instructor_query_form.html', {'form': form})


def degree_details(request):
    if request.method == 'POST':
        form = DegreeQueryForm(request.POST)
        if form.is_valid():
            degree = form.cleaned_data['degree']
            # course related to the degree
            courses = Course.objects.filter(degreecourse__degree=degree)
            # section related to the degree
            sections = Section.objects.filter(course__in=courses).order_by('year', 'semester')
            # objective related to the degree
            objectives = LearningObjective.objects.all()
            objectives_courses = {}
            for objective in objectives:
                objective_courses = Course.objects.filter(courseobjective__objective=objective)
                objectives_courses[objective] = objective_courses

            return render(request, 'university_evaluation/degree_details_result.html', {
                'degree': degree,
                'courses': courses,
                'sections': sections,
                'objectives': objectives,
                'objectives_courses': objectives_courses,
            })
    else:
        form = DegreeQueryForm()

    return render(request, 'university_evaluation/degree_query_form.html', {'form': form})
