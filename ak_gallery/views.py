from django.shortcuts import render
from exhibitions.models import Exhibition
from django.core.mail import send_mail
from django.shortcuts import redirect


def home(request):
    featured_exhibition = Exhibition.objects.filter(status='current').first()
    return render(request, 'home.html', {
        'featured_exhibition': featured_exhibition,
    })

def about(request):
    return render(request, 'about.html')


def send_inquiry(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', 'Не указан')
        message = request.POST.get('message', '')

        # Получаем список работ с кодами из скрытого инпута формы
        artworks_list = request.POST.get('artworks_list', 'Ничего не выбрано')

        full_name = f"{first_name} {last_name}".strip()

        subject = f"Новый запрос на покупку от {full_name}"
        email_body = f"""
Здравствуйте!
У вас новый запрос с сайта AK Gallery.

КОНТАКТЫ КЛИЕНТА:
Имя: {full_name}
Email: {email}
Телефон: {phone}

ВЫБРАННЫЕ РАБОТЫ:
{artworks_list}

СООБЩЕНИЕ ОТ КЛИЕНТА:
{message}
"""
        try:
            send_mail(
                subject,
                email_body,
                'akgallery.kg@gmail.com',  # Отправитель
                ['akgallery.kg@gmail.com'],  # Получатель
                fail_silently=False,
            )
        except Exception as e:
            pass

    return redirect(request.META.get('HTTP_REFERER', '/'))