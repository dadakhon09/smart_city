from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


USER_TYPES = (
    (0, 'Admin'),
    (1, 'Operator'),
    (2, 'Citizen')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    type = models.IntegerField(null=True, blank=True, choices=USER_TYPES)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def wtf(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.username)
        if UserProfile.objects.filter(slug=slug).exists():
            pass
        else:
            slug = slug
        up = UserProfile(user=instance, slug=slug)
        up.save()
