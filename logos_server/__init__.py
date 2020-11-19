from logos.context import Container, Service, ResourceGroup

container = Container({
    'groups.request_middleware': ResourceGroup(r'^app.request_middleware'),
    'app.command.serve': Service(
        klz='logos_server.command:ServeCommand',
        parameters={}
    )
})
