from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "casillero_sendex.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import casillero_sendex.users.signals  # noqa F401
        except ImportError:
            pass
