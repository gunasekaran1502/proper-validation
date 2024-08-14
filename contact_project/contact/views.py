from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
          
            form.save()

  
            subject = 'New Contact Us Message'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']
            recipient_list = ['recipient_email@gmail.com']
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Message sent successfully!')
            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html',{'form':form})