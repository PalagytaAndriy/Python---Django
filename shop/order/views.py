import imaplib

from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Product
from .forms import OrderForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email.message


def order(request):
        # Налаштування з'єднання з сервером
        mail = imaplib.IMAP4_SSL('imap.ukr.net')
        mail.login('made_by_mama@ukr.net', 'VykYqvJiV1CksdiG')

        # Створення повідомлення
        msg = email.message.EmailMessage()
        msg['From'] = 'made_by_mama@ukr.net'
        msg['To'] = 'made_by_mama@ukr.net'
        msg['Subject'] = 'Нове замовлення!'


        mail.append('INBOX', None, None, msg.as_bytes())
        mail.logout()

