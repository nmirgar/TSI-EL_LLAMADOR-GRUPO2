# -*- coding: utf-8 -*-
# from odoo import http


# class ElLlamador(http.Controller):
#     @http.route('/el__llamador/el__llamador', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/el__llamador/el__llamador/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('el__llamador.listing', {
#             'root': '/el__llamador/el__llamador',
#             'objects': http.request.env['el__llamador.el__llamador'].search([]),
#         })

#     @http.route('/el__llamador/el__llamador/objects/<model("el__llamador.el__llamador"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('el__llamador.object', {
#             'object': obj
#         })
