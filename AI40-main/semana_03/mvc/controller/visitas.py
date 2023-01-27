import web
from datetime import datetime
class Visitas:
    def GET(self, nombre):
        try:
            cookie = web.cookies()
            visitas = "0"
            fh = str(datetime.now())
            print(cookie)
            
            web.setcookie("Fecha_y_hora",fh, expires="",domain=None)

            if nombre:
                web.setcookie("nombre",nombre,expires="", domain=None)
            else:
                nombre = "ANONIMO"
                web.setcookie("nombre",nombre,expires="", domain=None)
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas",str(visitas), expires="",domain=None)
            else:
                web.setcookie("visitas",str(1), expires="",domain=None)
                visitas = "1"
            return "Visitas " + str(visitas) + " Nombre " + nombre + " Fecha y Hora " + fh
        except Exception as e:
            return "Error" + str(e.args)