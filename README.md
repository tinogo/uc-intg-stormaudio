# Unfolded Circle Integration StormAudio

This repository contains the source code for the [Unfolded Circle Remote Two/3](https://www.unfoldedcircle.com/) integration driver for StormAudio devices.

The integration is based on the amazing work of JackJPowell's [ucapi-framework](https://github.com/jackjpowell/ucapi-framework).

## Project Structure

```
├── driver.json              # Integration metadata and configuration
├── intg-stormaudio/         # Main integration code
│   ├── const.py             # Constants and device configuration dataclass
│   ├── device.py            # Device communication and state management
│   ├── discover.py          # Network device discovery
│   ├── driver.py            # Main entry point
│   ├── media_player.py      # Media player entity
│   └── setup.py             # Setup flow and user configuration
├── config/                  # Runtime configuration storage
├── Dockerfile               # Container build configuration
└── requirements.txt         # Python dependencies
```

## Development

### Prerequisites

- Python 3.11+
- uv
- Docker, Docker Compose

### Local Development

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the integration:
   ```bash
   python intg-stormaudio/driver.py
   ```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `UC_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | `DEBUG` |
| `UC_CONFIG_HOME` | Configuration directory path | `/config` |
| `UC_INTEGRATION_INTERFACE` | Network interface to bind | `0.0.0.0` |
| `UC_INTEGRATION_HTTP_PORT` | HTTP port for the integration | `9090` |
| `UC_DISABLE_MDNS_PUBLISH` | Disable mDNS advertisement | `false` |

## Deployment

### Install on Remote

1. Build the integration package (tar.gz file)
2. Upload via the Remote's web configurator under Integrations
3. Configure your device through the setup wizard

### Updating the integration on the Remote

1. Build the integration package (tar.gz file)
2. Remove the existing integration from the Remote (twice) → no worries, all your settings will still be there.
3. Update via the Remote's web configurator under Integrations
4. Configure your device through the setup wizard

### Docker

```bash
docker run -d \
  --name=uc-intg-stormaudio \
  --network host \
  -v $(pwd)/config:/config \
  --restart unless-stopped \
  ghcr.io/tinogo/uc-intg-stormaudio:latest
```

### Docker Compose

```yaml
services:
  uc-intg-stormaudio:
    image: ghcr.io/tinogo/uc-intg-stormaudio:latest
    container_name: uc-intg-stormaudio
    network_mode: host
    volumes:
      - ./config:/config
    restart: unless-stopped
```

## Resources

- [UC Integration Python Library](https://github.com/aitatoi/integration-python-library)
- [UCAPI Framework](https://github.com/jackjpowell/ucapi-framework)
- [Unfolded Circle Developer Documentation](https://github.com/unfoldedcircle/core-api)

## License

Mozilla Public License Version 2.0 – see [LICENSE](LICENSE) for details.
