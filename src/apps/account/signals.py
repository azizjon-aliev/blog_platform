from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from src.apps.account.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.username} created.")

        Profile.objects.create(user=instance)

        permissions = Permission.objects.filter(
            codename__in=[
                'view_category',
                'view_tag',

                'add_comment',
                'change_comment',
                'view_comment',
                'delete_comment',

                'add_post',
                'change_post',
                'view_post',
                'delete_post',
            ]
        )
        instance.user_permissions.set(permissions)
        instance.is_staff = True
        instance.save()
        print(f"Added permissions to {instance.username}.")
