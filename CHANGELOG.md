# Integration Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

_Changes in the next release_

---

## [0.8.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.7.0...v0.8.0) (2025-12-31)


### Features

* Restrict the Loggers to specific types ([46906bb](https://github.com/tinogo/uc-intg-stormaudio/commit/46906bb5c149f847a89f1d9f9b3e0e890a938117))


### Bug Fixes

* **ci:** Only check the unsorted imports in the CI-env, but don't fix them ([bd5ba89](https://github.com/tinogo/uc-intg-stormaudio/commit/bd5ba8957f64a3edc1812fe6972518fc8df69bcd))
* Emit only a single event after building the source_list ([a1abc01](https://github.com/tinogo/uc-intg-stormaudio/commit/a1abc01893189e8aa36a019906dbd5d29de0c291))


### Miscellaneous

* Extend the release-please config ([38da8c1](https://github.com/tinogo/uc-intg-stormaudio/commit/38da8c1f6593c9a17f6ea2cd7100acb575db11f2))
* Move the compose env one level up ([0af3dea](https://github.com/tinogo/uc-intg-stormaudio/commit/0af3deaebda0236d83b2c8a91c2082341bbeb776))
* Move the sound_mode_list into the device config ([a21d4e3](https://github.com/tinogo/uc-intg-stormaudio/commit/a21d4e3fb2f81272edab8a01f7afa566d2644e4f))
* Remove obsolete code ([3e4c7dc](https://github.com/tinogo/uc-intg-stormaudio/commit/3e4c7dc57e5ede09e63c940c03d06db0a0e044af))

## [0.7.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.6.0...v0.7.0) (2025-12-30)


### Features

* **#3:** Add a proper connection check to the setup flow ([#20](https://github.com/tinogo/uc-intg-stormaudio/issues/20)) ([f548a92](https://github.com/tinogo/uc-intg-stormaudio/commit/f548a9281fe838d4af14d2c0826c2e670fd83780))

## [0.6.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.5.0...v0.6.0) (2025-12-30)


### Features

* Wait for the response after selecting the input source ([265d11c](https://github.com/tinogo/uc-intg-stormaudio/commit/265d11cbc14255b5fc6aa216ec3fbda5deacb1a3))


### Miscellaneous

* Improve the Docker (Compose) setup ([053867c](https://github.com/tinogo/uc-intg-stormaudio/commit/053867c6e85d1aa7da6fa4fcaaa66411b8420d3a))

## [0.5.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.4.2...v0.5.0) (2025-12-30)


### Features

* **ci:** Add actionlint and PR-title linter ([cfde9ff](https://github.com/tinogo/uc-intg-stormaudio/commit/cfde9ffad1e8bd0b51ec33d4f6a632a58337b3a1))


### Bug Fixes

* **ci:** Satisfy actionlint ([#17](https://github.com/tinogo/uc-intg-stormaudio/issues/17)) ([cd03acb](https://github.com/tinogo/uc-intg-stormaudio/commit/cd03acb1df824c44533cb7b3a638ec470167c889))


### Miscellaneous

* Remove the telnetlib3 dependency ([c6cbc3f](https://github.com/tinogo/uc-intg-stormaudio/commit/c6cbc3f39c461015cae0780e6dc042f53bb43899))

## [0.4.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.4.1...v0.4.2) (2025-12-30)


### Miscellaneous

* slightly improve some wording ([667b716](https://github.com/tinogo/uc-intg-stormaudio/commit/667b716584778d5fb644f8fa8013595d52fdf829))

## [0.4.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.4.0...v0.4.1) (2025-12-30)


### Bug Fixes

* **#1:** Fix the artifact name ([1dd6058](https://github.com/tinogo/uc-intg-stormaudio/commit/1dd605880f92cc1202497aeef22b46cb42d4adab))

## [0.4.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.3.5...v0.4.0) (2025-12-30)


### Features

* **#1:** Introduce Google Release please ([61c36da](https://github.com/tinogo/uc-intg-stormaudio/commit/61c36dac922a6a3133c04119ad02ee4308c8c124))
* **#1:** Rely solely on Google Release Please ([6a5a78d](https://github.com/tinogo/uc-intg-stormaudio/commit/6a5a78dbd8f36964fe34fd4b55389454dd95cb63))

## v0.1.0 - 2025-12-03
### Added
- Initial template release based on ucapi-framework.
- Media player entity template with common features.
- Device communication template with connection management.
- Setup flow with manual device entry.
- mDNS device discovery template.
- Docker and Docker Compose configurations.
- Development environment with core-simulator.
