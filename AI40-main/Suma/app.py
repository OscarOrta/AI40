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
        form = dict(web.input("sumar"))
        print(type(form))
        n1 = int(form ["numero1"])
        n2 = int(form ["numero2"])
        s = n1 + n2
        return  s
        form = web.input("restar")
        print(type(form))
        n1 = int(form ["numero1"])
        n2 = int(form ["numero2"])
        s = n1 - n2
        return  s
        

if __name__ == "__main__":
    web.config.debug = False
    app.run()