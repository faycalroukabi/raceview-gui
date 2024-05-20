from django.shortcuts import render, redirect
from .forms import RunnerForm
from .models import Runner

def add_runner(request):
    #if(request.method == "POST"):
        form = RunnerForm()
        #print(request.POST)
        #print(form.is_valid())
        #print(form.cleaned_data)
        #if form.is_valid():
            #cleanedData = form.cleaned_data
        print(form)
            #return render(request,"myform_form/SignUp_display.html", {"cd":cleanedData})
        #else:
           # return render(request,"myform_form/SignUp_widgets.html", context={"form":form})
        return render(request,"runner_forms/add_runner.html", context={"form":form})
    
def validate_runner(request):
    if(request.method == "POST"):
        form = RunnerForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            cleanedData = form.cleaned_data
            print(cleanedData)
            Runner.save(cleanedData)
            return render(request,"runner_forms/add_runner.html", {"cd":cleanedData})
        else:
            return render(request,"runner_forms/add_runner.html", context={"form":form})


