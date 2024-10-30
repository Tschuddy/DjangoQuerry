from django.db import models

# Create your models here.


student_types = [
    ('leader', 'cohort leader'),
     ('deputy', 'vice leader'),
    ('secretary', 'secretary'),
    ('President', 'President'),
     ('member', 'member'),

]



class Student(models.Model):
    profile_picture = models.ImageField(upload_to='student_profile', null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    status = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    student_type = models.CharField(max_length=100, choices=student_types, default='member')
    date_join = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_join']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    




class Student_Profile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    bio = models.TextField()
    date_of_birth =models.DateField()
    address = models.CharField(max_length=300)
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to='student_profile')
    date_join = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.username}"
    
    
    



class Program(models.Model):
    courses = models.CharField(max_length=500)
    grade = models.IntegerField(default=0.0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.courses}"

    

   
    



class CohortGroup(models.Model):
    name = models.CharField(max_length=200)
    date_join = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return f"{self.name}"





