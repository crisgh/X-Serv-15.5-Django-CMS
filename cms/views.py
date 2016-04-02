from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound

 # Create your views here.

def newpages(request,name):
    try:
        obj=Pages.objects.get(name=name)
        return HttpResponse(obj.page)
    except Pages.DoesNotExist:
        return HttpResponse("<h3> Page Not Found, " + name + "</h3>")

def savepage(request,name,page):
    obj=Pages(name=name,page=page)
    obj.save()
    return HttpResponse(" Guardado..<h3><FONT COLOR=red>"+name+"</FONT></h3>")

def showpages(request):
    respuesta = ""
    list_cont=Pages.objects.all()
    for cont in list_cont :
        respuesta+="<li>"+cont.name+" : "+cont.page+"</li>"
    return HttpResponse(respuesta)

def Error404(request,cont1,cont2):
    return HttpResponse (" Error404 Not Found, try again.")
