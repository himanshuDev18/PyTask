import logging

logging.basicConfig(
    filename="pytask.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger("PyTask")