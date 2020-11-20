from typing import Callable, Optional, Union

from bottle import Response, Request
from logos.context import Context, context, StackContainer


class Middleware:

    def __init__(self, handler: Callable[[Request, Response], Optional[Union[str, dict, list, Response]]]):
        self.handler = handler

    def __call__(self, request: Request, response: Response, *args, **kwargs):
        return self.handler(request, response, *args, **kwargs)


class ContextMiddleware(Middleware):

    def __call__(self, request: Request, response: Response, *args, **kwargs):
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
            return super().__call__(request, response, *args, **kwargs)
