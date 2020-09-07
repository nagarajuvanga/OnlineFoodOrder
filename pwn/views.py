from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from django.contrib import messages

def showIndex(request):
    return render(request,"pwn/login.html")

def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    sm = StateModel.objects.all()
    return render(request,"pwn/openstate.html",{'data':sm})


def openCity(request):
    sm = StateModel.objects.all()
    cm = CityModel.objects.all()
    return render(request,"pwn/opencity.html",{'state':sm,'city':cm})


def openCusine(request):
    cm = CuisineModel.objects.all()
    return render(request,"pwn/opencuisine.html",{'data':cm})


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


def savestate(request):
    StateModel(name=request.POST.get('t1'),photo=request.FILES['t2']).save()
    messages.success(request,'state is saved successfully')
    return redirect('state')


def updatestate(request):
    sid = request.GET.get('id')
    sm = StateModel.objects.get(id=sid)
    sm_all = StateModel.objects.all()
    return render(request,'pwn/openstate.html',{'update':sm,"data":sm_all})


def updatedstate(request):
    StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('t1'),photo=request.FILES.get('t2'))
    return redirect('state')


def state_delete(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')


def savecity(request):
    CityModel(name=request.POST.get('t1'),photo=request.FILES.get('t3'),city_type_id= request.POST.get('t2')).save()
    messages.success(request,'City is added successfully')
    return redirect('city')


def updatecity(request):
    cm = CityModel.objects.filter(id=request.GET.get('cid'))
    sm = StateModel.objects.all()
    cm_all = CityModel.objects.all()
    return render(request,'pwn/opencity.html',{'ucity':cm,'state':sm,'city':cm_all})


def updatedcity(request):
    CityModel.objects.filter(id=request.GET.get('cid')).update(name=request.POST.get('t1'),photo =request.FILES.get('t3'))
    messages.success(request,'updated successfull')
    return redirect('city')


def cdelete(request):
    CityModel.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request,'City deleted')
    return redirect('city')


def savecuisine(request):
    CuisineModel(type=request.POST.get('t1'),photo=request.FILES.get('t2')).save()
    messages.success(request,'cuisine saved successfull')
    return redirect('cuisine')


def updatecuisine(request):
    cid = request.GET.get('cid')
    cm = CuisineModel.objects.filter(id=cid)
    cm_all= CuisineModel.objects.all()
    return render(request,'pwn/opencuisine.html',{'update':cm,'data':cm_all})


def updatedcuisine(request):
    CuisineModel.objects.filter(id=request.GET.get('cid')).update(type=request.POST.get('t1'),photo=request.FILES.get('t2'))
    messages.success(request,'cuisine updated successfully')
    return redirect('cuisine')


def delete_cuisine(request):
    CuisineModel.objects.filter(id=request.GET.get('cid')).delete()
    return redirect('cuisine')