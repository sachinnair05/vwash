from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from adminpage.models import admin
from homepage.models import bookings
from homepage.models import services
# Create your views here.
def adminpage(request):
    if request.method=="POST":
        email = request.POST['email']
        password= request.POST['password']
        count = admin.objects.filter(user_id= email, user_password = password, is_deleted=0 ).count()
        if count==1:
            user_id=admin.objects.filter(user_id=email)
            request.session['id']=user_id[0].id
            return redirect(dashboard)	
        else:
            messages.add_message(request,messages.WARNING,'Login Failed')	
            return render(request,"login.html")
    else:
        if request.session.has_key('id'):
            return redirect(dashboard)
        else:    
            return render(request,'login.html')

def dashboard(request):
    if request.session.has_key('id'):
        result_booking = bookings.objects.filter(is_deleted=0)
        result_service = services.objects.filter(is_deleted=0)
        # return HttpResponse(result_service[0].order_id)
        return render(request, "dashboard.html",{'booking':result_booking,'services':result_service})
    else:
        messages.add_message(request,messages.WARNING,'You Need To Login First')
        return redirect(adminpage)

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        return redirect(adminpage)
    else:
        messages.add_message(request,messages.WARNING,'You Need To Login First')
        return redirect(adminpage)