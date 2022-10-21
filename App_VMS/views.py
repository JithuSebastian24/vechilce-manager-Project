from django.shortcuts import render,redirect
from App_VMS.models import VehiceDetails
from django.contrib.auth import authenticate,login


# Create your views here.

def index(req):
    return render(req,'index.html')

def superadminlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            obj=VehiceDetails.objects.all()
            return render(request,"superadminaccess.html",{'obj':obj})
        else:
            return render(request,"superadminlogin.html")
    else:
        return render(request,"superadminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            obj=VehiceDetails.objects.all()
            return render(request,"adminacces.html",{'obj':obj})
            
        else:
            return render(request,"adminlogin.html")
    else:

        return render(request,"adminlogin.html")

def userlogin(req):
    obj=VehiceDetails.objects.all()
    return render(req,"userview.html",{'obj':obj})

def DetailUserview(req,id):
    obj=VehiceDetails.objects.filter(id=id)
    return render(req,"userdetailview.html",{'obj':obj})


def registration(request):
    if request.method=="GET":
        return render(request,"registration.html")
    else:
        num=request.POST.get("Vnum")
        type=request.POST.get("VType")
        model=request.POST.get("VModel")
        desc=request.POST.get("VDes")
        VehiceDetails.objects.create(VehicleNum=num,Vehicletype=type,VehicleModel=model,VehicleDes=desc)

    return render(request,"registration.html")

def edit(request,id):
    obj=VehiceDetails.objects.filter(id=id)
    return render(request,"editregistration.html",{'obj':obj})

def update(request):
    if request.method=="GET":
        return render(request,"registration.html")
    else:
        id=request.POST.get("Vid")
        num=request.POST.get("Vnum")
        type=request.POST.get("VType")
        model=request.POST.get("VModel")
        desc=request.POST.get("VDes")
        VehiceDetails.objects.filter(id=id).update(VehicleNum=num,Vehicletype=type,VehicleModel=model,VehicleDes=desc)
    return render(request,"registration.html")

def delete(request,id):
    VehiceDetails.objects.filter(id=id).delete()
    return render(request,"superadminlogin.html")