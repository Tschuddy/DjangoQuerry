from django.urls import path
# from .home import HomepageView
from . import views


urlpatterns = [
    # path('', HompageView.as_view(), name='homeview')
    path('', views.homepage, name='homepage'),
    # path('homeview', HomepageView.as_view(), name='homeview')
    path('homeview', views.homepage, name='homeview')
    
   

]
