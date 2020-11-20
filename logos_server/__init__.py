from logos.context import Container, Service, ResourceGroup, Class

container = Container({
    'groups.request_middleware': ResourceGroup(r'^app.request_middleware'),
    'app.request_middleware.context': Class('logos_server.middleware:ContextMiddleware'),
    'app.command.serve': Service(
        klz='logos_server.command:ServeCommand',
        parameters={}
    )
})
