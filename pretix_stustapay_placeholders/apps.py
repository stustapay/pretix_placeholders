from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class StuStaPayApp(PluginConfig):
    default = True
    name = "pretix_stustapay_placeholders"
    verbose_name = "Pretix Placeholder Plugin for StuStaPay"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix Placeholder Plugin for StuStaPay")
        author = "Tobias Jülg"
        description = gettext_lazy(
            "Pretix plugin for email placeholder extensions in StuStaPay. Specifically, it adds ticket voucher hash placeholders to the pretix email templates."
        )
        visible = True
        version = __version__
        category = "FORMAT"
        compatibility = "pretix>=2.7.0"
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_stustapay_placeholders.StuStaPayApp"
