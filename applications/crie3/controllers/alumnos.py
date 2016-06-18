# -*- coding: utf-8 -*-
#página para visualizar nombre y links
def agre_alum():
    alumno = db().select(db.alumnos.ALL, orderby=db.alumnos.nombre)
    return dict(alumno=alumno)
#muestra el grid
def mostrar():
   grid = SQLFORM.smartgrid(db.alumnos, linked_tables=['nombre'])
   return dict(grid=grid)
#saca la estadistica según los parametros que se impongan.
def estadistica():
    contador = 0
    base = db(db.alumnos).select()
# formulario para seleccionar el nombre de elemento a buscar
    formulario= FORM( TR("busqueda: ", 
          SELECT(_name='seleccion', 
          *[OPTION(base[i].nombre, _value=str(base[i].nombre)) for i in range(len(base))])),
          TR(INPUT(_type='submit')),_action="estadistica")
#hace la contabilidad del elemento seleccionado
    count = db.alumnos.id.count()
    for row in db(db.alumnos.nombre==request.vars.seleccion).select(db.alumnos.nombre, count, groupby=db.alumnos.nombre):
        contador = contador +  row[count]
    return dict(contador=contador, formulario=formulario)
