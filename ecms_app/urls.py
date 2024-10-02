from django.urls import path
from .views import home_view , add_student, edit_student, delete_student, search_student, show_profile, create_profile, edit_profile

urlpatterns = [
    path('home/', home_view, name='home'),
    path('add/', add_student, name='add_student'),
    path('edit/<student_id>/', edit_student, name='edit_student'),
    path('delete/<student_id>/', delete_student, name='delete_student'),
    path('search/', search_student, name='search_student'),
    path('profile/<int:user_id>/', show_profile, name='profile'),
    path('profiles/new', create_profile, name='add_profile'),
    path('profile/edit/<profile_id>', edit_profile, name='edit_profile'),
]
