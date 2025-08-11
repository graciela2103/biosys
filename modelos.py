from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario(Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")

    class Meta: 
        api_key = "patCJHPsDL7m21JV7.bf57d0d57c46b04f0389db4579826244822df412291c5bf64b721e4614abdd55"
        base_id = "appktXM30kKg7swqX"
        table_name = "usuario"

class Bioenergia(Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    cantidad = fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    municipio = fields.SelectField("municipio")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")

    class Meta:
        api_key = "patCJHPsDL7m21JV7.bf57d0d57c46b04f0389db4579826244822df412291c5bf64b721e4614abdd55"
        base_id = "appktXM30kKg7swqX"
        table_name = "bioenergia"

if __name__ == "__main__":
    pass
