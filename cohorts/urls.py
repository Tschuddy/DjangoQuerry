# from django.urls import path
# from . import views


# urlpatterns = [
    
#     path('', views.homepage, name='homepage'),
#     path('homeview', views.homepage, name='homeview')
    
   

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homeview'),
    path('add_student/', views.add_student, name='add_student'),
]
