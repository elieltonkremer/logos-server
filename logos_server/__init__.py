from logos.context import Container, Service, ResourceGroup, Class

container = Container({
    'groups.request_middleware': ResourceGroup(r'^app.request_middleware'),
    'app.request_middleware.context': Class('logos_server.middleware:ContextMiddleware'),
    'app.factories.server': Service(
        klz='logos_server.factory:ServerFactory',
        parameters={}
    ),
    'app.server': Service(
        factory='app.factories.server',
        parameters={}
    ),
    'app.command.serve': Service(
        klz='logos_server.command:ServeCommand',
        parameters={
            'server': '%app.server%'
        }
    )
})
