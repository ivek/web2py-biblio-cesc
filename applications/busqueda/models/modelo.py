# -*- coding: utf-8 -*-
db.define_table('catalogoxtipo',
Field('cod_articulo','integer',label='Cód. Artículo'),
Field('marca','string',length = 20, label = 'Marca'),
Field('tipo','string',length = 20,label = 'Tipo'),
Field('descripcion','string',length = 50,label = 'Descripción'),
Field('foto','upload',label = 'Foto'))
