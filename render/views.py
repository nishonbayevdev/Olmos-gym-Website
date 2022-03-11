from django.shortcuts import render,redirect
from .models import corousel,Plan,Employes,VideoMedia,Client,Contact,Blog1

# Create your views here.
def home(request):
    data = {
        'corousel' : corousel.objects.all(),
        'plans' : Plan.objects.all(),
        'employes' : Employes.objects.all(),
    }
    return render(request,'index.html',data)

def classDeteals(request):
    return render(request,'class-details.html')

def aboutUs(request):
    data = {
        'client':Client.objects.all(),
        'video':VideoMedia.objects.all()[0],
        'employes1': Employes.objects.all(),

    }
    return render(request, 'about.html',data)

def classTimetable(request):
    return render(request, 'class-timetable.html')

def team(request):
    return render(request, 'team.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    data = {
        'Blog':Blog1.objects.all()
    }
    return render(request, 'blog.html',data)

def notFound(request):
    return render(request, 'notFound.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def main(request):
    return render(request, 'main.html')

def blogDetails(request):
    return render(request, 'blog.html')


def contactSend(request):
    if request.method == 'POST':
        Contact(name=request.POST['name'],email=request.POST['email'],phonnumber=request.POST['phone'],comment=request.POST['comment']).save()
        return redirect(to='/')
    return render(request,'contact.html')