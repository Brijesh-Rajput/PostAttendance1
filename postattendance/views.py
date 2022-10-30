from django.shortcuts import render,redirect

# Create your views here.
from .models import Student_attendance_report,Lecture_time_slot,Lecture_time_table

def index(request):
    return render(request,"postattendance.html")

def attendance(request):
      if request.method=='POST':
        s1=Student_attendance_report.objects.all()
        s1.delete()
        vEnrollment=request.POST.getlist('Enrollment')
        vdate=request.POST['date']
        # vsemester=request.POST['semester']  #using these all below variables we have to find the Lec_tt_id 
        # vsubject=request.POST['subject']
        # vcomponent=request.POST['component']   #consider that component is equals to Theory
        # vdivision=request.POST['division']  #required to fetch the student of that division only 
        # vbatch=request.POST['batch']
        # vtime=request.POST['time'] 

        # Lecture=Lecture_time_table.objects.filter(Faculty_id=facultyid,Subject_code=subjectcode,Semester=vsemester,Division=vdivision,Day=vday,slot_id_name=slotid)  #Here, we have to find out day's from date 
        for l in vEnrollment:
            print(l)
        for l in vEnrollment:
            us=Student_attendance_report(Enrollment_no=l,date=vdate,status=True,Lec_tt_id=12345)#Lecture.Lectureid) #lec_tt_id will be also same for all students. But How to find the Lec_tt_id ?
            us.save(request)
            print("user is created Successfull") #this will be shown in terminal
      return redirect('/')  #NOT ''


