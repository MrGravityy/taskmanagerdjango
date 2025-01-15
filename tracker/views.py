from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms
# Create your views here.

class newform(forms.Form):
    tasks = forms.CharField(max_length=10)
def index(request): 
    if "taskslist" not in request.session: 
        request.session["taskslist"]=[]
    if request.method=='POST': 
        removetask= request.POST.get('task')
        print(removetask)
        if removetask and removetask in request.session["taskslist"]:
            request.session["taskslist"].remove(removetask)
            request.session.modified =True
    return render(request, 'tracker/index.html', 
                  {"tasks":request.session["taskslist"]})
        
def add(request): 
    if request.method=="POST":
        validation = newform(request.POST)
        if validation.is_valid(): 
            print(validation.cleaned_data)
            print(validation.errors)
            task = validation.cleaned_data['tasks']
            request.session["taskslist"].append(task)
            request.session.modified = True
            return HttpResponseRedirect(reverse('index'))
        else: 
            return render(request,'tracker/add.html',{'form':validation})
    return render(request, 'tracker/add.html',{'form':newform})

