from django import forms
from .models import Course, CourseDuration

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_aval_seat', 'course_image']

class CourseDurationForm(forms.ModelForm):
    class Meta:
        model = CourseDuration
        fields = ['course_duration', 'course_fees']
