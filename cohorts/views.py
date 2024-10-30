from django.shortcuts import render,redirect
from .models import Student # Replace with actual model names if different

def homeview(request):
    # Fetch all student data to pass to the template
    students = Student.objects.all()
    
    # Render the template with the context
    return render(request, 'index.html', {'homeview': students})

def homepage(request):
    return render(request, "index.html")

def homeview(request):
    if request.method == 'POST':
        profile_picture = request.POST['profileImage']
        full_name = request.POST['fullName']
        cohort = request.POST['cohort']
        program = request.POST['program']
        status = request.POST['status']
        date_join = request.POST['dateJoined']
        rating = request.POST['rating']
        
    new_students = Student(
        profile_picture = profileImage,
        full_name = fullName,
        cohort = cohort,
        program = program,
        status = status,
        date_join = dateJoined,
        rating = rating
    )
    
    new_student.save()
    return redirect('home')
