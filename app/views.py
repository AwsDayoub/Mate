from django.shortcuts import render , redirect
from .models import Subject , Message
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
# Create your views here.


def home(request):

    if request.user.is_authenticated:
        #q = request.GET.get('q') if request.GET.get('q') != None else ''
        #subject = Subject.objects.filter( Q(name__icontains=q) | Q(prof__icontains=q) )
        subjects = Subject.objects.filter(collage=request.user.collage)
        students = CustomUser.objects.filter(status='student',collage=request.user.collage)
        proffisors = CustomUser.objects.filter(status='proffisor',collage=request.user.collage)
        employees = CustomUser.objects.filter(status='employee',collage=request.user.collage)
        return render(request,'app/home.html',{'subjects':subjects,'students':students,'proffisors':proffisors,'employees':employees})
    else:
        return render(request,'app/home.html',{})

def subject(request,id):
    sub = Subject.objects.get(pk=id)
    messages = Message.objects.filter(subject=sub)
    return render(request,'app/subject.html',{'subject':sub,'messages':messages})


def profile(request,id):
    pro = CustomUser.objects.get(pk=id)
    return render(request,'app/profile.html',{'user':pro})


