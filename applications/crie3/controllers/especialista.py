# -*- coding: utf-8 -*-
# intente algo como
def agre_alum():
    docentes = db().select(db.especialista.ALL, orderby=db.especialistas.nombre)
    return dict(docentes=docentes)
def mostrar():
   grid = SQLFORM.smartgrid(db.especialistas, linked_tables=['nombre'])
   return dict(grid=grid)
