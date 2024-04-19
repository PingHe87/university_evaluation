from django.urls import path # type: ignore
from .views import course_list,create_degree, degree_details,home, instructor_sections, query_sections  # 确保导入了home视图

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('', home, name='home'),  # 添加这一行
    # path('courses/add/', add_course, name='add_course'),
    path('create_degree/', create_degree, name='create_degree'),
    path('query/', query_sections, name='query'),
    path('sections_result/', query_sections, name='sections_result'),
	path('instructor_sections/', instructor_sections, name='instructor_sections'),
	 path('instructor_sections_result/', instructor_sections, name='instructor_sections_result'),
	 path('degree_details/', degree_details, name='degree_details'),
    path('degree_details_result/', degree_details, name='degree_details_result'),
]
