from django.core.management.base import BaseCommand
from university_evaluation.models import Course, Degree, Instructor, LearningObjective, Section, Evaluation, DegreeCourse, CourseObjective

class Command(BaseCommand):
    help = 'Populates the database with some sample data'

    def handle(self, *args, **options):
        # 创建一些假数据
        # Courses
        course1 = Course.objects.create(course_number='CS101', name='Introduction to Computer Science')
        course2 = Course.objects.create(course_number='CS102', name='Data Structures')
        course3 = Course.objects.create(course_number='CS103', name='Algorithms')
        course4 = Course.objects.create(course_number='CS104', name='Database Systems')
        course5 = Course.objects.create(course_number='CS105', name='Web Development')
        course6 = Course.objects.create(course_number='CS106', name='Artificial Intelligence')
        
        # Degrees
        degree1 = Degree.objects.create(name='Computer Science', level='Bachelor')
        degree2 = Degree.objects.create(name='Information Technology', level='Bachelor')
        degree3 = Degree.objects.create(name='Software Engineering', level='Bachelor')
        
        # Instructors
        instructor1 = Instructor.objects.create(name='John Doe')
        instructor2 = Instructor.objects.create(name='Jane Smith')
        instructor3 = Instructor.objects.create(name='Michael Johnson')
        
        # LearningObjectives
        objective1 = LearningObjective.objects.create(code='LO1', title='Understand basic concepts', description='Understanding the basic concepts of computer science')
        objective2 = LearningObjective.objects.create(code='LO2', title='Apply data structures', description='Applying data structures in problem solving')
        objective3 = LearningObjective.objects.create(code='LO3', title='Design efficient algorithms', description='Designing algorithms for optimization')
        objective4 = LearningObjective.objects.create(code='LO4', title='Manage databases', description='Managing and querying databases effectively')
        objective5 = LearningObjective.objects.create(code='LO5', title='Develop web applications', description='Developing dynamic web applications using modern frameworks')
        objective6 = LearningObjective.objects.create(code='LO6', title='Implement AI algorithms', description='Implementing artificial intelligence algorithms for various applications')

        # Sections
        section1 = Section.objects.create(course=course1, year=2024, semester='Fall', section_number=1, enrollment_count=30, instructor=instructor1)
        section2 = Section.objects.create(course=course2, year=2024, semester='Spring', section_number=1, enrollment_count=25, instructor=instructor2)
        section3 = Section.objects.create(course=course3, year=2024, semester='Fall', section_number=1, enrollment_count=20, instructor=instructor3)
        section4 = Section.objects.create(course=course4, year=2024, semester='Spring', section_number=1, enrollment_count=28, instructor=instructor1)
        section5 = Section.objects.create(course=course5, year=2024, semester='Fall', section_number=1, enrollment_count=35, instructor=instructor2)
        section6 = Section.objects.create(course=course6, year=2024, semester='Spring', section_number=1, enrollment_count=22, instructor=instructor3)

        # Evaluations
        Evaluation.objects.create(section=section1, objective=objective1, assessment_method='Exam', performance_A=5, performance_B=15, performance_C=10, performance_F=0, improvement_suggestions='None')
        Evaluation.objects.create(section=section2, objective=objective2, assessment_method='Project', performance_A=10, performance_B=10, performance_C=5, performance_F=0, improvement_suggestions='More practice problems')
        # Add evaluations for other sections if needed

        # DegreeCourses
        DegreeCourse.objects.create(degree=degree1, course=course1, is_core=True)
        DegreeCourse.objects.create(degree=degree1, course=course2, is_core=False)
        # Add degree courses for other degrees and courses if needed

        # CourseObjectives
        CourseObjective.objects.create(course=course1, objective=objective1)
        CourseObjective.objects.create(course=course2, objective=objective2)
        # Add course objectives for other courses if needed

        self.stdout.write(self.style.SUCCESS('Database has been populated with sample data.'))
