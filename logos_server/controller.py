from abc import ABC, abstractmethod
from bottle import Request, Response


class AbstractController(ABC):

    @abstractmethod
    def handler(self, request, response, *args, **kwargs):
        pass


class RestController(AbstractController):

    def handler(self, request: Request, response: Response, *args, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        if handler is None:
            response.status = 401
            response.content_type = 'application/json'
            response.body = '{"code": 401, "message": "method not allowed"}'
            return response

        return handler(request, response, *args, **kwargs)

