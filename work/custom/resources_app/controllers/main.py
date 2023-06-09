from odoo import http
from werkzeug.wrappers import Response
import json
import math
import logging

_logger = logging.getLogger(__name__)

#if we want to check auth, add --> auth="my_api_key" <-- in the @http.route

class Resources(http.Controller):
    @http.route("/resources/infrastructure", methods=["GET"], website=True, auth='public')
    def list(self, *args, **kwargs):

        #search elements
        ScientificDomain = http.request.env["resources.scientific_domain"]
        Keyword = http.request.env["resources.keyword"]
        universities = http.request.env['res.partner'].search([
            ('id', 'in', http.request.env["resources.infrastructure"].search([]).mapped('home_partner_institution.id'))
        ]).read(['name'])
        scientificDomains = ScientificDomain.search([])
        keywords = Keyword.search([])

        return http.request.render(
            "resources_app.infrastructure_web_template",
            {
                "page": 1,
                "themes": scientificDomains,
                "keywords": keywords,
                "universities": universities
            }
        )

    @http.route("/resources/infrastructure/filtered", methods=["POST"], csrf=False, auth='public')
    def filtered(self, *args, **kwargs):
        theme = kwargs.get("theme")
        university = kwargs.get("university")
        keywords_str = kwargs.get("keywords")
        open = kwargs.get("open")

        page = int(kwargs.get('page', 1))
        items_per_page = 10

        domain = []

        if theme:
            domain.append(('scientific_domain', '=', theme))

        if university:
            domain.append(('home_partner_institution.name', '=', university))
        _logger.info(open)
        if open == 'True':
            domain.append(('external_users', '=', True))
        elif open == 'False':
            domain.append(('external_users', '=', False))

        if keywords_str:
            keyword_names = keywords_str.split(',')
            keyword_objs = http.request.env['resources.keyword'].search([('name', 'in', keyword_names)])
            keyword_ids = keyword_objs.ids
            domain.append(('keywords', 'in', keyword_ids))
                

        infrastructures = http.request.env['resources.infrastructure'].search(domain, limit=items_per_page, offset=(page - 1) * items_per_page)
        total_items = math.ceil(http.request.env['resources.infrastructure'].search_count(domain)/items_per_page)

        return http.request.render(
            "resources_app.infrastructure_list",
            {
                'infrastructures': infrastructures,
                'total_items': total_items,
                'page': page,
                'items_per_page': items_per_page,
            }
        )