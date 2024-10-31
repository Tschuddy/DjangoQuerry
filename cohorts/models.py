# from django.db import models

# # Create your models here.


# student_types = [
#     ('leader', 'cohort leader'),
#      ('deputy', 'vice leader'),
#     ('secretary', 'secretary'),
#     ('President', 'President'),
#      ('member', 'member'),

# ]



# class Student(models.Model):
#     profile_picture = models.ImageField(upload_to='student_profile', null=True, blank=True)
#     # username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, verbose_name='Last Name')
#     status = models.BooleanField(default=True)
#     rating = models.FloatField(default=0.0)
#     student_type = models.CharField(max_length=100, choices=student_types, default='member')
#     date_join = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date_join']

#     def __str__(self):
#         # return f"{self.first_name} {self.last_name} ({self.username})"
#         return f"{self.first_name} {self.last_name}"

    




# class Student_Profile(models.Model):
#     student = models.OneToOneField(Student,on_delete=models.CASCADE)
#     bio = models.TextField()
#     date_of_birth =models.DateField()
#     address = models.CharField(max_length=300)
#     rating = models.FloatField(default=0.0)
#     profile_picture = models.ImageField(upload_to='student_profile')
#     date_join = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.student.username}"
    
    
    



# class Program(models.Model):
#     courses = models.CharField(max_length=500)
#     grade = models.IntegerField(default=0.0)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.courses}"

    

   
    



# class CohortGroup(models.Model):
#     name = models.CharField(max_length=200)
#     date_join = models.DateTimeField(auto_now_add=True)
#     students = models.ManyToManyField(Student)
#     def __str__(self):
#         return f"{self.name}"



from django.db import models

class Cohort(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online Exam'),
        ('class', 'Class Exam'),
        ('missed', 'Missed Exam')
    ]
    
    STUDENT_TYPE_CHOICES = [
        ('member', 'Member'),
        ('non-member', 'Non-member')
    ]

    profile_image = models.URLField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cohort_name = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="students")
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="students")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_joined = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    student_type = models.CharField(max_length=10, choices=STUDENT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


