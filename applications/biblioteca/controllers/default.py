# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
def index():
    return  dict()
def mostrar():
   grid = SQLFORM.smartgrid(db.biblioteca, linked_tables=['titulo'])
   return dict(grid=grid)
def agregar():
    libros = db().select(db.biblioteca.ALL, orderby=db.biblioteca.titulo)
    return dict(libros=libros)
def estadistica():
    contador = 0
    supl=""
    base = db(db.biblioteca).select()
    fo=FORM('Tu nombre:', INPUT(_name='nombre', _value='', _id="nom"), INPUT(_type='submit', _id="boton"))
    if fo.accepts(request,session):
        supl = "resultado"+ str(fo.element('#nom')['_value'])
        response.flash="form accepted"
      
    elif fo.errors:
        response.flash="form is invalid"
    else:
        response.flash="please fill the form"
    
    formulario= FORM(TR("busquedar :", 
          SELECT(_name='selecion', 
          *[OPTION(base[i].genero, _value=str(base[i].id)) for i in range(len(base))])),
          TR(INPUT(_type='submit')))
    count = db.biblioteca.id.count() 
    for row in db(db.biblioteca.genero == "Ciencias").select(db.biblioteca.titulo, count, groupby=db.biblioteca.genero):
        contador = contador +  row[count]
    return dict(contador=contador, supl=supl, fo=fo,formulario=formulario)



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
