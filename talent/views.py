
from datetime import datetime
from django.db import connection

from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


from django.contrib.auth import logout

from django.http import JsonResponse

from portfolio.models import Profile

from talent.models import *
#to import serialize

#from django.core.serializers import serialize

# Create your views here.



def loginpage(request):
    return render(request,'webpages/login.html')

def signin(request):
    # user = Customer.objects.all()

    if request.method=='POST':
        email=request.POST['email']
        pass1=request.POST['pass']

        if Customer.objects.filter(cust_email=email).exists():

            if Customer.objects.filter(cust_password=pass1).exists():

                data = Customer.objects.get(cust_email=email)

                if data.cust_password == pass1 and data.cust_email == email:
                    request.session['cid']=data.cust_id
                    return redirect('webcourse')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('signin')
            else:
                messages.info(request,'Invalid Password')
                return redirect('signin')
        else:
            messages.info(request,'Invalid Email', extra_tags='info')
            # messages.success(request,'Success from login', extra_tags='success')
            return redirect('signin')
    else :
        return render(request,'webpages/login.html')

def signup(request):
    user = Customer.objects.all()
    if request.method=='POST':
        cust_firstname =request.POST['fname']
        cust_lastname=request.POST['lname']
        cust_email=request.POST['email']
        cust_password=request.POST['pass']
        cust_gender=request.POST['gender']
        # cust_address=request.POST['address']
        # cust_dob=request.POST['dob']
        # cust_mobile=request.POST['mobile']

        if Customer.objects.filter(cust_email=cust_email).exists():
            messages.info(request,'Email is already used')
            # messages.success(request,'Successfull', extra_tags='success')
            return redirect('signup')
        elif Customer.objects.filter(cust_password=cust_password).exists():
            messages.info(request,'Use another password')
            return redirect('signup')
        else:
            Customer(cust_firstname=cust_firstname,cust_lastname=cust_lastname, cust_email=cust_email, cust_password=cust_password, cust_gender=cust_gender).save()
            messages.success(request,request.POST['fname'] + ' is Registered Successfully', extra_tags='success')
            messages.success(request,'login to continue...')

            return render(request,'webpages/login.html')
    else:
        return render(request,'webpages/register.html')

def registerpage(request):
    return render(request,'webpages/register.html')


def logout_customer(request):
    logout(request)
    request.session.clear()
    request.session['cid'] = None

    return redirect('home')


#*************** admin side **************************
def logout_admin(request):
    logout(request)
    request.session.flush()
    request.session['adminnnn'] = None
    return redirect('/adminlogin/')


def adminlogin(request):
    if request.method=="POST":
        email=request.POST.get("email")
        pwd=request.POST.get("pass")

        if Admin.objects.filter(admin_email=email).exists() and Admin.objects.filter(admin_email=email).exists():
            admins=Admin.objects.filter(admin_email=email,password=pwd)
            i=0
            for ad in admins:
                i=i+1
                request.session['adminn']=ad.admin_email
                return redirect('/admin/')
        else:
            messages.info(request,'Invalid Credentials', extra_tags='info')
            return redirect('adminlogin')
    return render(request,"adlogin.html")



def admin_show(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    customer_count = Customer.objects.count()
    service_book_count=ServiceBooking.objects.count()
    course_booking=Course.objects.count()
    result1=Service.objects.all()
    book=ServiceBooking.objects.all()
    result=Admin.objects.all()
    return render(request,'admin.html',{'Admin':result,'Service':result1,'customer_count': customer_count,'ServiceBook':book,'bookcount':service_book_count,'coursecount':course_booking})


def dadmin(request):
    return render(request,'d-admin.html')


def pro(request):
    return render(request,'pro.html')



def index(request):
    try:
        c_id = request.session.get('cid')
        user = Customer.objects.get(cust_id=c_id)
        return render(request, "webpages/index.html", { 'c_id': c_id, 'user': user})
    except:
        return render(request,'webpages/index.html')

    




#*************** webcourse/services **************************
"""
def checkcourselogout(request):
    try:
        c_id = request.session.get('cid')
        user = Customer.objects.get(cust_id=c_id)
        return render(request, "webpages/webco.html", { 'c_id': c_id, 'user': user})
    except:
       return render(request,'webpages/webco.html')
"""
    

def showcourse(request):

    result=Course.objects.all()
    try:
        c_id = request.session.get('cid')
        user = Customer.objects.get(cust_id=c_id)
        return render(request, "webpages/webcourse.html", { 'c_id': c_id, 'user': user,'Course':result})
    except:
        return render(request,'webpages/webcourse.html')

    

    #return render(request,'webpages/webcourse.html',{'Course':result})

def showservice(request):

    result=Service.objects.all()
    try:
        c_id = request.session.get('cid')
        user = Customer.objects.get(cust_id=c_id)
        return render(request, "webpages/webservice.html", { 'c_id': c_id, 'user': user,'Service':result})
    
    except:
        return render(request,'webpages/webservice.html')

# ===============CommunityPost==========================

def showfeed(request):

    return render(request,'webpages/webfeed.html')

def showpost(request):

    result=CommunityPost.object.all()

    return render(request,'webpages/webfeed.html',{'CommunityPost':result})

def makepost(request):

    if request.method=="POST":
        post_media = request.FILES.get('post_media')
        post_cap = request.POST.get('post_cap')

        newpost=CommunityPost(post_media=post_media,post_cap=post_cap)
        newpost.save()

        return redirect('/')
    else:
        return redirect('/')

def showsetting(request):
    return render(request,'setting.html')



#**************** service *********************************

"""
def service_show(request):
    if request.session.has_key('adminnnn'):
        pass
    else:
        return redirect('/adminlogin/')
    result=Service.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st != None :
            result=Service.objects.filter(service_name__icontains=st)



    return render(request,'service.html',{'Service':result})
"""



def service_show(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    result = Service.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        if st is not None:
            result = Service.objects.filter(service_name__icontains=st)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If the request is an AJAX request, return JSON response
        data = serialize('json', result)
        return JsonResponse(data, safe=False)
    else:
        # If the request is a normal GET request, render HTML template
        return render(request, 'service.html', {'Service': result})








def serviceadd(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    if request.method=='POST':
        service_name=request.POST['service_name']
        service_desc=request.POST['service_desc']
        no_of_days=request.POST['no_of_days']
        per_day_cost=request.POST['per_day_cost']

        Service(service_name=service_name,service_desc=service_desc,no_of_days=no_of_days,per_day_cost=per_day_cost ).save()
        return redirect('services')
    else:
        return render(request,'addservice.html')

def editservice(request,service_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=Service.objects.get(service_id=service_id)
    return render(request,'upservice.html',{'Service':ff})

def serviceup(request,service_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
        ff=Service.objects.all()
    ff=Service.objects.get(service_id=service_id)
    ff.service_name=request.POST['service_name']
    ff.service_desc=request.POST['service_desc']
    ff.no_of_days=request.POST['no_of_days']
    ff.per_day_cost=request.POST['per_day_cost']
    ff.save()

    return redirect('serviceshow')

def delservice(request,service_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deleteservice=Service.objects.get(service_id=service_id)
    deleteservice.delete()
    ans=Service.objects.all()
    return render(request,'service.html',{'Service':ans})



#*************** audition **************************


def showservicebook(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    ff=ServiceBooking.objects.all()

    return render(request,'showservicebook.html',{'ServiceBooking':ff})




#*************** courses **************************


"""
def showcourses(request):

    f1=Course.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st != None :
            f1=Course.objects.filter(course_name__icontains=st)
    return render(request,'course.html',{'Course':f1})
"""



def showcourses(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    result = Course.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        if st is not None:
            result = Course.objects.filter(course_name__icontains=st)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If the request is an AJAX request, return JSON response
        data = serialize('json', result)
        return JsonResponse(data, safe=False)
    else:
        # If the request is a normal GET request, render HTML template
        return render(request, 'course.html', {'Course': result})








def coursedetail(request, course_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    
    dis=Course.objects.get(course_id=course_id)

    return render(request,'course_detail.html',{'display':dis})



def courseadd(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    if request.method == 'POST':
        # Get form data
        course_name = request.POST.get('course_name')
        course_cap = request.POST.get('course_cap')
        course_desc=request.POST.get('course_desc')
        course_aval_seat = request.POST.get('course_aval_seat')
        course_image = request.FILES.get('course_image')
        course_duration = request.POST.get('course_duration')
        course_fees = request.POST.get('course_fees')

        # Create new course
        course = Course(course_name=course_name,course_cap=course_cap,course_desc=course_desc, course_aval_seat=course_aval_seat, course_image=course_image)
        course.save()

        # Create new course duration
        duration_obj = CourseDuration(course_duration=course_duration, course_fees=course_fees, course=course)
        duration_obj.save()



        return redirect('courses')
    else:
        return render(request, 'courseadd.html')



def durationadd(request,course_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    

    dis=Course.objects.get(course_id=course_id)

    if request.method=='POST':
        course_duration=request.POST['course_duration']
        course_fees=request.POST['course_fees']

        CourseDuration(course_duration=course_duration,course_fees=course_fees,course_id=course_id).save()

        return render(request,'durationadd.html',{'display':dis})
    else :
        return render(request,'durationadd.html',{'display':dis})



def coursedel(request, course_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    dis=Course.objects.get(course_id=course_id)
    dis.delete()
    return showcourses(request)



def delcourseduration(request,duration_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    dis=CourseDuration.objects.get(duration_id=duration_id)
    dis.delete()


    return showcourses(request)


def editcourse(request,course_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=Course.objects.get(course_id=course_id)
    return render(request,'upcourse.html',{'Course':ff})


def courseup(request,course_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=Course.objects.get(course_id=course_id)
    if request.method == 'POST':

        if request.FILES.get('course_image') :

            if ff.course_image:
                ff.course_image.delete()

            ff.course_image = request.FILES['course_image']
            ff.save()
        else :


            ff.course_name=request.POST['course_name']
            ff.course_cap=request.POST['course_cap']
            ff.course_desc=request.POST['course_desc']
            ff.course_aval_seat=request.POST['course_aval_seat']

            ff.save()


    return redirect('courses')



def editcourseduration(request,duration_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=CourseDuration.objects.get(duration_id=duration_id)
    return render(request,'upduration.html',{'CourseDuration':ff})

def durationupdate(request,duration_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=CourseDuration.objects.all()
    ff=CourseDuration.objects.get(duration_id=duration_id)
    ff.course_duration=request.POST['course_duration']
    ff.course_fees=request.POST['course_fees']

    ff.save()

    return redirect('courses')




#*************************** BOOKING ************************************************



def book_course(request,course_id):

    ff=Course.objects.get(course_id=course_id)
    
    

    if request.method == 'POST':
        address = request.POST['address']
        mobile_no = request.POST['mobile']
        dob = request.POST['dob']
        course=request.POST['course_id']
        duration=request.POST['course_duration']

        course1=Course.objects.get(course_id=course)
        duration1=CourseDuration.objects.get(duration_id=duration)
        customer =  request.session['cid']
        
        en_date = datetime.now()
        d=int(duration)
        c=int(course)
        c2 = int(customer)

        obj=Enrolled.objects.filter(cust=c2,duration=d,course=c)
        if obj.exists():
            return redirect('webcourse')
        else:
            booking = Enrolled.objects.create(en_date=en_date ,cust_id=customer, address=address, mobile=mobile_no, dob=dob,course=course1,duration=duration1 )
            return render(request, 'webpages/index.html', {'booking': booking ,'en_date':en_date})
    list=CourseDuration.objects.all()
    return render(request,'coursebook.html',{'Course':ff,'display':list})


def bookingshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    

    f1=Enrolled.objects.all()
    
   
    return render(request,'showcoursebook.html',{'Enrolled':f1})


#*************** staff **************************

"""
def staffshow(request):

    f1=Staff.objects.all()
   
    return render(request,'staff.html',{'Staff':f1})
"""



def staffshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    result = Staff.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        if st is not None:
            result = Staff.objects.filter(staff_firstname__icontains=st)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If the request is an AJAX request, return JSON response
        data = serialize('json', result)
        return JsonResponse(data, safe=False)
    else:
        # If the request is a normal GET request, render HTML template
        return render(request, 'staff.html', {'Staff': result})




def staffadd(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    if request.method=='POST':
        staff_firstname=request.POST['staff_firstname']
        staff_lastname=request.POST['staff_lastname']
        staff_password=request.POST['staff_password']
        staff_address=request.POST['staff_address']
        staff_email =request.POST['staff_email']
        staff_mobile =request.POST['staff_mobile']
        staff_joining_date=request.POST['staff_joining_date']
        staff_work_duration=request.POST['staff_work_duration']
        staff_leave=request.POST['staff_leave']
        staff_salary=request.POST['staff_salary']
        Staff(staff_firstname=staff_firstname,staff_lastname=staff_lastname, staff_password= staff_password, staff_address= staff_address,staff_email =staff_email,staff_mobile=staff_mobile, staff_joining_date= staff_joining_date,staff_work_duration=staff_work_duration,staff_leave=staff_leave, staff_salary= staff_salary ).save()
        return redirect('/staff/')
    else:
        return render(request,'addstaff.html')

def editstaff(request,staff_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=Staff.objects.get(staff_id=staff_id)
    return render(request,'upstaff.html',{'Staff':ff})

def staffup(request,staff_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    ff=Staff.objects.all()
    ff=Staff.objects.get(staff_id=staff_id)
    ff.staff_firstname=request.POST['staff_firstname']
    ff.staff_lastname=request.POST['staff_lastname']
    ff.staff_password=request.POST['staff_password']
    ff.staff_address=request.POST['staff_address']
    ff.staff_email =request.POST['staff_email']
    ff.staff_mobile =request.POST['staff_mobile']
    ff.staff_joining_date=request.POST['staff_joining_date']
    ff.staff_work_duration=request.POST['staff_work_duration']
    ff.staff_leave=request.POST['staff_leave']
    ff.staff_salary=request.POST['staff_salary']
    ff.save()

    return redirect('staff')

def delstaff(request,staff_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletestaff=Staff.objects.get(staff_id=staff_id)
    deletestaff.delete()
    ans=Staff.objects.all()
    return render(request,'staff.html',{'Staff':ans})



#*************** student **************************



def studentshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    result=Student.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st != None :
            result=Student.objects.filter(stu_firstname__icontains=st)

    return render(request,'student.html',{'Student':result})



def stuadd(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    if request.method=='POST':
        stu_firstname =request.POST['stu_firstname']
        stu_lastname=request.POST['stu_lastname']
        stu_password=request.POST['stu_password']
        stu_address=request.POST['stu_address']
        stu_gender=request.POST['stu_gender']
        stu_dob=request.POST['stu_dob']
        stu_mobile=request.POST['stu_mobile']
        stu_email=request.POST['stu_email']
        Student(stu_firstname=stu_firstname,stu_lastname=stu_lastname, stu_password= stu_password, stu_address= stu_address,stu_gender=stu_gender,stu_dob=stu_dob,stu_email =stu_email,stu_mobile=stu_mobile).save()
        return redirect('/student/')
    else:
        return render(request,'addstudent.html')


def editstudent(request,stu_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    studentedit=Student.objects.get(stu_id=stu_id)
    return render(request,'upstudent.html' ,{'Student':studentedit})


def studentupdate(request,stu_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    ff=Student.objects.all()
    ff=Student.objects.get(stu_id=stu_id)
    ff.stu_firstname =request.POST['stu_firstname']
    ff.stu_lastname=request.POST['stu_lastname']
    ff.stu_password=request.POST['stu_password']
    ff.stu_address=request.POST['stu_address']
    ff.stu_gender=request.POST['stu_gender']
    ff.stu_dob=request.POST['stu_dob']
    ff.stu_mobile=request.POST['stu_mobile']
    ff.stu_email=request.POST['stu_email']
    ff.save()

    return redirect('student')


def delstudent(request,stu_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletestudent=Student.objects.get(stu_id=stu_id)
    deletestudent.delete()
    ans=Student.objects.all()
    return render(request,'student.html',{'Student':ans})




#*************** custome **************************

"""
def customer_show(request):
    result=Customer.objects.all()
    if request.method=="GET":
        st=request.GET.get('search')
        if st != None :
            result=Customer.objects.filter(cust_firstname__icontains=st)

    return render(request,'customer.html',{'Customer':result})

"""



def customer_show(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    result = Customer.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        if st is not None:
            result = Customer.objects.filter(cust_firstname__icontains=st)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If the request is an AJAX request, return JSON response
        data = serialize('json', result)
        return JsonResponse(data, safe=False)
    else:
        # If the request is a normal GET request, render HTML template
        return render(request, 'customer.html', {'Customer': result})





""" blank code for search.... """

"""
def customer_show(request):
    result = Customer.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        if st is not None:
            result = Customer.objects.filter(cust_firstname__icontains=st)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If the request is an AJAX request, return JSON response
        data = [model_to_dict(customer) for customer in result]
        return JsonResponse(data, safe=False)
    else:
        # If the request is a normal GET request, render HTML template
        return render(request, 'customer.html', {'Customer': result})

"""

def editcustomer(request,cust_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    ff=Customer.objects.get(cust_id=cust_id)
    return render(request,'upcustomer.html',{'Customer':ff})

def customerupdate(request,cust_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    ff=Customer.objects.all()
    ff=Customer.objects.get(cust_id=cust_id)
    ff.cust_firstname=request.POST['cust_firstname']
    ff.cust_lastname=request.POST['cust_lastname']
    ff.cust_password=request.POST['cust_password']
    
    ff.cust_gender=request.POST['cust_gender']
  
    ff.cust_email=request.POST['cust_email']
    ff.save()

    return redirect('customer')

def delcustomer(request,cust_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletestudent=Customer.objects.get(cust_id=cust_id)
    deletestudent.delete()
    ans=Customer.objects.all()
    return render(request,'customer.html',{'Customer':ans})









def editaudition(request,audition_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    auditionedit=Audition.objects.get(audition_id=audition_id)
    return render(request,'upaudition.html' ,{'Audition':auditionedit})


def auditionupdate(request,audition_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    ff=Audition.objects.all()
    ff=Audition.objects.get(audition_id=audition_id)
    ff.audition_type=request.POST['audition_type']
    ff.cand_fname=request.POST['cand_fname']
    ff.cand_height=request.POST['cand_height']
    ff.cand_weight=request.POST['cand_weight']
    ff.cand_qual=request.POST['cand_qual']
    ff.mediafile=request.POST['mediafile']
    
    ff.save()

    return redirect('audition')


def deleteaudition(request,audition_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletestudent=Audition.objects.get(audition_id=audition_id)
    deletestudent.delete()
    ans=Audition.objects.all()
    return render(request,'audition.html',{'Audition':ans})




def bookservice(request,service_id):

    ff=Service.objects.get(service_id=service_id)
     
    if request.method == 'POST':
        # Retrieve data from form
        address = request.POST['c_address']
        mobile = request.POST['c_mobile']
        dob = request.POST['c_dob']
        
        service = request.POST['service_id']
        no_of_days =(request.POST['no_of_days'])
   
        
            
        customer =  request.session['cid']
        
        # Fetching per day cost from service table based on I'd
        service1 = Service.objects.get(service_id=service)
        
        per_day_cost = service1.per_day_cost
        
        # Calculating total cost 
        total_cost = int(no_of_days) * per_day_cost
        
        book_date = datetime.now()


        booking = ServiceBooking.objects.create(book_date=book_date ,cust_id=customer, c_address=address, c_mobile=mobile, c_dob=dob,service=service1,book_price=total_cost ).save()
        return render(request, 'webpages/index.html', {'booking': booking ,'book_date':book_date,'total_cost': total_cost})
    
    return render(request,'servicebook.html',{'Service':ff})



def upload(request):

    if request.method == 'POST':
        
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        date=datetime.now()
        cust=request.session['cid']

        post = CommunityPost.objects.create(post_date=date,post_img=image,post_cap=caption,cust_id=cust)
        post.save()


        return render(request,'webpages/index.html')
    else:
        return redirect('/')

def showpost(request):

    ff=CommunityPost.objects.all()
    gg=Profile.objects.all()

    return render(request,'student.html',{'CommunityPost':ff,'Profile':gg})

def showfeed(request):
    ff=CommunityPost.objects.all()

    return render(request,'webpages/webfeed.html',{'CommunityPost':ff})



def deletepost(request,post_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletepost=CommunityPost.objects.get(post_id=post_id)
    deletepost.delete()
    ans=CommunityPost.objects.all()
    return render(request,'student.html',{'CommunityPost':ans})


#**********profiles *******************

def showsetting(request):
    
    return render(request,'webpages/setting.html')

def showprofile(request):
    ff=Profile.objects.all()

    return render(request,'webpages/profile.html',{'Profile':ff})

def makeprofile(request):

    if request.method == 'POST':
        username = request.POST['uname']
        bio = request.POST['bio']
        image = request.FILES.get('pfimg')

        cust1=request.session['cid']
       
        profile = Profile(pf_username=username,pf_bio=bio,pf_image=image,cust_id=cust1)
        profile.save()

        return render(request,'webpages/index.html')
    else:
        return redirect('/')
   


def deletecoursebook(request,en_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletestaff=Enrolled.objects.get(en_id=en_id)
    deletestaff.delete()
    ans=Enrolled.objects.all()
    return render(request,'showcoursebook.html',{'Enrolled':ans})


def deleteservicebook(request,book_id):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('/adminlogin/')
    
    deletebooking=ServiceBooking.objects.get(book_id=book_id)
    deletebooking.delete()
    ans=ServiceBooking.objects.all()
    return render(request,'showcoursebook.html',{'ServiceBooking':ans})
