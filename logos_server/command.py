from typing import List

from bottle import Bottle
from logos.command import AbstractCommand
from logos.context import context

from logos_server.routes import Registrable, Router
from importlib import import_module


class ServeCommand(AbstractCommand):

    @property
    def routes(self) -> Registrable:
        routes = []
        for module in context.get('app.modules') or []:
            router = getattr(import_module(module), 'router', None)
            if router is not None:
                routes.append(router)
        return Router(
            registrable_list=routes
        )

    def define_arguments(self):
        self.argument_parser.add_argument('--host', default='localhost')
        self.argument_parser.add_argument('--port', default=8080, type=int)

    def execute(self):
        app = Bottle()
        self.routes.register(app)
        arguments = self.arguments
        app.run(
            host=arguments.host,
            port=arguments.port,
            reloader=True
        )


