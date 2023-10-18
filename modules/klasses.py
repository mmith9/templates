import logging
import logging.config
import time

from pydantic.dataclasses import dataclass

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__[__name__.find('.')+1:])
logp = logging.getLogger('print')

logger.debug('importing klasses')

@dataclass
class User:
    id: int
    name: str
    birth: int

    @property
    def age(self) -> int:
        return time.time() - self.birth

