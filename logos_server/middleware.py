from typing import Callable, Optional, Union

from bottle import Response, Request


class Middleware:

    def __init__(self, handler: Callable[[Request, Response], Optional[Union[str, dict, list, Response]]]):
        self.handler = handler

    def __call__(self, request: Request, response: Response, *args, **kwargs):
        return self.handler(request, response, *args, **kwargs)


