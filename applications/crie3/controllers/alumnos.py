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
    contar_esc = 0
    contar_doc = 0
    contar_pdrs = 0
    contar_gpo = 0
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
#busca los alumnos y asesor que coincidan
    count =  db((db.alumnos.aso_esp==asesor) & (db.alumnos.escuela==asesor2)).select()
    for Rows in count:
             contador = contador + 1
#busca los escuelas que coincidan con asesor
    count2 =  db(db.alumnos.aso_esp==asesor).select(db.alumnos.escuela, distinct=True)
    for Rows in count2:
             contar_esc = contar_esc + 1
#busca el numero de docentes en cada escuela
    tmps = db((db.alumnos.aso_esp==asesor) & (db.alumnos.escuela==asesor2)).select(db.alumnos.prof_aula, distinct=True)
    for Rows in tmps:
             contar_doc = contar_doc + 1
#busca los padres en cada escuela         
    padres = db((db.alumnos.aso_esp==asesor) & (db.alumnos.escuela==asesor2)).select(db.alumnos.padre, distinct=True)
    for Rows in padres:
             contar_pdrs=contar_pdrs + 1
#despliega la estadistica por grado y grupo         
    despliegue = db((db.alumnos.aso_esp==asesor) & (db.alumnos.escuela==asesor2)).select(db.alumnos.grupo)
    for Rows in despliegue:
             contar_gpo=contar_gpo + 1
    return dict(contador=contador, formulario=formulario, contar_esc = contar_esc,contar_pdrs=contar_pdrs,contar_gpo=contar_gpo,contar_doc = contar_doc, asesor=asesor,asesor2=asesor2)
