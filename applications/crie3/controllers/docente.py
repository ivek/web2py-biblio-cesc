# -*- coding: utf-8 -*-
# intente algo como
def agre_alum():
    docentes = db().select(db.docente.ALL, orderby=db.docente.nombre)
    return dict(docentes=docentes)
def mostrar():
   grid = SQLFORM.smartgrid(db.docente, linked_tables=['nombre'])
   return dict(grid=grid)
