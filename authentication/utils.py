from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):

        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']],
        )
        try:
            email.send()
        except Exception as e:
            print("Email sending failed:", e)