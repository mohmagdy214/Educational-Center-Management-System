from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, TeacherProfile, Material
from .forms import StudentForm, TeacherProfileForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home_view(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})



@login_required(login_url='/login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.teacher = request.user
            myform.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form':form})



@login_required(login_url='/login')
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'student': student, 'form':form})



@login_required(login_url='/login')
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')



@login_required(login_url='/login')
def search_student(request):
    student_search = request.GET.get('student_search')
    students = Student.objects.filter(name__icontains=student_search)
    return render(request, 'home.html', {'students': students})



@login_required(login_url='/login')
def show_profile(request, user_id):
    profile = get_object_or_404(TeacherProfile, teacher_id=user_id) # before this there was not teacher_id got passed so the id gets only 404 not found
    return render(request, 'teacher_profile.html', {'profile': profile})



@login_required(login_url='/login')
def create_profile(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.teacher = request.user
            my_form.save()
            return redirect('/posts/news')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = TeacherProfileForm()
    return render(request, 'create_profile.html', {'form': form})



@login_required(login_url='/login')
def edit_profile(request, profile_id):
    profile = get_object_or_404(TeacherProfile, id=profile_id)
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/ecms/profile/{profile_id}')
    else:
        form = TeacherProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'profile': profile, 'form': form})
