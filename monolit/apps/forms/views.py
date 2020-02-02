from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


def callback_form(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        msg_body = f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}'

        send_mail('Заявка на обратный звонок [monolit.site]', msg_body, settings.EMAIL_HOST_USER, ['jqphp@yandex.ru',])

        return redirect(request.POST.get("url_from"))
