# Copyright 2016 Tecnativa - Antonio Espinosa
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MailTrackingEvent(models.Model):
    _inherit = "mail.tracking.event"

    mass_mailing_id = fields.Many2one(
        string="Mass mailing",
        comodel_name="mailing.mailing",
        readonly=True,
        related="tracking_email_id.mass_mailing_id",
        store=True,
    )

    @api.model
    def process_open(self, tracking_email, metadata):
        res = super().process_open(tracking_email, metadata)
        mail_mail_stats = self.sudo().env["mailing.trace"]
        domain = [("mail_mail_id_int", "=", tracking_email.mail_id_int)]
        mail_mail_stats.set_opened(domain=domain)
        return res

    def _tracking_set_bounce(self, tracking_email, metadata):
        mail_mail_stats = self.sudo().env["mailing.trace"]
        domain = [("mail_mail_id_int", "=", tracking_email.mail_id_int)]
        mail_mail_stats.set_bounced(domain=domain)

    @api.model
    def process_hard_bounce(self, tracking_email, metadata):
        res = super().process_hard_bounce(tracking_email, metadata)
        self._tracking_set_bounce(tracking_email, metadata)
        return res

    @api.model
    def process_soft_bounce(self, tracking_email, metadata):
        res = super().process_soft_bounce(tracking_email, metadata)
        self._tracking_set_bounce(tracking_email, metadata)
        return res

    @api.model
    def process_reject(self, tracking_email, metadata):
        res = super().process_reject(tracking_email, metadata)
        self._tracking_set_bounce(tracking_email, metadata)
        return res

    @api.model
    def process_spam(self, tracking_email, metadata):
        res = super().process_spam(tracking_email, metadata)
        self._tracking_set_bounce(tracking_email, metadata)
        return res
