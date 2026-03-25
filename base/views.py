from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

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
    return render(request,'add.html')

def complete(request):
    return render(request,'complete.html')

def trash(request):
    return render(request,'trash.html')

def about(request):
    return render(request,'about.html')