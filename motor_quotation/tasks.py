from celery import shared_task

from django.conf import settings

from app.features.utils import render_to_pdf

# to send HTML emails
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

@shared_task
def send_email(title, emails_list, email_template, text_alternative_email, email_context, pdf_data, pdf_template, has_pdf):
    plaintext = get_template(text_alternative_email)
    htmly = get_template(email_template)

    text_content = plaintext.render(email_context)
    html_content = htmly.render(email_context)

    msg = EmailMultiAlternatives(
        title,
        text_content,
        settings.EMAIL_HOST_USER,
        emails_list,
    )

    msg.attach_alternative(html_content, "text/html")

    if has_pdf and pdf_data and pdf_template:
        pdf = render_to_pdf(pdf_template, pdf_data)
        msg.attach('quotation-pdf.pdf', pdf)

    msg.send()