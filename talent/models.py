# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinValueValidator

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=45, blank=True, null=True)
    admin_email = models.CharField(max_length=50)
    password = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Advertisement(models.Model):
    ad_id = models.AutoField(primary_key=True)
    ad_name = models.CharField(max_length=25, blank=True, null=True)
    ad_desc = models.CharField(max_length=100, blank=True, null=True)
    ad_date = models.DateField(blank=True, null=True)
    ad_image = models.CharField(max_length=45, blank=True, null=True)
    company_link = models.CharField(max_length=45, blank=True, null=True)
    admin_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Admin_admin_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertisement'


class Audition(models.Model):
    audition_id = models.AutoField(primary_key=True)
    audition_type = models.CharField(max_length=25, blank=True, null=True)
    cand_fname = models.CharField(max_length=10, blank=True, null=True)
    cand_height = models.CharField(max_length=25)
    cand_weight = models.CharField(max_length=25)
    cand_qual = models.CharField(max_length=45)
    mediafile = models.CharField(max_length=45)
    student_stu_id = models.IntegerField(db_column='Student_stu_id', blank=True, null=True)  # Field name made lowercase.
    cust = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audition'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_desc = models.CharField(max_length=100, blank=True, null=True)
    com_date = models.DateField(blank=True, null=True)
    student_stu = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_stu_id', blank=True, null=True)  # Field name made lowercase.
    customer_cust = models.ForeignKey('Customer', models.DO_NOTHING, db_column='Customer_cust_id', blank=True, null=True)  # Field name made lowercase.
    community_post_post = models.ForeignKey('CommunityPost', models.DO_NOTHING, db_column='Community_post_post_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class CommunityPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_date = models.DateTimeField(blank=True, null=True)
    post_img = models.ImageField(upload_to='POST_IMAGE/', default='')
    post_cap = models.CharField(max_length=100, blank=True, null=True)
    
    cust = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_post'


class Profile(models.Model):
    pf_id = models.AutoField(primary_key=True)
    pf_username = models.CharField(max_length=45, blank=True, null=True)
    pf_bio = models.CharField(max_length=150, blank=True, null=True)
    pf_image = models.ImageField(upload_to='PROFILE_IMAGE/', default='')
    cust = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=45, blank=True, null=True)
    course_cap = models.CharField(max_length=45,blank=True,null=True)
    course_desc = models.CharField(max_length=200, blank=True, null=True)
    course_aval_seat = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    course_image = models.ImageField(upload_to='COURSE_IMAGE/', default='')

    class Meta:
        managed = False
        db_table = 'course'


class CourseDuration(models.Model):
    duration_id = models.AutoField(primary_key=True)
    course_duration = models.CharField(max_length=25, blank=True, null=True)
    course_fees = models.FloatField(blank=True, null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="display",blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_duration'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_firstname = models.CharField(max_length=10, blank=True, null=True)
    cust_lastname = models.CharField(max_length=10, blank=True, null=True)
    cust_email = models.CharField(max_length=45, blank=True, null=True)
    cust_password = models.CharField(max_length=10, blank=True, null=True)
    cust_gender = models.CharField(max_length=6, blank=True, null=True)
    # cust_address = models.CharField(max_length=100, blank=True, null=True)
    # cust_dob = models.DateField(blank=True, null=True)
    # cust_mobile = models.BigIntegerField(blank=True, null=True)
   

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Enrolled(models.Model):
    en_id = models.AutoField(primary_key=True)
    en_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    course = models.ForeignKey(Course, models.DO_NOTHING)
    duration = models.ForeignKey(CourseDuration, models.DO_NOTHING)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enrolled'


class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=100, blank=True, null=True)
    f_date = models.DateField(blank=True, null=True)
    student_stu = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_stu_id', blank=True, null=True)  # Field name made lowercase.
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_cust_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_method = models.CharField(max_length=25, blank=True, null=True)
    pay_amount = models.FloatField(blank=True, null=True)
    pay_date = models.DateField(blank=True, null=True)
    enrolled_en = models.ForeignKey(Enrolled, models.DO_NOTHING, db_column='Enrolled_en_id', blank=True, null=True)  # Field name made lowercase.
    service_booking_book = models.ForeignKey('ServiceBooking', models.DO_NOTHING, db_column='Service_booking_book_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=45, blank=True, null=True)
    service_desc = models.CharField(max_length=100, blank=True, null=True)
    no_of_days = models.PositiveIntegerField(default=1)
    per_day_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceBooking(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_date = models.DateTimeField(blank=True, null=True)
    c_address = models.CharField(max_length=100)
    c_mobile = models.BigIntegerField()
    c_dob = models.DateField()
    book_price = models.FloatField()
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    service = models.ForeignKey(Service, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_booking'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_firstname = models.CharField(max_length=10, blank=True, null=True)
    staff_lastname = models.CharField(max_length=10, blank=True, null=True)
    staff_password = models.CharField(max_length=8, blank=True, null=True)
    staff_address = models.CharField(max_length=100, blank=True, null=True)
    staff_email = models.CharField(max_length=45, blank=True, null=True)
    staff_mobile = models.BigIntegerField(blank=True, null=True)
    staff_joining_date = models.DateField(blank=True, null=True)
    staff_work_duration = models.CharField(max_length=25, blank=True, null=True)
    staff_leave = models.IntegerField(blank=True, null=True)
    staff_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_firstname = models.CharField(max_length=10, blank=True, null=True)
    stu_lastname = models.CharField(max_length=10, blank=True, null=True)
    stu_password = models.CharField(max_length=8, blank=True, null=True)
    stu_address = models.CharField(max_length=100, blank=True, null=True)
    stu_gender = models.CharField(max_length=6, blank=True, null=True)
    stu_dob = models.DateField(blank=True, null=True)
    stu_mobile = models.BigIntegerField(blank=True, null=True)
    stu_email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentPortfolio(models.Model):
    pf_id = models.AutoField(primary_key=True)
    stu_exp = models.CharField(max_length=45, blank=True, null=True)
    stu_socialac = models.CharField(db_column='stu_socialAC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    stu_objective = models.CharField(max_length=25, blank=True, null=True)
    stu_skill = models.CharField(max_length=25, blank=True, null=True)
    stu_image = models.CharField(max_length=45, blank=True, null=True)
    student_stu = models.ForeignKey(Student, models.DO_NOTHING, db_column='Student_stu_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_portfolio'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_password = models.CharField(max_length=8, blank=True, null=True)
    user_type = models.CharField(max_length=10, blank=True, null=True)
    admin_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Admin_admin_id', blank=True, null=True)  # Field name made lowercase.
    staff_staff = models.ForeignKey(Staff, models.DO_NOTHING, db_column='Staff_staff_id', blank=True, null=True)  # Field name made lowercase.
    student_stu = models.ForeignKey(Student, models.DO_NOTHING, db_column='Student_stu_id', blank=True, null=True)  # Field name made lowercase.
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_cust_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


