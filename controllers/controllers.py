# -*- coding: utf-8 -*-
# from odoo import http


# class ElLlamador(http.Controller):
#     @http.route('/el_llamador/el_llamador', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/el_llamador/el_llamador/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('el_llamador.listing', {
#             'root': '/el_llamador/el_llamador',
#             'objects': http.request.env['el_llamador.el_llamador'].search([]),
#         })

#     @http.route('/el_llamador/el_llamador/objects/<model("el_llamador.el_llamador"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('el_llamador.object', {
#             'object': obj
#         })
