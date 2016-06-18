# -*- coding: utf-8 -*-
# intente algo como
def agre_alum():
    docentes = db().select(db.escuela.ALL, orderby=db.escuela.nombre)
    return dict(docentes=docentes)
def mostrar():
   grid = SQLFORM.smartgrid(db.escuela, linked_tables=['nombre'])
   return dict(grid=grid)
