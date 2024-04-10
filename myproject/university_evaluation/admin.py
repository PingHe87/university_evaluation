from django.contrib import admin

# Register your models here.

from .models import Degree, Course, Instructor, Section, LearningObjective

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_number', 'name')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'year', 'semester', 'instructor')

class LearningObjectiveAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Degree, DegreeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(LearningObjective, LearningObjectiveAdmin)

