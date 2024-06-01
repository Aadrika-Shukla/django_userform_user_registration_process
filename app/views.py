from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from app.forms import *   # to import all the forms from our app





'''
DATA WE SUBMITTED ARE OF TWO TYPE DATA,DATA AND MEDIA FILES
IF WE ARE DEALING WITH DATA THEN request.POST will collect input data only
IF WE ARE DEALING WITH DATA  ALONG WITH MEDIA THEN request.POST it  will collect input data only and request.FILES for collecting media files


WHATEVER DATA WE SEND FROM FRONTEND TO BACKEND IT IS NON MODIFIABLE  FOR PERFORMING ANY OPERATIONS LIKE ENCRYTION
WE NEED TO CONVERT INTO MODIFIABLE FORMAT BY USING.save(commit=False) AS BY DEFAULT 
COMMIT=TRUE SO AFTER USING save(commit=False) IT WILL CONVERT NON MODIFIABLE DATA OBJECT INTO MODIFIABLE
DATA OBJECT SO NOW WE CAN PERFORM SOME OPERATIONS ON IT


WE HAVE .set_password() TO PERFORM ENCRYPTION OPERATION
'''



##################  PASSING MULTIPLE OBJECTS TO SINGLE FUNCTION/VIEW    ###############


def registration(request):
    EUFO=Userform()                      #to create empty form fields of user form
    EPFO=Profileform()                   #to create empty form fields of profile form
    d={'EUFO':EUFO,'EPFO':EPFO}          #to pass both parent class(user )object and child class(profile) object to same dictionary variable which we will pass to context attribute
    if request.method=='POST' and request.FILES:    #for collecting both data and media files both
        NMUFDO=Userform(request.POST)                    #for collecting user data as it is sending only input  data 
        NMPFDO=Profileform(request.POST,request.FILES)    #for collecting profile data as it is sending both input data and media files both
        if NMUFDO.is_valid() and NMPFDO.is_valid():      
            MUFDO=NMUFDO.save(commit=False)             #converted non modifiable data object to modifiable data object
            pw=NMUFDO.cleaned_data['password']          # as we need to perform(encryption operation ) to ourv passowrd field so we will collect the data from NON MODIFIABLE FORM only because if we collect from MODIFIABLE OBJECT chances is that it is already modified hence if user login with his password but the developer here modifies it so our user doesn't knows that and it will face him difficulties in login
            MUFDO.set_password(pw)                     #   to perform encryption operation we use set_password here on password filed stored under pw name
            MUFDO.save()                               # now save the encrypted/operations performed data into database
            MPFDO=NMPFDO.save(commit=False)            # again I need to give that encrypted password(modified data after operations ) to my profile of every user  as it is child table
            MPFDO.username=MUFDO                       #as in models of profile we have 3 coloumns username,profile_pic,address but in forms for profile we created only 2 coloumns profile_pic and address and for username we are passing userform object so we need to provide that data to our profile form 
            MPFDO.save()                               # now save the data after performing operations  into database
            return HttpResponse('REGISTRATION SUCCESSFULL')
        else:
            return HttpResponse('INVALID DATA CAN"T REGISTER')
    return render(request,'registration.html',d)
