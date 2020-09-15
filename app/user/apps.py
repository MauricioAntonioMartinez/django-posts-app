from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):  # WHEN THE USER IS LOADED
        import user.signals
