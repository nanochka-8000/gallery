from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages


def submit_inquiry(request):
    # Проверяем, что данные пришли методом POST (пользователь нажал кнопку отправки)
    if request.method == 'POST':
        # Вытаскиваем данные из формы по атрибуту name
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        artworks_list = request.POST.get('artworks_list', 'Работы не выбраны')

        # Формируем тему и текст письма
        subject = f'АК Галерея: Новый запрос от {first_name} {last_name}'

        body = f"""
У вас новый запрос с сайта АК Галереи.

Контактные данные:
Имя: {first_name} {last_name}
Email: {email}
Телефон: {phone}

Интересующие работы:
{artworks_list}

Сообщение пользователя:
{message}
"""
        try:
            # Функция отправки письма
            send_mail(
                subject,  # Тема
                body,  # Текст письма
                'akgallery.kg@gmail.com',  # От кого отправляем (должно совпадать с EMAIL_HOST_USER)
                ['akgallery.kg@gmail.com'],  # Кому отправляем (тебе на эту же почту)
                fail_silently=False,
            )
            # Если отправка успешна, можем передать сообщение на фронтенд
            messages.success(request, 'Ваш запрос успешно отправлен! Мы свяжемся с вами в течение 24 часов.')
        except Exception as e:
            # Обработка ошибки, если письмо не ушло
            messages.error(request, 'Произошла ошибка при отправке запроса. Пожалуйста, попробуйте позже.')

        # Перенаправляем пользователя обратно на ту страницу, где он был
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # Если кто-то попытается просто перейти по ссылке /inquiries/ (GET запрос), кидаем на главную
    return redirect('/')