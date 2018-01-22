# -*- coding: utf-8 -*-
from odoo import http

# class SceMatrix(http.Controller):
#     @http.route('/sce_matrix/sce_matrix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sce_matrix/sce_matrix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sce_matrix.listing', {
#             'root': '/sce_matrix/sce_matrix',
#             'objects': http.request.env['sce_matrix.sce_matrix'].search([]),
#         })

#     @http.route('/sce_matrix/sce_matrix/objects/<model("sce_matrix.sce_matrix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sce_matrix.object', {
#             'object': obj
#         })