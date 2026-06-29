from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail, send_mail
from .models import CustomUser
from events.models import Event
from datetime import datetime

@receiver(post_save, sender=Event)
def send_event_notification(sender, instance, created, **kwargs):
    if created:
        subscribers = CustomUser.objects.filter(subscribed_to_event=True)
        emails = [s.email for s in subscribers]

        if emails:
            max_participants = instance.max_attendance

            if instance.max_attendance == 0:
                max_participants = "Unlimited"

            subject = "New Event Notification"
            text = f"✨ Event: {instance.title}\n\n🚩 Location: {instance.location}\n📅 Date/Time: {datetime.fromisoformat(str(instance.date_time)).strftime('%d.%m.%Y %H:%M')}\n💃 Max participants: {max_participants} \n\n🎙️ Description: {instance.description}"

            send_mass_mail([(subject, text, "backford6@gmail.com", emails)], fail_silently=True)
