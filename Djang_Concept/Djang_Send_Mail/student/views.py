
"""sending email using django send mail"""
""" 
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def send_email(request):
    subject = 'I have sent you a project report please download it'
    message = 'This report consist of all the project flow including user guide'
    from_mail = 'bkdhaniswar7991@gmail.com'
    to_mail = 'bkdhanishower@gmail.com'
    send_mail(subject,message,from_mail, [to_mail], fail_silently=False)
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

"""


""" Sending Email using sendgrid """

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(
from_email='bkdhaniswar7991@gmail.com',
to_emails='bkdhanishowor@gmail.com',
subject='Sending with Twilio SendGrid is Fun',
html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('EMAIL_PASS'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
        
except Exception as e:
    
    print(e)

