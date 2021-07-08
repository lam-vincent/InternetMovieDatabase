from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def conversionHeureMinute(duree_minute):
    heure = duree_minute//60
    minute = duree_minute % 60
    return f"{heure}h{minute}"


def afficherCategories(categories):
    res = []
    for i in range(len(categories)):
        res.append(categories[i].name)
        res.append(", ")
    if len(res) >= 1:
        res.pop()
    if len(categories) > 1:
        res[len(res)-2] = " & "
    return "".join(res)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
