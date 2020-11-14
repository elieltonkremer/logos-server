# logos-server

Bottle wrapper for Logos


## usage

### module requirements declaration
```py
from logos.context import ApplicationContainer


app = ApplicationContainer(
  modules=[
    "logos_server"
  ]
)
```

### route definition `[your-package]/__init__.py`

```py
from logos.context import Container, Class
from logos_server.routes import Router, Route

container = Container([...])


router = Router([
  Route(
    path="/user/",
    methods=["GET", "POST"],
    controller=Class("[your-package].controller:UserController")
  )
])

```

### run server

`python app.py --command serve [--port] [--host]`



