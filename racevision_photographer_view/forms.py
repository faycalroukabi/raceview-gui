from django import forms

class RunnerForm(forms.Form):
    place = forms.IntegerField()
    n_jersey = forms.IntegerField()
    name = forms.CharField(max_length = 100)
    n_licence = forms.DateField()
    club = forms.CharField(max_length = 100)
    image = forms.FileField()
    netTiming = forms.TimeField()
    place = forms.IntegerField()