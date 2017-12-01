from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Lookup

class NotEqual(Lookup):
    lookup_name = 'ne'
    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params



def get_upload_path(instance, filename):
    return '{0}/{1}'.format(instance.areaPertenece.nombre, filename)
# Create your models here.
class Usuario(models.Model):
    username = models.OneToOneField(User)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, default="")
    direccion = models.CharField(max_length=200, default="")
    telefono = models.CharField(max_length=20)
    pagina = models.CharField(max_length=50, default="")
    arboles = models.IntegerField(default=0)
    email = models.EmailField()
    image = models.ImageField(upload_to='Usuarios', default='/img/user.png')

    def __str__(self):
        return str(self.username)

class Area_Verde(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    creador = models.ForeignKey(Usuario, related_name="creador")
    encargado = models.ForeignKey(Usuario, related_name="encargado")
    enAdopcion = models.CharField(max_length=200, default="")

class Foto(models.Model):
    areaPertenece = models.ForeignKey(Area_Verde)
    image = models.ImageField(upload_to=get_upload_path)
    subidaPor = models.ForeignKey(Usuario)
    fechaPublicacion = models.DateTimeField(default = datetime.now, blank = True)

class Adopcion(models.Model):
    creadaPor = models.ForeignKey(Usuario,default =  "", blank = True, related_name="duenio")
    adoptadaPor = models.ForeignKey(Usuario,default = "", blank = True, related_name="adoptante")
    paraArea = models.ForeignKey(Area_Verde)
    fechaCreacion = models.DateTimeField(default = datetime.now, blank = True)
    fechaAdopcion = models.DateTimeField(default = datetime.now, blank = True)

class Peticion(models.Model):
    hechaPor = models.ForeignKey(Usuario)
    paraArea = models.ForeignKey(Area_Verde)
    peticion = models.IntegerField()
    arbolesTotales = models.IntegerField(default=0)
    comentario = models.CharField(max_length=50)
    abierta = models.BooleanField(default=True)

class Aportacion(models.Model):
    hechaPor = models.ForeignKey(Usuario)
    paraArea = models.ForeignKey(Area_Verde)
    respondiendoPeticion = models.ForeignKey(Peticion, blank=True, null=True)
    aportacion = models.IntegerField()
    comentario = models.CharField(max_length=50)
