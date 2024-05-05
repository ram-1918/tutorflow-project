from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_email_verification(email):
    html_message = render_to_string('feedback.html', {"email": email.value})
    sub = 'Thanks for your feedback!'
    msg = 'Thank you for the feedback, please feel free to review my resume attached!'
    try: 
        print("Everything is good so far")
        send_mail(
            sub, 
            msg, 
            from_email= settings.EMAIL_HOST_USER, 
            recipient_list= [email.value], 
            html_message=html_message, 
            fail_silently=False)
    except: print('Issue with Sending email!')