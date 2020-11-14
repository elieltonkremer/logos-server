from abc import ABC, abstractmethod
from typing import List

from logos.context import Class, context, Parameter, Context, StackContainer
from bottle import Bottle, request, response


class Registrable(ABC):

    @abstractmethod
    def register(self, app: Bottle):
        pass


class Route(Registrable):

    def __init__(self, path: str, controller: Class, methods: list = None, parameters: dict = None,
                 handler: str = 'handler'):
        self.path = path
        self.controller = controller
        self.methods = methods or ['GET']
        self.parameters = parameters or {}
        self.handler = handler

    def register(self, app: Bottle):
        @app.route(path=self.path, method=self.methods)
        def wrapper(*args, **kwargs):
            request_containers = []
            request_context = Context.new_from(
                context=context.get('context'),
                runtime={
                    "request": request,
                    "response": response
                },
                container=StackContainer(request_containers)
            )
            with request_context:
                if request_context.has('app.container.request'):
                    request_containers.append(request_context.get('app.container.request'))
                controller_class = self.controller.resolve(context)
                controller = controller_class(**Parameter.resolve_value(self.parameters, context))
                handler = getattr(controller, self.handler)
                return handler(request, response, *args, **kwargs)


class Router(Registrable):

    def __init__(self, registrable_list: List[Registrable]):
        self.registrable_list = registrable_list

    def register(self, app: Bottle):
        for registrable in self.registrable_list:
            registrable.register(app)
