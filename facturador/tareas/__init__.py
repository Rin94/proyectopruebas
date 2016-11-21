class clientes(models.Model):
    first_name = models.CharField('first_name', max_length = 35)
    last_name = models.CharField('last_name', max_length = 45)
    gender = models.IntegerField('gender')
    email = models.EmailField('email', max_length = 60)
    phone_number = models.CharField('phone', max_length = 15)
    num_direccion = models.IntegerField('numero_casa')
    calle = models.CharField('calle', max_length = 45)
    colonia = models.CharField('colonia', max_length = 45)
    codigo_postal = models.IntegerField('codigo_postal')
    municipio = models.CharField('municipio', max_length = 30)
    estado = models.CharField('estado', max_length = 30)
    #detalles = models.CharField('detalles', max_length = 120, null = True, blank = True)


    def __init__(self):
        pass


    def __init__(self, name, lastname, gender, email,phone,num,call,col,cp,mun,est):
        models.Model.__init__(self)
        self.first_name = name
        self.last_name = lastname
        self.gender=gender
        self.email=email
        self.phone_number=phone
        self.num_direccion=num
        self.calle=call
        self.colonia=col
        self.codigo_postal=cp
        self.municipio=mun
        self.estado=est


    def __unicode__(self):
        return self.first_name + ' ' + self.last_name