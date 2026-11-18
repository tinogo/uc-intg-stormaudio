# Agent instructions

## Build, lint, and run

The project requires Python 3.14+ and `uv`. Install the development dependencies with:

```bash
uv sync
```

Run the same checks as CI:

```bash
uv run -m pylint uc_intg_stormaudio
uv run -m flake8 uc_intg_stormaudio --count --show-source --statistics
uv run -m isort uc_intg_stormaudio/. --check --verbose
uv format --check
```

To check one changed module, pass its path to each tool, for example:

```bash
uv run -m pylint uc_intg_stormaudio/device.py
uv run -m flake8 uc_intg_stormaudio/device.py --count --show-source --statistics
uv run -m isort uc_intg_stormaudio/device.py --check --verbose
uv format --check uc_intg_stormaudio/device.py
```

There is no automated test suite in the repository. For an end-to-end development run, use `docker compose up --remove-orphans --build --watch --pull=always` to start the integration with the Unfolded Circle Core Simulator and the TCP echo server.

Run the driver locally with `uv run python3 uc_intg_stormaudio` or `uv run python -m uc_intg_stormaudio`.

## Architecture

- `uc_intg_stormaudio/__init__.py` wires the `ucapi-framework` `BaseIntegrationDriver` to the StormAudio device, entities, persistent config manager, discovery, and setup flow. `__main__.py` is the module entry point.
- `StormAudioSetupFlow` accepts discovered mDNS devices or a manually entered hostname/IP, tests the TCP connection, and creates a `StormAudioConfig`. The framework persists the config, including the discovered source and preset maps.
- `StormAudioDevice` extends `PersistentConnectionDevice`. Its connection is managed by the framework; `StormAudioClient` (`stormaudio.py`) reads newline-delimited TCP responses and sends commands over the device connection (default port 23).
- The device parses protocol responses into `StormAudioDeviceAttributes`, updates persisted source/preset lists, and calls `push_update()`. Media-player, remote, select, and sensor entities subscribe to the device and synchronize their Unfolded Circle API attributes from this shared state.
- Device commands and protocol identifiers are centralized in `device.py` and `const.py`. `simple_commands.py` maps public simple-command identifiers to device methods. `select_entity.py` and `sensor.py` use per-type configuration maps to define entity behavior and state projection.

## Repository conventions

- Follow `docs/code_guidelines.md`: use double quotes and keep lines within 120 characters. Import ordering is configured in `setup.cfg`; format with `uv format`.
- Use `StormAudioDeviceAttributes` as the shared source of current device state. When adding a protocol response, update that state in the response handler and push an update so subscribed entities stay synchronized.
- When adding a select or sensor type, extend its `StrEnum` and corresponding configuration map; entity construction is already registered for every enum member in `__init__.py`.
- When adding or removing a runtime dependency, use `uv add` or `uv remove`, then regenerate the exported runtime dependency list with `uv export --format requirements.txt --output-file requirements.txt --no-annotate --no-header --no-hashes --no-dev`. Keep `uv.lock` and `requirements.txt` in sync.
- Keep integration metadata in `driver.json` aligned with changes that affect the published driver or supported API.
