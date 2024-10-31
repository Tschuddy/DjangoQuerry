# from django.shortcuts import render,redirect
# from .models import Student # Replace with actual model names if different

# def homepage(request):
#     # Fetch all student data to pass to the template
#     students = Student.objects.all()
    
#     # Render the template with the context
#     return render(request, 'index.html', {'homepage': students})

# def homepage(request):
#     return render(request, "index.html")

# def homepage(request):
#     if request.method == 'POST':
#         profile_picture = request.POST['profile_picture']
#         full_name = request.POST['full_name']
#         cohort = request.POST['cohort']
#         program = request.POST['program']
#         status = request.POST['status']
#         date_join = request.POST['date_join']
#         rating = request.POST['rating']
        
#     new_students = Student(
#         profile_picture = profile_picture,
#         full_name = full_name,
#         cohort = cohort,
#         program = program,
#         status = status,
#         date_join = date_join,
#         rating = rating
#     )
    
#     new_students.save()
#     return redirect('home')


from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student, Cohort, Program

def home_view(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        profile_image = request.POST.get('profileImage')
        full_name = request.POST.get('fullName').split()
        first_name, last_name = full_name[0], " ".join(full_name[1:]) if len(full_name) > 1 else ''
        cohort_name = request.POST.get('cohort')
        program_name = request.POST.get('program')
        status = request.POST.get('status')
        date_joined = request.POST.get('dateJoined')
        rating = request.POST.get('rating')
        student_type = 'member'  # Set based on your requirements

        cohort, _ = Cohort.objects.get_or_create(name=cohort_name)
        program, _ = Program.objects.get_or_create(name=program_name)

        Student.objects.create(
            profile_image=profile_image,
            first_name=first_name,
            last_name=last_name,
            cohort_name=cohort,
            program_name=program,
            status=status,
            date_joined=date_joined,
            rating=rating,
            student_type=student_type
        )
        return redirect(reverse('homeview'))

    return render(request, 'index.html')
