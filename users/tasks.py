from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add(x, y):
    print(f"args: {x} + {y}")
    from time import sleep

    sleep(10)
    return x + y


@shared_task
def send_otp_mail(email, code):
    send_mail(
        "Your OTP-CODE",
        f"Ваш одноразовый код {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "OK"


@shared_task
def send_report_mail():
    send_mail(
        "Daily Report",
        "кандай пидр мамыр кот",
        settings.EMAIL_HOST_USER,
        ["amirkad033@gmail.com"],
        fail_silently=False,
    )
    return "OK"