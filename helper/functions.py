# funcction file

#---------- External Imports
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.core.mail import send_mail

#---------- Internal Imports
from task_manager.models import SendRegisterationEmailData
# ------------ Token Functions  --------------- #

def get_tokens_for_user(user_obj):
        """
        To get tokens by mobile number
        params mobile: mobile of user 
        result: object
        """
        refresh = RefreshToken.for_user(user_obj)

        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

# ---------------------- Send Email for user with registration link--------------------------- #
def send_registration_email(instance):
    """
    Sending Email to admin added email in admin panel.
    :param email: User's email address
    :param instance: instance to update the flag status
    :return : Success or failure message
    """
    registration_link = "https://taskmanager.example.com/register"
    instance = SendRegisterationEmailData.objects.get(id = instance.id)
    user_name = instance.user_name
    data = f"""
    Hello {user_name}!

    Come & Join!! Task Manager App - your personal assistant for efficient task management.

    Click the link below to complete your registration and start organizing your tasks seamlessly:
    {registration_link}

    Take control of your to-do lists, boost your productivity, and achieve your goals with ease.

    Best regards,
    Task Manager Team
    """

    subject = "Start Managing Your Tasks Effectively!"
    message = data
    sender = settings.EMAIL_HOST_USER
    recipient_list = [instance.email]

    try:
        send_mail(subject, message, sender, recipient_list)
    
        print(f"Email sent successfully to {instance.email}")
        instance.flag_email_sent = True
        instance.save()

    except Exception as e:
        # logging.error(f"Failed to send OTP email: {e}")
        print(f"Failed to send OTP email: {e}")