from pyairtable import Api 

api = Api("patCJHPsDL7m21JV7.bf57d0d57c46b04f0389db4579826244822df412291c5bf64b721e4614abdd55")
tabla = api.table("appktXM30kKg7swqX", "usuario")

#altas 
yo={'clave': 'avila', 
'contra': 'avila',
'nombre': 'graciela', 
'admin': 1
}
tabla.create(yo)

registros= tabla.all()
for r in registros:
    print(r["fields"])

#Inicio de la aplicacion 
if __name__ == "__main__":
     ft.app(target=main)