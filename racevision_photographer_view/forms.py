from django import forms

class SignupForm(forms.Form):
    place = forms.IntegerField(max_length=4, unique = True)
    name = forms.CharField(max_length = 100)
    n_licence = forms.DateField(null = False)
    club = forms.CharField(max_length = 100)
    image = forms.FileField(upload_to = 'images/', blank = True)
    netTiming = forms.TimeField(null = False)
    place = forms.IntegerField(max_length=4, unique = True)