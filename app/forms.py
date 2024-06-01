from django import forms   #to create model forms we need to import forms class  from django
from app.models import *    #to import models from our models file to create form for that input fields

class Userform(forms.ModelForm):
    class Meta:
        model = User
        #fields='__all__'             #  we are not using fields =all because I don't want all the input fields to be created and displayed in my form
        fields=['username','email','password']         # we want only these infult fields
        widgets={'password':forms.PasswordInput}       # to hide the password so that password while entering should show in ..... format


class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        #fields:'__all__'             # we are not using all here because we are only creating a user their that we are providing to profile form so no need to get agin parent onject in child as we are passing multiple objects (of both parent and child)in same view /function
        fields=['address','profile_pic']   #we need only these input fields  