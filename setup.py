from setuptools import setup

setup(
    entry_points={
        "pretix.plugin": [
            "pretix_stustapay_placeholders = "
            "pretix_stustapay_placeholders:PretixPluginMeta",
        ],
    },
)
