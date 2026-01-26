# Unfolded Circle Integration StormAudio

This repository contains the source code for the [Unfolded Circle Remote Two/3](https://www.unfoldedcircle.com/) integration driver for StormAudio devices. The Focal Astral 16 and Bryston SP4 should work, too.

The integration is based on the amazing work of JackJPowell's [ucapi-framework](https://github.com/jackjpowell/ucapi-framework).

## Table of contents

1. [Supported entity types](#supported-entity-types)
2. [Installation instructions](#installation-instructions)
3. [Update instructions](#update-instructions)
4. [Versioning](#versioning)
5. [Changelog](#changelog)
6. [Development](#development)
7. [Resources](#resources)
8. [License](#license)

## Supported entity types

- [Media player](#media-player-entity)
- [Remote](#remote-entity)
- [Sensors](#sensor-entity)

### Media Player entity

The Media Player entity implements the following features:
- `ON_OFF`: Provides dedicated on/off commands
- `DPAD`: Enables navigating your ISPs front panel (for supported models)
- `TOGGLE`: Provides the power toggle
- `VOLUME`: Enables adjusting the volume slider via the Remote 3's touch slider
- `VOLUME_UP_DOWN`: Provides dedicated volume up/down commands
- `HOME`: Provides the home and back commands. Both commands are mapped to the `back` command, as there is no `home` command for the ISPs
- `MUTE`: Mutes the device
- `UNMUTE`: Unmutes the device
- `MUTE_TOGGLE`: Toggles the mute state of the device
- `SELECT_SOUND_MODE`: Provides a dropdown of available sound modes (Upmixers)
- `SELECT_SOURCE`: Provides a dropdown of available sources

The entity doesn't provide any of the playback features, though, as the StormAudio API doesn't provide any of those commands (they would only be active for Roon anyway).

Furthermore, the Media Player entity implements all the Simple-Commands provided by the Remote entity, too.

### Remote entity

The Media Player entity implements the following features:
- `ON_OFF`: Provides dedicated on/off commands
- `TOGGLE`: Provides the power toggle
- `SEND_CMD`: Allows sending a (custom) command to the device
- `SEND_CMD_SEQUENCE`: Allows sending a (custom) command sequence to the device

Furthermore, it implements many Simple-Commands.

These commands `SEND_CMD` and `SEND_CMD_SEQUENCE` allow the user to send any of your StormAudio's supported TCP commands (see https://www.stormaudio.com/tools-guides/ → Drivers Packages → TCP/IP API for reference).

Additionally, you can send the following custom commands for the `send_cmd` and `send_cmd_sequence` commands:
1. `PRESET_<YourPresetName>` --> This will select the given preset on your device.
2. `SOURCE_<YourSourceName>` --> This will select the given source on your device.
3. `VOLUME_<YourVolumeLevel>` --> This will set the volume level on your device to the given value (i.e. `VOLUME_45` will result in `-55dB` in your ISP).

### Sensor entity

This integration provides the following sensors:
- Current Volume
- Muted Status
- Current Loudness Setting
- Current Preset
- Current Source
- Current Upmixer
- StormXT Status
- Tone controls (Bass, Treble, Brightness, Center enhancement, Surround enhancement, LFE enhancement)

## Installation instructions

1. Download the integration package (tar.gz file) from the [Releases](https://github.com/tinogo/uc-intg-stormaudio/releases) page
2. Upload the archive via the Remote's web configurator: "Integrations" → "Install custom"
3. Configure your device through the setup wizard

## Update instructions

1. Download the integration package (tar.gz file) from the [Releases](https://github.com/tinogo/uc-intg-stormaudio/releases) page
2. Remove the existing integration from the Remote (twice) → no worries, all your configured activity settings will still be there.
3. Upload the archive via the Remote's web configurator: "Integrations" → "Install custom"
4. Configure your device through the setup wizard

## Versioning

We use [SemVer](https://semver.org) for versioning. For the versions available, see the [tags and releases in this repository](https://github.com/tinogo/uc-intg-stormaudio/releases).

## Changelog

The major changes found in each new release are listed in the [changelog](https://github.com/tinogo/uc-intg-stormaudio/blob/main/CHANGELOG.md) and under the GitHub [releases](https://github.com/tinogo/uc-intg-stormaudio/releases).

## Development

### Project Structure

```
├── driver.json              # Integration metadata and configuration
├── uc_intg_stormaudio/         # Main integration code
│   ├── __init__.py          # Main entry point
│   ├── const.py             # Constants and device configuration dataclass
│   ├── device.py            # Device communication and state management
│   ├── discover.py          # Network device discovery
│   ├── driver.py            # Integration Driver
│   ├── media_player.py      # Media player entity
│   └── setup.py             # Setup flow and user configuration
├── config/                  # Runtime configuration storage
├── Dockerfile               # Container build configuration
└── requirements.txt         # Python dependencies
```

### Prerequisites

- Python 3.11+
- uv
- Docker, Docker Compose

### Running the integration

1. Prepare the environment:
   ```bash
   uv venv
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Install the git-hooks:
   ```bash
   uv run pre-commit install
   ```

4. Run the integration either locally or via a Compose environment:
   1. Locally:
      ```bash
      uv run uc_intg_stormaudio/__init__.py
      ```
   2. via Compose:
      ```bash
      docker compose up --remove-orphans --build --watch --pull=always
      ```

### Adding and removing dependencies

#### Adding dependencies

```bash
uv add <dependency>
uv export --format requirements.txt --output-file requirements.txt --no-annotate --no-header --no-hashes --no-dev
```

#### Removing dependencies

```bash
uv remove <dependency>
uv export --format requirements.txt --output-file requirements.txt --no-annotate --no-header --no-hashes --no-dev

```

#### Updating all dependencies

```bash
uv lock --upgrade
uv export --format requirements.txt --output-file requirements.txt --no-annotate --no-header --no-hashes --no-dev
```

### Environment Variables

| Variable                   | Description                                 | Default   |
|----------------------------|---------------------------------------------|-----------|
| `UC_LOG_LEVEL`             | Logging level (DEBUG, INFO, WARNING, ERROR) | `DEBUG`   |
| `UC_CONFIG_HOME`           | Configuration directory path                | `/config` |
| `UC_INTEGRATION_INTERFACE` | Network interface to bind                   | `0.0.0.0` |
| `UC_INTEGRATION_HTTP_PORT` | HTTP port for the integration               | `9090`    |
| `UC_DISABLE_MDNS_PUBLISH`  | Disable mDNS advertisement                  | `false`   |


## Resources

- [UC Integration Python Library](https://github.com/aitatoi/integration-python-library)
- [UCAPI Framework](https://github.com/jackjpowell/ucapi-framework)
- [Unfolded Circle Developer Documentation](https://github.com/unfoldedcircle/core-api)

## License

Mozilla Public License Version 2.0 – see [LICENSE](LICENSE) for details.
