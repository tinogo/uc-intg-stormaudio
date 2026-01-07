# Integration Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

_Changes in the next release_

---

## [0.10.5](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.4...v0.10.5) (2026-01-07)


### Bug Fixes

* Reduce the maximum timeout for the power-on command ([#39](https://github.com/tinogo/uc-intg-stormaudio/issues/39)) ([6912372](https://github.com/tinogo/uc-intg-stormaudio/commit/691237260c0cb433d5db02350bea70f56cc32f31))


### Miscellaneous

* **docs:** Update the README ([991d767](https://github.com/tinogo/uc-intg-stormaudio/commit/991d767ceb7c9478a05e9af30aa3c5dcaa699aae))
* Optimize the compose setup ([7d06df9](https://github.com/tinogo/uc-intg-stormaudio/commit/7d06df949d4cec7db6c954f6d8b5c3c6bf72fb02))

## [0.10.4](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.3...v0.10.4) (2026-01-06)


### Bug Fixes

* Force a connection to the device during entity registration ([48568dc](https://github.com/tinogo/uc-intg-stormaudio/commit/48568dc01786f5e78b0cbfa9b710fd09eee0bc87))


### Miscellaneous

* **docs:** Adds docs for updating all dependencies ([59a2445](https://github.com/tinogo/uc-intg-stormaudio/commit/59a24454ff7fe34d70f389d488de66dbaad6403b))
* Format the code ([45acff4](https://github.com/tinogo/uc-intg-stormaudio/commit/45acff48021d2912bb4469dc50badd5a237b1d8a))


### Reverts

* Remove the websocket parameter from the handle_command method again ([6e2acf8](https://github.com/tinogo/uc-intg-stormaudio/commit/6e2acf8e8eea56e20915c20d3d04f9c0b48698ab))

## [0.10.3](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.2...v0.10.3) (2026-01-06)


### Bug Fixes

* **deps:** Update the requirements.txt ([d1f0f0c](https://github.com/tinogo/uc-intg-stormaudio/commit/d1f0f0cdff99e4a7698efd00db160b43c4db51e5))


### Miscellaneous

* **deps:** bump aiohttp from 3.13.2 to 3.13.3 ([#30](https://github.com/tinogo/uc-intg-stormaudio/issues/30)) ([06cbfd4](https://github.com/tinogo/uc-intg-stormaudio/commit/06cbfd49d2bc6c6d83455d1761c34d272ec4903a))
* **deps:** Update integration for 1.4.2 ucapi-framework ([#33](https://github.com/tinogo/uc-intg-stormaudio/issues/33)) ([d42f89f](https://github.com/tinogo/uc-intg-stormaudio/commit/d42f89f46e21d96db39b2ad241bf22ec91712ac2))
* Reuse some more code from the device within the media_player ([237d5b8](https://github.com/tinogo/uc-intg-stormaudio/commit/237d5b80ed9e2c07aa9d408938c7292672cfd009))

## [0.10.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.1...v0.10.2) (2026-01-05)


### Bug Fixes

* **#8:** Revert the multiple connections prevention ([1730c6e](https://github.com/tinogo/uc-intg-stormaudio/commit/1730c6effc3918a948009b57d8fc8ad8e59e0c9a))

## [0.10.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.0...v0.10.1) (2026-01-05)


### Bug Fixes

* **#8:** Fix device initialization ([#29](https://github.com/tinogo/uc-intg-stormaudio/issues/29)) ([9308398](https://github.com/tinogo/uc-intg-stormaudio/commit/93083988d3032ac18a3b164a60423c936c486219))

## [0.10.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.9.0...v0.10.0) (2026-01-02)


### Features

* **ci:** Check the code against flake8 ([#28](https://github.com/tinogo/uc-intg-stormaudio/issues/28)) ([be69f78](https://github.com/tinogo/uc-intg-stormaudio/commit/be69f78a8ef95f15e43925c6966b36f5ee342d45))


### Bug Fixes

* **docs:** Fix the coding guidelines ([430870f](https://github.com/tinogo/uc-intg-stormaudio/commit/430870fbc94f7aeeb950c56293e6638b53bfa8ee))


### Reverts

* Revert the changes related to the connection handling ([b84c858](https://github.com/tinogo/uc-intg-stormaudio/commit/b84c858af58d5dc4aebaaf3c2059c9f520f2c8ba))

## [0.9.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.8.1...v0.9.0) (2026-01-02)


### Features

* **#5:** Prepare the Zone-Management ([3e0798b](https://github.com/tinogo/uc-intg-stormaudio/commit/3e0798b0593326485ae523107d288c4c6fbd9dfa))
* Make the establishing the connection even more robust ([5dcde83](https://github.com/tinogo/uc-intg-stormaudio/commit/5dcde83aca03ea887c3ae3212526a014c47be4ae))


### Bug Fixes

* add a missing Response constant ([9bce8ad](https://github.com/tinogo/uc-intg-stormaudio/commit/9bce8ad103fb88608502f7cb5c79c3d3e5e329ce))


### Miscellaneous

* **ci:** Lint the code against Pylint within the CI-Pipeline ([2f5f57c](https://github.com/tinogo/uc-intg-stormaudio/commit/2f5f57c7845add11b46819715df56c15356cdee1))
* consistently use positional parameters in the media_player ([b555e1a](https://github.com/tinogo/uc-intg-stormaudio/commit/b555e1a388f9b1b468703e499683ecd075d6db10))
* Format the code ([cd745d0](https://github.com/tinogo/uc-intg-stormaudio/commit/cd745d0e715f3ff4c98cf8820b3ac16f5a4b0e89))
* Make use of the entity argument ([4dc81da](https://github.com/tinogo/uc-intg-stormaudio/commit/4dc81dab16f33ae4c4c2ab3dd69067d9743a0fdc))
* Reduce the code complexity within the media player ([40cc0fa](https://github.com/tinogo/uc-intg-stormaudio/commit/40cc0fa62c29d5b98149684ee6ed8d9d4738d8a1))
* Remove the black package ([c934701](https://github.com/tinogo/uc-intg-stormaudio/commit/c9347012e87d0dca9b3f148e53d635c7a811a5ea))
* Satisfy Pylint ([7fc8847](https://github.com/tinogo/uc-intg-stormaudio/commit/7fc8847151a8c1766b0dfac8e9c61173bde59898))

## [0.8.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.8.0...v0.8.1) (2026-01-01)


### Miscellaneous

* **deps:** bump ucapi-framework from 1.4.0 to 1.4.1 ([#23](https://github.com/tinogo/uc-intg-stormaudio/issues/23)) ([6f5c534](https://github.com/tinogo/uc-intg-stormaudio/commit/6f5c5345164440b85deb655e3fe217c2c43aa6b2))
* **deps:** Update the uv.lock ([b866eb5](https://github.com/tinogo/uc-intg-stormaudio/commit/b866eb5ad9da71c03772994de5737998ae3120c3))
* Use the StormAudioClient instead of instantiating the complete device ([89e9636](https://github.com/tinogo/uc-intg-stormaudio/commit/89e963618755748f8c0e6d17e9f11dd17d56dd05))

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
