from django.conf import settings
from django.db.models.signals import pre_delete,post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def delete_user_token(sender, instance, **kwargs):
    Token.objects.filter(user=instance).delete()

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_user_token(sender , instance , created =False, **kwargs):
    if created:
        Token.objects.create(user = instance)