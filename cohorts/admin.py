from django.contrib import admin
from .models import Student,Program,Student_Profile,CohortGroup

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['profile_picture', 'username', 'first_name','last_name','status','student_type','date_join']
    
    def profile_picture(self, obj):
        if obj.profile_picture:
            return format.html('<img src= "{}" width = "50" height="50" style="border-radius: 50%">')




@admin.register(Student_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student','date_of_birth', 'rating','date_join','address']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin) :
    list_display = ['courses','grade','student']


@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin) :
    list_display = ['name', 'date_join']



# Register your models here.
# admin.site.register(Student)
# admin.site.register(Program)
# admin.site.register(Student_Profile)
# admin.site.register(CohortGroup)






