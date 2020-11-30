from logos.command import AbstractCommand
from logos.context import context


class ServeCommand(AbstractCommand):

    def __init__(self, server):
        self.server = server

    def define_arguments(self):
        self.argument_parser.add_argument('--host', default='localhost')
        self.argument_parser.add_argument('--port', default=8080, type=int)

    def execute(self):
        arguments = self.arguments
        self.server.run(
            host=arguments.host,
            port=arguments.port,
            reloader=True
        )


