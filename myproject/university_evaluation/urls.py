from django.urls import path # type: ignore
from .views import course_list,create_degree,home  # 确保导入了home视图

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('', home, name='home'),  # 添加这一行
    # path('courses/add/', add_course, name='add_course'),
    path('create_degree/', create_degree, name='create_degree'),
    path('query/', query_sections, name='query'),
    path('sections_result/', query_sections, name='sections_result'),
]
