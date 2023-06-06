from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def send_email(request):
    send_mail('Hello from PrettyPrinted',
    'Hello there. This ia an automated message.',
    'bkdhaniswar7991@gmail.com', ['bkdhanishower@gmail.com'], fail_silently=False)
    return HttpResponse(request)
    # subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')

    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['admin@example.com'])
    #     except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/contact/thanks/')
    # else:
    #     return HttpResponse('Make sure all fields are entered and valid.') 

