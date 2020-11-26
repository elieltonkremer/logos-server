from logos.command import AbstractCommand
from logos.context import context


class ServeCommand(AbstractCommand):

    def define_arguments(self):
        self.argument_parser.add_argument('--host', default='localhost')
        self.argument_parser.add_argument('--port', default=8080, type=int)

    def execute(self):
        app = context.get('app.server')
        arguments = self.arguments
        app.run(
            host=arguments.host,
            port=arguments.port,
            reloader=True
        )


