from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data': data})

def add(request):
    print(request.method) #GET #POST
    print(request.GET) #<QueryDict: {}>
    print(request.POST) #<QueryDict: {}> #<QueryDict: {'csrfmiddlewaretoken': ['268VmpHxZwJ1E3ibBZ1Bhwd2mgj985FOWC0nJ3eDZMevFfKP2JabZ2ImHD7HVrBf'], 'title': ['django '], 'desc': ['this is a TODO project']}>

    if request.method == 'POST':
        a = request.POST['title']
        b = request.POST['desc']
        print(a,b) #django  this is a TODO project
        TaskModel.objects.create(
            title = a,
            desc = b
        )
        return redirect('home')
    return render(request,'add.html')

def complete(request):
    data = CompleteModel.objects.all()
    return render(request,'complete.html',{'data': data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{'data': data})

def about(request):
    return render(request,'about.html')

#home page complete button
def complete_h(request,id):
    '''
    1.fetch the particular record from TaskModel
    2.create this record in CompleteModel
    3.Delete this record in Taskmodel
    '''
    data = TaskModel.objects.get(id=id)
    print(data)
    print(data.title,data.desc)
    CompleteModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

#home page complete all button 
def complete_allh(request):
    '''
    1.fetch the all records which are present in TaskModel
    2.Create them in CompleteModel
    3.delete it from TaskModel
    '''
    data = TaskModel.objects.all()
    print(data) #<QuerySet [<TaskModel: TaskModel object (2)>, <TaskModel: TaskModel object (4)>, <TaskModel: TaskModel object (6)>, <TaskModel: TaskModel object (7)>, <TaskModel: TaskModel object (8)>]>
    for i in data:
        print(i)
        print(i.title,i.desc)
        CompleteModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        #i.delete() delete each record after created
    data.delete() #Delete all records after created
    return redirect('complete')

#home page delete button 
def delete_h(request,id):
    '''
    1.fetch the particular record from TaskModel
    2.create this record in Taskmodel
    3.Delete this record in Taskmodel
    '''
    data = TaskModel.objects.get(id=id)
    TaskModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')