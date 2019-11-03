from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
import pymysql as p
import requests
import json
import random
#URL = 'http://www.way2sms.com/api/v1/sendCampaign'
otp = str(random.randint(999, 9999))

con = p.connect('localhost','root','root','csv_db')
c = con.cursor()

# Create your views here.
def index(request):
    """"" with con:
        if 'Register' in request.POST:
            License_number = request.POST['License_number']
            Plate_number = request.POST['Plate_number']
            First_Name = request.POST['First_Name']
            Last_Name = request.POST['Last_Name']
            Age = request.POST['Age']
            Contact_Number = request.POST['Contact_Number']
            Gender = request.POST['Gender']
"""
    return render(request,'index.html')
def Signup(request) :
    with con :
        if 'ronnie' in request.POST :
            print("Register Button Pressed")
            License_number = request.POST['License_number']
            Contact_Number = request.POST['Contact_Number']
            c.execute("select * from license_details")
            x = c.fetchall()
            print("License Number :  ", License_number, " Contact :  ",Contact_Number)
            ln= x[2][1]
            cn= x[2][6]
            print("LN : ", ln, " Cn: ", cn)
            if License_number == ln and Contact_Number == cn:
                print("The Value Entered is Correct")
                return redirect('Retrive')
            else:
                print("The Value Entered is not Correct")
                return render(request,'Signup.html', {'key': '1'})
    return render(request,'Signup.html')

def Otp(request):
    return render(request,'Otp.html')
def Retrive(request):
    with con:
       ''' if 'ronnie' in request.POST:
            c.execute("select * from license_details")
            x = c.fetchall()
            License_number = request.POST['License_number']
            Plate_number = request.POST['Plate_number']
            First_Name = request.POST['First_Name']
            Last_Name = request.POST['Last_Name']
            Age = request.POST['Age']
            Contact_Number = request.POST['Contact_Number']
            Gender = request.POST['Gender']
            print(License_number," ", First_Name )
        '''
    if 'verify' in request.POST :
        list = []
        Contact_Number=request.POST.get('Contact_Number')
        return redirect('Otp')
    elif 'not_verified' in request.POST:
        return redirect('Signup')
    else :
        return render(request, 'Signup.html', {'key': '1'})

    return render(request,'Retrive.html')


def LoginStudent(request):
    with con:
        list = []
        fname=[]
        enroll_no=[]
        if 'req' in request.POST :
            mob_no=request.POST.get('Mob_No')
            c.execute("select Mob_number,Enroll_Number,FName,Card_Block from student_register where Mob_Number=%s",(mob_no))
            x=c.fetchall()
            for items in x:
                list.append(items[0])
                global name,enroll,Card_Block
                name = items[2]
                enroll = items[1]
                Card_Block=items[3]
            print(list)

            if mob_no in list:
                print("Mobile number matched")
                if Card_Block==0:
                    print(otp)
                    OTP_REQUEST(URL,mob_no)

                    return redirect('VerifyOTP')
                else:
                    return render(request,'Battery/LoginStudent.html',{'key':'2'})
            else :
                return render(request, 'Battery/LoginStudent.html', {'key': '1'})
    return render(request, 'Battery/LoginStudent.html')

def VerifyOTP(request):
    if 'verify_otp1' in request.POST :
        print("VOTP is Clicked")
        votp=request.POST.get('OTP')
        print(otp)
        if votp==otp:
            person = {'fname': name, 'enroll_no': enroll}
            print (person)
            context = {
                'person': person
            }
            return render(request,'Battery/student.html',context)

