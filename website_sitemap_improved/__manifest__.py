# -*- coding: utf-8 -*-
{
    'name': 'Website Sitemap Improved',
    'summary': 'Simple improvements to sitemap.xml',
    'version': '1.0.0',
    'author': 'Vihren Kanev',
    'support': 'vihren.kanev@gmail.com',
    'price': 0.00,
    'currency': 'EUR',
    'license': 'AGPL-3',
    'category': 'website',
    'depends': ['website','website_sale'],
    "description": """
        This plug-in improves sitemap for better search engine indexing.

        Changes to sitemap:
            - Locations in sitemap are now exactly the same as URLs in e-commerce.

        Before:
            <url>
                <loc>http://localhost:8069/shop/product/apple-wireless-keyboard-18</loc>
            </url>
        After:
            <url>
                <loc>http://localhost:8069/shop/product/e-com10-apple-wireless-keyboard-18</loc>
            </url>
    """,
    'data': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'category': 'Website',
    'images':['static/description/cover.png']
}
