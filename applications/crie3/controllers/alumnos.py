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
    base = db(db.especialistas).select()
    base2 = db(db.escuela).select()
# formulario para seleccionar el nombre de elemento a buscar
    formulario= FORM( TR("ESPECIALISTA: ", 
          SELECT(_name='seleccion', 
          *[OPTION(base[i].nombre, _value=str(base[i].nombre)) for i in range(len(base))])),
          (TR("ESCUELA: ",SELECT(_name='seleccion2', 
          *[OPTION(base2[i].clv_p, _value=str(base2[i].clv_p)) for i in range(len(base2))]),
          INPUT(_type="submit"))))
#hace la contabilidad del elemento seleccionado
    asesor = request.vars.seleccion
    asesor2 = request.vars.seleccion2
    count =  db((db.alumnos.aso_esp==asesor) & (db.alumnos.escuela==asesor2)).select()
    count2 = db.alumnos.escuela.count()
    for Rows in count:
             contador = contador + 1
    return dict(contador=contador, formulario=formulario, asesor=asesor,asesor2=asesor2)
