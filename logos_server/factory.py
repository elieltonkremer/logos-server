from importlib import import_module

from logos.context import context

from logos_server.routes import Registrable, Router
from bottle import Bottle


class ServerFactory:

    @property
    def router(self) -> Registrable:
        routes = []
        for module in context.get('app.modules') or []:
            router = getattr(import_module(module), 'router', None)
            if router is not None:
                routes.append(router)
        return Router(
            registrable_list=routes
        )

    def create(self):
        server = Bottle()
        self.router.register(server)
        return server
