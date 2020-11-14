from logos.context import Container, Service

container = Container({
    'app.command.serve': Service(
        klz='logos_server.command:ServeCommand',
        parameters={}
    )
})
