import base64
from django.dispatch import receiver
from hashlib import sha256
from pretix.base.services.placeholders import SimpleFunctionalTextPlaceholder
from pretix.base.signals import register_text_placeholders


def secret_hash(secret: str) -> str:
    shorted_digest = sha256(secret.encode("utf-8")).digest()[:24]
    return "$" + base64.urlsafe_b64encode(shorted_digest).decode("utf-8")


@receiver(register_text_placeholders, dispatch_uid="stustapay_pretix_placeholders")
def register_placeholder_renderers(sender, **kwargs):
    return (
        SimpleFunctionalTextPlaceholder(
            "ticket_voucher_hash",
            ["order"],
            lambda order: secret_hash(order.secret),
            "sOcMf0QL8CqE9O4U6ChJpXZjcYjo74zB",
        ),
    )
