from django.apps import AppConfig


class CdBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cd_blog'


    def ready(self):
        import cd_blog.signals  # noqa