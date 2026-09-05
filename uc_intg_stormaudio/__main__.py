"""
Entry point for running the integration as a module.

This allows running: python -m uc_intg_stormaudio
Or directly:         python uc_intg_stormaudio

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import os
import sys

if not __package__:
    # Running as `python uc_intg_stormaudio` (directory execution): the
    # project root isn't put on sys.path automatically, unlike `-m`, so a
    # relative import would fail. Add it manually before importing.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from uc_intg_stormaudio import main  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    main()
