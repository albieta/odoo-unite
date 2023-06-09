# Copyright 2020 Tecnativa - Pedro M. Baeza
# Copyright 2020 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Allow to unsubscribe discretely from an event",
    "category": "Marketing",
    "version": "15.0.1.0.0",
    "depends": ["event", "mass_mailing_custom_unsubscribe"],
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/social",
    "data": ["views/event_registration_views.xml"],
    "assets": {
        "web.assets_tests": [
            "/mass_mailing_custom_unsubscribe_event/static/src/js/tour.esm.js"
        ]
    },
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
}
