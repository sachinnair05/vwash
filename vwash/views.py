from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect

from homepage.models import bookings;
from homepage.models import services;


def booknow(request):
    if request.method=="POST":
        checkbox=request.POST.getlist('q12_input12[]')
        name=request.POST['q1_fullName[first]']
        email_id= request.POST['q4_email']
        post= bookings()
        post.first_name= request.POST['q1_fullName[first]']
        post.last_name= request.POST['q1_fullName[last]']
        post.area_code= request.POST['q3_phoneNumber3[area]']
        post.phone_number= request.POST['q3_phoneNumber3[phone]']
        post.email_id= request.POST['q4_email']
        post.address_line1= request.POST['q5_address[addr_line1]']
        post.address_line2=request.POST['q5_address[addr_line2]']
        post.city=request.POST['q5_address[city]']
        post.state=request.POST['q5_address[state]']
        post.postal_code=request.POST['q5_address[postal]']
        post.country=request.POST['q5_address[country]']
        post.pickup_date=request.POST['q9_pleaseSelect[year]']+'-'+request.POST['q9_pleaseSelect[month]']+'-'+request.POST['q9_pleaseSelect[day]']
        post.pickup_time=request.POST['q15_selectYour']
        post.details_of_service_request=request.POST['q13_detailsOf']
        post.special_instructions=request.POST['q14_anySpecial']
        if(post.save()):
            messages.add_message(request,messages.WARNING,'Booking Failed')	
            return redirect('homep')
        else:
            booking_id=post.id
            for value in checkbox:
                post= services()
                post.service = value
                post.is_deleted= 0
                post.order_id = bookings.objects.get(id=booking_id)
                post.save()
            if(email_id !=''):
                html_content=render_to_string('ConfirmationMail.html', {'name':name})
                msg = EmailMessage("Booking Confirmation", html_content, "vwash@gmail.com", [email_id])
                msg.content_subtype = "html" 
                msg.send()
                messages.add_message(request,messages.WARNING,'Booking Confirmed')	
                return redirect('homep')
            else:
                messages.add_message(request,messages.WARNING,'Booking Confirmed')	
                return redirect('homep')
    else:    
        return render(request,'booknow.html')