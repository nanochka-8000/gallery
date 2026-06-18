from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Message

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Message.objects.create(name=name, email=email, phone=phone, message=message)

        send_mail(
            subject=f'Новое сообщение с сайта от {name}',
            message=f'Имя: {name}\nEmail: {email}\nТелефон: {phone}\n\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['info@akgallery.kg'],
            fail_silently=True,
        )

        return redirect('/contacts/?sent=true')
    return render(request, 'contacts/contacts.html')