# -*- coding: utf-8 -*-
def build_query(field, op, value):
    equals = ['equals','igual']
    not_equal = ['not equal','distinto']
    greater_than = ['greater than','mayor que']
    less_than = ['less than','menor que']
    starts_with = ['starts with','comienza con']
    ends_with = ['ends with','termina con']
    contains = ['contains','contiene']
    if (op in equals):
        return field == value
    elif (op in not_equal):
        return field != value
    elif (op in greater_than):
        return field > value
    elif (op in less_than):
        return field < value
    elif (op in starts_with):
        return field.startswith(value)
    elif (op in ends_with):
        return field.endswith(value)
    elif (op in contains):
        return field.contains(value)

def build_row(label,ops,field,dddw_component):
    chkval = request.vars.get('chk'+field,None)
    txtval = request.vars.get('txt'+field,None)
    opval = request.vars.get('op'+field,None)
    dddw_id=None
    dddw_table=None
    dddw_column=None
    
    # Si la columna esta en la lista de las dddw (Drop Down DataWindow) construye el select options
    if dddw_component <> None:
        if len(dddw_component) % 3 == 0: #Verifica que la longitud de la lista sea multiplo de 3
            for j in range(len(dddw_component)):
                #En este caso la primera columna viene de la forma 'codigo_tabla:codigo_dddw'
                cadena = dddw_component[j]
                li_pos = cadena.find(':')
                aux=''
                if (li_pos > 0):
                   aux = cadena[0:li_pos]
                if field == dddw_component[j]:
                   dddw_id = field
                   dddw_table = dddw_component[j+1]
                   dddw_column= dddw_component[j+2]
                if field == aux:
                   dddw_id = field
                   dddw_table = dddw_component[j+1]
                   dddw_column= dddw_component[j+2]
                aux=''
    if field == dddw_id:
        txtval = request.vars.get('search_'+dddw_table,None)
        query = db(db[dddw_table]).select()

        #Arma la fila para el elemento select options
        row = TR(TD(INPUT(_type="checkbox",_name="chk"+field,value=chkval=='on')),
                 TD(label),
                 TD(SELECT(ops,_name="op"+field,value=opval)),
                 TD(SELECT(_name='search_'+dddw_table,*[OPTION(i[dddw_column], _value=str(i['id'])) 
                     for i in query],value = txtval)))
    else:
        #arma fila para un elemento input de tipo text
         row = TR(TD(INPUT(_type="checkbox",_name="chk"+field,value=chkval=='on')),
                  TD(label),
                  TD(SELECT(ops,_name="op"+field,value=opval)),
                  TD(INPUT(_type="text",_name="txt"+field,_value=txtval)))
    return row,chkval,txtval,opval
    
def dynamic_search(table,columns,dddw_component=None):
    tbl = TABLE()
    selected = []
    #Por defecto las opciones para las comparaciones aparecen en Inglés
    
    query = table.id > 0

    li_flag = 0 # Se asume que la primera vez no hay ningún criterio de busqueda seleccionado
    for field in table.fields:
        #Obtiene la etiqueta que tiene la columna
        label = db[table][field].label
        ops = ['contains','not equal','greater than','less than','starts with','ends with','equals']
        # si el idioma seleccionado es Español
        if T.accepted_language == 'es':
            ops = ['contiene','igual','distinto','mayor que','menor que','comienza con','termina con']  

        # Si la columna no tiene una etiqueta, asigna el nombre de la columna como etiqueta.
        if label == '' or label == None:
            label = field

         #Sólo se incluyen las columnas que enviamos en la lista columns.
        for element in columns:
            if field == element:
                #función que construye la fila de la tabla
                if ((db[table][field].type in ('integer','long','float','complex')) and (T.accepted_language == 'es')):
                    ops = ['igual','distinto','mayor que','menor que']
                if ((db[table][field].type == ('integer','long','float','complex')) and (T.accepted_language <> 'es')):
                    ops = ['not equal','greater than','less than']

                row,chkval,txtval,opval = build_row(label,ops,field,dddw_component)
                #Agrega la fila a la tabla.
                tbl.append(row)
                if chkval:
                    li_flag = 1
                    if txtval:
                        query &= build_query(table[field],opval,txtval)
                    selected.append(table[field])

    # Esto es para evitar que recupere todas las filas, cuando se ingresa a la página la primera vez.
    if li_flag == 0: 
        query = table.id == 0

    #Construye el formulario	
    form = FORM(FIELDSET(LEGEND(T("Filter by")),tbl,_class='groupbox',_id='groupbox'),BR(),INPUT(_type="submit"))
    #Recupera las filas con el criterio seleccionado.
    results = db(query).select()
    return form, results,query
