import odoo
from odoo import models
from odoo.http import request
from odoo.tools.safe_eval import safe_eval
from odoo.addons.website.models.ir_http import ModelConverter

import logging
logger = logging.getLogger(__name__)

class ModelConverter(ModelConverter):

    def generate(self, uid, dom=None, args=None):
        Model = request.env[self.model].sudo(uid)
        args.update(current_website_id=request.env['website'].get_current_website().id)
        domain = safe_eval(self.domain, (args or {}).copy())
        if dom:
            domain += dom
        for record in Model.search_read(domain=domain, fields=['write_date', Model._rec_name]):
            display_name = Model.browse(record['id']).display_name
            if display_name:
                yield {'loc': (record['id'], display_name)}
            elif record.get(Model._rec_name, False):
                yield {'loc': (record['id'], record[Model._rec_name])}

class IrHttp(models.AbstractModel):
    _inherit = ['ir.http']

    @classmethod
    def _get_converters(cls):
        return dict(
            super(IrHttp, cls)._get_converters(),
            model=ModelConverter
        )