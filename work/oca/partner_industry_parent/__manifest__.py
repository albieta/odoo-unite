# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Industry Parent",
    "summary": """
        This module add a parent relation to the partner industry""",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/partner-contact",
    "depends": ["base"],
    "data": [
        "views/res_partner_views.xml",
        "views/res_partner_industry_views.xml",
    ],
    "demo": [],
}
