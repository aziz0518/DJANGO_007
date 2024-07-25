from django.apps import AppConfig


class OlchaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'olcha'
    def ready(self):
        import olcha.signals
      