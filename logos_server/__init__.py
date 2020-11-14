from logos.context import Container, Service, Class
from logos_server.routes import Router, Route

container = Container({
    'app.command.serve': Service(
        klz='logos_server.command:ServeCommand',
        parameters={}
    )
})
