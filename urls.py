from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('student.views',
    url(r'^home/',views.home, name = 'home'),
    url(r'^login/',views.login, name = 'login'),
    url(r'^stud/', views.stud, name = 'stud'),
    
    #url(r'^stud/display/', views.display, name= 'display'),
    
)


 
