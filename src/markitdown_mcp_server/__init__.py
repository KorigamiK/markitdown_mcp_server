import asyncio
import os

from .server import run


def main() -> None:
    os.system("notify-send 'Parseer server started'")
    asyncio.run(run())
