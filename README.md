## FEP
### Finir En Prison

FEP is a general purpose exploitation framework made in Python.

### Setup

``` bash
git clone https://github.com/traumatism/fep && cd fep && bash setup.sh
```

### Add module

```py
from fep.common.module import Module

class ExampleModule(Module):

    @property
    def data(self) -> dict[str, str]:
        return {
            "name": "example-module",
            "desc": "Example module",
            "author": "Your username here",
        }

    def execute(self) -> int:
        # module code here

        return 0
```

**Don't forget to import your module class in `modules/__init__.py`**