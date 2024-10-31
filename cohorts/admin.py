# from django.contrib import admin
# from .models import Student,Program,Student_Profile,CohortGroup

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['profile_picture', 'first_name','last_name','status','student_type','date_join']
    
#     def profile_picture(self, obj):
#         if object.profile_picture:
#             return format.html('<img src= "{}" width = "50" height="50" style="border-radius: 50%">')




# @admin.register(Student_Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['student','date_of_birth', 'rating','date_join','address']


# @admin.register(Program)
# class ProgramAdmin(admin.ModelAdmin) :
#     list_display = ['courses','grade','student']


# @admin.register(CohortGroup)
# class CohortAdmin(admin.ModelAdmin) :
#     list_display = ['name', 'date_join']










from django.contrib import admin
from .models import Student, Cohort, Program

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'first_name', 'last_name', 'cohort_name', 'program_name', 'status', 'date_joined', 'rating', 'student_type')

admin.site.register(Cohort)
admin.site.register(Program)
