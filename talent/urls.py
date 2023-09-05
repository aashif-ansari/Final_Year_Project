"""talent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('',views.index , name='home'),

    #path('webco/',views.checkcourselogout),
    path('webcourse/',views.showcourse,name="webcourse"),
    path('webservice/',views.showservice),

    path('prt/',include('portfolio.urls')),
    path('setting',views.showsetting),
    # path('upload/', views.upload, name='upload'),

    #path('profile/',views.pro, name='profile'),
    path('',include('portfolio.urls')),

    path('makepost/',views.upload,name='makepost'),

    path('showfeed/',views.showfeed , name="showfeed"),
    

    #************** staff  *******************************
    
    path('staff/',views.staffshow, name='staff'),
    path('addstaff/',views.staffadd , name="addstaff"),
    path('editstaff/<int:staff_id>',views.editstaff, name='editstaff'),
    path('staffupdate/<int:staff_id>',views.staffup, name='staffupdate'),
    path('delstaff/<int:staff_id>',views.delstaff, name='delstaff'),

     
    #************** student *******************************
   

   # path('student/',views.studentshow,name='student'),
    path('postdetail/',views.showpost, name="postdetail"),
   
    path('addstudent/',views.stuadd, name="addstudent"),
    path('editstudent/<int:stu_id>',views.editstudent,name='editstudent'),
    path('updatestu/<int:stu_id>',views.studentupdate, name='updatestu'),
    path('delstudent/<int:stu_id>',views.delstudent, name='delstudent'),
    
  
    # =====================Community Post========================

    # path('feedposts/',views.feedpost),
    path('webfeed/',views.showfeed),
    path('makepost/',views.makepost),   

    path('deletepost/<int:post_id>',views.deletepost , name='deletepost'),


    path('makeprofile/',views.makeprofile,name='makeprofile'),
    path('settings/',views.showsetting ,name="settings"),
    path('profile/',views.showprofile, name='profile'),

 
    #************** customer  *******************************
   

    
    path('editcust/<int:cust_id>', views.editcustomer , name='edit'),
    path('update_cust/<int:cust_id>', views.customerupdate , name='update_cust'),
    path('delcustomer/<int:cust_id>',views.delcustomer , name='delcustomer'),
    path('customer/',views.customer_show, name='customer'),
   
   

 
    #************** login/signup *******************************
   
    
    path('signup/',views.signup, name='signup'),
    path('signin/', views.signin ,name='signin'),
    path('register/',views.registerpage, name='register'),
    path('login/',views.loginpage, name='login'),

    path('logoutcust/',views.logout_customer , name='logoutcust'),
   
    path('logoutadmin/',views.logout_admin , name='logoutadmin'),
   
 
    #************** Admin  *******************************
   
    
    path('admin/',views.admin_show,name='admin'),
    path('adminlogin/',views.adminlogin , name='adminlogin'),
    path('admindjango/',admin.site.urls),
    path('dadmin/',views.dadmin,name='dadmin'),

 
    #************** courses  *******************************
   

    path('courses/',views.showcourses, name='courses'),
    path('course_detail/<int:course_id>',views.coursedetail, name='display'),
    path('course_add/', views.courseadd, name='courseadd'),
    path('durationadd/<int:course_id>',views.durationadd, name="durationadd"),
    path('delcourse/<int:course_id>',views.coursedel , name='delcourse'),
    path('delcourseduration/<int:duration_id>',views.delcourseduration , name='delcourseduration'),
    path('editcourse/<int:course_id>',views.editcourse, name='editcourse'),
    path('courseupdate/<int:course_id>',views.courseup, name='courseupdate'),
    path('editduration/<int:duration_id>',views.editcourseduration, name='editduration'),
    path('durationupdate/<int:duration_id>',views.durationupdate, name='durationupdate'),
   
    #*************** book *************************************************

    path('book/<int:course_id>',views.book_course , name="book"),
    path('bookingshow/',views.bookingshow, name='bookingshow'),
   

    path('bookservice/<int:service_id>',views.bookservice , name="bookservice"),

    path('deletecoursebook/<int:en_id>',views.deletecoursebook , name="deletecoursebook"),

    path('bookingshow/<int:book_id>',views.deleteservicebook , name="bookingshow"),

    #************** services  *******************************
   

    path('services/',views.service_show, name='services'),
    path('addservice/',views.serviceadd , name="addservice"),
    path('editservice/<int:service_id>',views.editservice, name='editservice'),
    path('serviceshow/',views.service_show , name='serviceshow'),
    path('serviceupdate/<int:service_id>',views.serviceup, name='serviceupdate'),
    path('delservice/<int:service_id>',views.delservice , name='delservice'),

   
    #************** audition  *******************************
   
   
     path('showservicebook/',views.showservicebook,  name='showservicebook'),
     path('editaudition/<int:audition_id>',views.editaudition, name='editaudition'),
     path('auditionupdate/<int:audition_id>',views.auditionupdate, name='auditionupdate'),
     path('deleteaudition/<int:audition_id>',views.deleteaudition , name='deleteaudition'),


    
    
   

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
