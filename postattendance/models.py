from django.db import models
from django.db.models import Deferrable, UniqueConstraint
from kiwisolver import Constraint

# Create your models here.
class Student_attendance_report(models.Model):
    Enrollment_no = models.PositiveBigIntegerField() #(primary_key=True)
    Lec_tt_id=models.IntegerField()
    date=models.DateField()
    status=models.BooleanField() #Boolean: False --> Absent  and    True --> present
    class Meta:  #using unique together 
        unique_together=(('Enrollment_no','Lec_tt_id' ,'date' ),) 
    # class Meta: #using uniqueConstraints
    #     # db_table='student_attendance_report'
    #     Constraints = [
    #         models.UniqueConstraint(fields=['Enrollment_no','Lec_tt_id' ,'date' , ] , name='Enroll_Lec_tt_id_Date')
    #     ]
    

class Lecture_time_slot(models.Model):
    slot_id_name=models.CharField(max_length=255,primary_key=True)
    slot_time=models.PositiveSmallIntegerField()  #1 for 10:30-11:30   #2 for 11:30-12:30

class Lecture_time_table(models.Model):
    Lec_tt_id=models.IntegerField(primary_key=True)
    Faculty_id=models.IntegerField()  #from faculty details 
    Subject_code=models.PositiveSmallIntegerField() #from subject deatils table
    Semester=models.PositiveSmallIntegerField() #from term details
    Division=models.CharField(max_length=255) #==> decide by the faculty acc. to there timetable
    Day=models.CharField(max_length=255) #==> decide by the faculty acc. to there timetable
    slot_id_name=models.CharField(max_length=255)  #from lecture time slot table 

    # class Meta:  #using unique together 
    #     unique_together=('Lec_tt_id','Day',)
    
    # class Meta: #using uniqueConstraints
    #     Constraints = [
    #         models.UniqueConstraint(fields=['Lec_tt_id' , 'Day' , ] , name='Lec_tt_id_Day')
    #     ]


# class Faculty_details(models.Model):
#     Faculty_id=models.IntegerField()
#     Faculty_name=models.CharField()
#     Faculty_emailid=models.EmailField()
#     Faculty_department=models.CharField()
#     Faculty_password=models.IntegerField()

# class Student_details(models.Model):
#     Enrollment_no = models.PositiveBigIntegerField()

