"""
Toggles for accounts related code.
"""
from __future__ import absolute_import

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangoapps.waffle_utils import WaffleFlag

# .. toggle_name: REDIRECT_TO_ORDER_HISTORY_MICROFRONTEND
# .. toggle_type: waffle_flag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout of a new micro-frontend-based implementation of the order history page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2019-04-11
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.ORDER_HISTORY_MICROFRONTEND_URL and site's ENABLE_ORDER_HISTORY_MICROFRONTEND.
# .. toggle_tickets: DEPR-17
# .. toggle_status: supported
REDIRECT_TO_ORDER_HISTORY_MICROFRONTEND = WaffleFlag('order_history', 'redirect_to_microfrontend')


def should_redirect_to_order_history_microfrontend():
    return (
        configuration_helpers.get_value('ENABLE_ORDER_HISTORY_MICROFRONTEND') and
        REDIRECT_TO_ORDER_HISTORY_MICROFRONTEND.is_enabled()
    )


# .. toggle_name: REDIRECT_TO_ACCOUNT_MICROFRONTEND
# .. toggle_type: waffle_flag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout of a new micro-frontend-based implementation of the account page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2019-04-30
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.ACCOUNT_MICROFRONTEND_URL and site's ENABLE_ACCOUNT_MICROFRONTEND.
# .. toggle_tickets: DEPR-17
# .. toggle_status: supported
REDIRECT_TO_ACCOUNT_MICROFRONTEND = WaffleFlag('account', 'redirect_to_microfrontend')


def should_redirect_to_account_microfrontend():
    return (
        configuration_helpers.get_value('ENABLE_ACCOUNT_MICROFRONTEND') and
        REDIRECT_TO_ACCOUNT_MICROFRONTEND.is_enabled()
    )
