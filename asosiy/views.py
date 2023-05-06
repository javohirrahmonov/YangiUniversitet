from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def fanlar(request):
    fan = request.GET.get('qidir')
    if fan == "" or fan is None:
        content = {
            "fanlar": Fan.objects.all()
        }
    else:
        content = {
            "fanlar": Fan.objects.filter(nom__icontains=fan)
        }

    return render(request,'fanlar.html',content)

def fan_ochir(request,son):
    Fan.objects.filter(id=son).delete()
    return redirect("/fanlar/")

def yonalishlar(request):
    content = {
        "yonalishlar" : Yonalish.objects.all()
    }
    return render(request,'yonalishlar.html',content)

def yonalish_ochir(request,son):
    Yonalish.objects.filter(id = son).delete()
    return redirect("/yonalishlar/")

def ustozlar(request):
    ustoz = request.GET.get('qidir')
    if ustoz == "" or ustoz is None:
        content = {
            "ustozlar": Ustoz.objects.all()
        }
    else:
        content = {
            "ustozlar": Ustoz.objects.filter(ism__icontains=ustoz)
        }

    return render(request,'ustozlar.html',content)

def ustoz_ochir(request,son):
    Ustoz.objects.filter(id=son).delete()
    return redirect('/ustozlar/')

def asosiy(request):
    return HttpResponse("<h1>Salom universitet boshqaruv tizimiga hush kelibsiz</h1>")