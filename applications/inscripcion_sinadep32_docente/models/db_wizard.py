### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_docente',
    Field('f_nombre', type='string',
          label=T('Nombre')),
    Field('f_email', type='string',
          label=T('Email')),
    Field('f_telefono', type='string',
          label=T('Telefono')),
    Field('f_clave_presupuestal', type='string',
          label=T('Clave Presupuestal')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_docente_archive',db.t_docente,Field('current_record','reference t_docente',readable=False,writable=False))
