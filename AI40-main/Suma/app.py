import web
urls = (
    '/', 'Index',
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

    def POST(self):
    
        form = dict(web.input())
        if form["operacion"] == "sumar":
            return int(form ["numero1"]) + int(form ["numero2"])
        elif form["operacion"] == "restar":
            return int(form ["numero1"]) - int(form ["numero2"])
        elif form["operacion"] == "multiplicar":
            return int(form ["numero1"]) * int(form ["numero2"])
        elif form["operacion"] == "dividir":
            return int(form ["numero1"]) / int(form ["numero2"])

if __name__ == "__main__":
    web.config.debug = False
    app.run()