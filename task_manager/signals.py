#--------------- External Imports ----------------- #

from rest_framework.response import Response
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import threading

#--------------- Internal Imports ----------------- #
from task_manager.models import SendRegisterationEmailData
from helper.functions import send_registration_email

#----------------------- Signal to send email on user email
@receiver(post_save, sender=SendRegisterationEmailData)
def send_email(sender, instance, created, **kwargs):
    if instance.flag_email_sent == False:
        try:
            send_registration_email(instance)
        except Exception as e:
            print(f"Failed to send email: {e}")
        