from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Comment

@receiver(post_save, sender=Comment)
def notify_post_author_on_comment(sender, instance, created, **kwargs):
    if not created:
        return
    post = instance.post
    author = post.author
    # if the commenter is the author, don't send
    if instance.author == author:
        return
    subject = f"New comment on your post: {post.title}"
    message = (
        f"Hi {author.username},\n\n"
        f"{instance.author.username} commented on your post \"{post.title}\":\n\n"
        f"\"{instance.content}\"\n\n"
        f"View your post in the app to reply.\n\n"
        f"— Community Discussion Blog"
    )
    recipient = [author.email] if author.email else []
    if recipient:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient, fail_silently=True)
