from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail, mail_managers
from contactos.models import Contacto
from jimmiss.settings.production import EMAIL_STATIC_URL


def nuevo_contacto(contacto_id):
    qs = Contacto.objects.filter(id=contacto_id)
    if qs.exists():
        obj = qs.first()
        context = {"obj": obj, "STATIC_URL": EMAIL_STATIC_URL}
        try:
            subject = 'JimMiss - Nueva Formulario de Contacto'
            message = render_to_string('mails/contacto/nuevo.txt', context)
            html_message = render_to_string('mails/contacto/nuevo.html', context)
            to_mails = ['carlosblancosierra@gmail.com']
            from_mail = 'no-responda@jimmiss.mx'

            staff_mails_sent = send_mail(
                subject=subject,
                message=message,
                from_email=from_mail,
                recipient_list=to_mails,
                fail_silently=False,
                html_message=html_message
            )

            return staff_mails_sent
        except:
            pass
