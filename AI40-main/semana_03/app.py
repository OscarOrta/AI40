import web
urls = (
    '/(.*)', 'mvc.controller.visitas.Visitas',
)
app = web.application(urls, globals())



if __name__ == "__main__":
    web.config.debug = False
    app.run()