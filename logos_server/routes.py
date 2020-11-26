from abc import ABC, abstractmethod
from typing import List, Callable, Type, Optional, Union

from logos.context import Class, context, Parameter, Context, StackContainer
from bottle import Bottle, request, response, Request, Response


class Registrable(ABC):

    @abstractmethod
    def register(self, app: Bottle):
        pass


class Route(Registrable):

    def __init__(self,
                 path: str,
                 controller: Class,
                 methods: list = None,
                 parameters: dict = None,
                 handler: str = 'handler',
                 middleware: List[Callable[[Request, Response], Optional[Union[str, dict, Response]]]] = None
                 ):
        self.path = path
        self.controller = controller
        self.methods = methods or ['GET']
        self.parameters = parameters or {}
        self.handler = handler
        self.middleware = middleware or []

    def register(self, app: Bottle):
        request_middleware: List[Type[Callable]] = [
            context.get(item) for item in context.get('groups.request_middleware').values()
        ]
        paths = self.path if isinstance(self.path, list) else [self.path]
        for path in paths:
            @app.route(path=path, method=self.methods)
            def wrapper(*args, **kwargs):
                controller_class = self.controller.resolve(context)
                controller = controller_class(**Parameter.resolve_value(self.parameters, context))
                handler = getattr(controller, self.handler)
                for middleware_class in reversed(self.middleware):
                    handler = middleware_class(handler)
                for middleware_class in reversed(request_middleware):
                    handler = middleware_class(handler)
                return handler(request, response, *args, **kwargs)


class Router(Registrable):

    def __init__(self, registrable_list: List[Registrable]):
        self.registrable_list = registrable_list

    def register(self, app: Bottle):
        for registrable in self.registrable_list:
            registrable.register(app)
