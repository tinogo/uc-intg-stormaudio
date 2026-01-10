"""
Entry point for running the integration as a module.

This allows running: python -m uc_intg_stormaudio

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio

from . import main

if __name__ == "__main__":
    asyncio.run(main())
