"""
Device Discovery Module.

This module handles automatic device discovery on the local network. It uses mDNS (Multicast DNS).

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from const import Loggers
from ucapi_framework import DiscoveredDevice
from ucapi_framework.discovery import MDNSDiscovery

_LOG = logging.getLogger(Loggers.SETUP_FLOW)


class StormAudioDiscovery(MDNSDiscovery):
    """
    Discover devices on the local network.
    """

    def parse_mdns_service(self, service_info: Any) -> DiscoveredDevice | None:
        """Parse mDNS service info."""
        if not service_info.addresses:
            return None

        # Get first IPv4 address
        import socket

        address = socket.inet_ntoa(service_info.addresses[0])

        # Extract name and properties
        name = service_info.name.replace(f".{self.service_type}", "")
        properties = {
            k.decode(): v.decode() if isinstance(v, bytes) else v
            for k, v in service_info.properties.items()
        }

        return DiscoveredDevice(
            identifier=service_info.name,
            name=name,
            address=address,
            extra_data=properties,
        )
