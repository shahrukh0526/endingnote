from django.apps import AppConfig


class EndingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ending'
    
    def ready(self):
        try:
            import ending.signals
        except ImportError:
            pass
