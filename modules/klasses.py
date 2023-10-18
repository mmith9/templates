import time
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    birth: int

    @property
    def age(self) -> int:
        return time.time() - self.birth

