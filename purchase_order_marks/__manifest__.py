# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Marks",
    "summary": """
        This module add the field marks""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["Lolstalgia"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Purchase",
    "version": "11.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "purchase",
        "foreign_purchase_order",
        "purchase_order_invoice_to",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/res_partner_oct_view.xml",
        "views/purchase_order_view.xml",
        "views/res_company_view.xml"
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
