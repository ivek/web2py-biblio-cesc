# -*- coding: utf-8 -*-
# intente algo como
def agre_alum():
    docentes = db().select(db.supervision.ALL, orderby=db.supervision.nombre)
    return dict(docentes=docentes)
def mostrar():
   grid = SQLFORM.smartgrid(db.supervision, linked_tables=['nombre'])
   return dict(grid=grid)
