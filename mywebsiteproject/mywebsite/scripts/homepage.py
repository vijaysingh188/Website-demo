from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect
from ..models import ContactMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings



class homepageview(TemplateView):
    def get(self, request):
        return render(request, "index.html")
    

class aboutpageview(TemplateView):
    def get(self, request):
        return render(request, "about.html")
    
class servicepageview(TemplateView):
    def get(self, request):
        return render(request, "service.html")
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Save the form data to the database
        ContactMessage.objects.create(name=name, email=email, message=message_content)

        # Add a success message
        subject = 'New Contact Form Submission'
        message = f"Name: {name}\nEmail: {email}\nMessage: {message_content}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['dunchanmaster007@gmail.com']  # Add your email address here
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('/service', messages.success(request, 'Thank you for contacting Us. Our team will contact you as soon as earliest.', 'alert-success'))


    
class contactpageview(TemplateView):
    def get(self, request):
        return render(request, "contact.html")
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Save the form data to the database
        ContactMessage.objects.create(name=name, email=email, message=message_content)

        # Add a success message
        subject = 'New Contact Form Submission'
        message = f"Name: {name}\nEmail: {email}\nMessage: {message_content}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['dunchanmaster007@gmail.com']  # Add your email address here
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('/contact', messages.success(request, 'Thank you for contacting Us. Our team will contact you as soon as earliest.', 'alert-success'))

