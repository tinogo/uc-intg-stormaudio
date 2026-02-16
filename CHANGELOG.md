# Integration Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

_Changes in the next release_

---

## [0.25.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.1...v0.25.2) (2026-02-16)


### Documentation

* Update the project structure ([1858c26](https://github.com/tinogo/uc-intg-stormaudio/commit/1858c266e32164ea044095f735467415ecbf776e))


### Miscellaneous

* **ci-cd:** Update the PyInstaller image ([c90b499](https://github.com/tinogo/uc-intg-stormaudio/commit/c90b499335dfe44651ae84bebc6b8833c7e37ae4))
* **deps:** Update the dependencies ([9347203](https://github.com/tinogo/uc-intg-stormaudio/commit/93472031dd08d963ae0d9b80ae696196a0cc59f9))
* Make documentation updates visible in the changelog ([4d18e86](https://github.com/tinogo/uc-intg-stormaudio/commit/4d18e8660d69118ac9017d4bb542a3c2e1d12f60))

## [0.25.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.0...v0.25.1) (2026-02-15)


### Bug Fixes

* Fix the reporting of the color depth ([0b4b6ad](https://github.com/tinogo/uc-intg-stormaudio/commit/0b4b6add2e7e1657d95cb6fcd029e28f192d86ec))
* Improve the output of the audio stream sensor ([079e009](https://github.com/tinogo/uc-intg-stormaudio/commit/079e009215087062366d1abc60512c63c91a74ec))

## [0.25.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.24.0...v0.25.0) (2026-02-15)


### Features

* **#68:** Add sensors for the current Video Stream ([#108](https://github.com/tinogo/uc-intg-stormaudio/issues/108)) ([124d615](https://github.com/tinogo/uc-intg-stormaudio/commit/124d6159633ab397762fece44a281a22970a84da))

## [0.24.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.23.4...v0.24.0) (2026-02-14)


### Features

* Add asensor which shows the current Dolby Center Spread status ([24a3828](https://github.com/tinogo/uc-intg-stormaudio/commit/24a3828f8a7cb7fe1a0f9ecaa080dc6a7325602a))
* Add SimpleCommands for the Dolby Center Spread ([48e8074](https://github.com/tinogo/uc-intg-stormaudio/commit/48e8074ecdffef58e38391bfe94736be5dd3d860))


### Bug Fixes

* Fix the dolby_center_spread_off simple-command ([26286ed](https://github.com/tinogo/uc-intg-stormaudio/commit/26286ed2b44f5824f8a29567f6752a90662bc5b1))


### Miscellaneous

* **deps:** Update the dependencies ([9f3e00e](https://github.com/tinogo/uc-intg-stormaudio/commit/9f3e00ebe2f32f4d5530b21b328f72b1b4b961d0))
* **deps:** Update uv to version 0.10.0 ([8f35c2c](https://github.com/tinogo/uc-intg-stormaudio/commit/8f35c2c4299d544c70421bb537dc12c80ae9e10b))

## [0.23.4](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.23.3...v0.23.4) (2026-02-07)


### Bug Fixes

* Fix the default names of the decibel-based sensors ([89e08df](https://github.com/tinogo/uc-intg-stormaudio/commit/89e08dfc114294883c32e7625f69159881f965ce))

## [0.23.3](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.23.2...v0.23.3) (2026-02-07)


### Bug Fixes

* Fix the entity states after powering the ISP off ([22dba28](https://github.com/tinogo/uc-intg-stormaudio/commit/22dba284334ada09e6268f260043946d6f3956f3))

## [0.23.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.23.1...v0.23.2) (2026-02-06)


### Bug Fixes

* **#67:** Display a fallback value if there is currently no audio stream ([949ec89](https://github.com/tinogo/uc-intg-stormaudio/commit/949ec89507a0956551c3caa85d83adedb6c5a863))

## [0.23.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.23.0...v0.23.1) (2026-02-06)


### Bug Fixes

* Use the max waiting time when powering off the ISP ([f317fb3](https://github.com/tinogo/uc-intg-stormaudio/commit/f317fb3050b8c80250dd131994a26c6f7ee8db2e))

## [0.23.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.22.2...v0.23.0) (2026-02-06)


### Features

* **#67:** Add a sensor which displays the current audio stream ([db869bd](https://github.com/tinogo/uc-intg-stormaudio/commit/db869bdaac5ea944da95261624a8c1da628085a6))
* Add support for the Dolby virtualizer (Simple Commands, Sensor) ([2471038](https://github.com/tinogo/uc-intg-stormaudio/commit/24710388c23346d46565e73887ac8cee3a57c26a))


### Bug Fixes

* **#98:** Take the allowed upmixer mode into account for the Auro-Matic select- and sensor-entities ([9194865](https://github.com/tinogo/uc-intg-stormaudio/commit/9194865ba0ea2a6b4b3806978c5de25c32cb7d46))


### Miscellaneous

* Fix a typo ([1174ecf](https://github.com/tinogo/uc-intg-stormaudio/commit/1174ecff27e2ae7ae64c81565a9b8fb93790fcbf))

## [0.22.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.22.1...v0.22.2) (2026-02-01)


### Bug Fixes

* Add a debug log for invalid Auro-Matic strength values ([447da03](https://github.com/tinogo/uc-intg-stormaudio/commit/447da03e5c69994be34ce7261821911749654cba))

## [0.22.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.22.0...v0.22.1) (2026-01-31)


### Bug Fixes

* Fix the Auro-Matic strength select entity ([bcdeac9](https://github.com/tinogo/uc-intg-stormaudio/commit/bcdeac90ef72793c801dd81325e587a4928594fc))

## [0.22.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.21.1...v0.22.0) (2026-01-31)


### Features

* **#86:** Add support for Auro-Matic strength selection ([a5d8166](https://github.com/tinogo/uc-intg-stormaudio/commit/a5d8166cc4815fadb3c059b654620147540367a3)), closes [#86](https://github.com/tinogo/uc-intg-stormaudio/issues/86)


### Bug Fixes

* **#98:** apply the first restrictions on the allowed upmixer modes ([9b6c917](https://github.com/tinogo/uc-intg-stormaudio/commit/9b6c91771096b9cce2e05e31d6a17eab42393547))


### Miscellaneous

* **docs:** Update the readme ([345863b](https://github.com/tinogo/uc-intg-stormaudio/commit/345863bbd52187c59cab741d7e28eb901c773ed6))
* **docs:** Update the readme ([0b71325](https://github.com/tinogo/uc-intg-stormaudio/commit/0b71325ca8665df4cd418308f70c565c8ff39545))

## [0.21.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.21.0...v0.21.1) (2026-01-31)


### Bug Fixes

* Fix select attribute updates ([9ba349f](https://github.com/tinogo/uc-intg-stormaudio/commit/9ba349f22d46f4bb457211a37281826b9c16a800))
* Fix the select- and remote-entity attributes ([2f25f55](https://github.com/tinogo/uc-intg-stormaudio/commit/2f25f55b9ba9b97633dc5c102e601db80a34a394))


### Miscellaneous

* Apply some minor code changes ([80518ca](https://github.com/tinogo/uc-intg-stormaudio/commit/80518ca9fcda4432594ac9daf22a6d2d62f5d951))

## [0.21.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.20.0...v0.21.0) (2026-01-31)


### Features

* **#71:** Add select entities for presets and surround-mode ([#91](https://github.com/tinogo/uc-intg-stormaudio/issues/91)) ([053094c](https://github.com/tinogo/uc-intg-stormaudio/commit/053094c0c4dc1e5bf6cb9a8a54920d57622c104c))


### Miscellaneous

* **deps:** Update the dependencies ([aca0c49](https://github.com/tinogo/uc-intg-stormaudio/commit/aca0c49e219fd5f05622ffb32cc901984bbafd97))
* Use keyword args in the media-player again ([0c6243a](https://github.com/tinogo/uc-intg-stormaudio/commit/0c6243a733550da0ddd4fd054ae2122466265d8b))

## [0.20.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.19.2...v0.20.0) (2026-01-26)


### Features

* **#66:** Add a sensor for the current dolby mode ([d4ed8a4](https://github.com/tinogo/uc-intg-stormaudio/commit/d4ed8a4e9b064f4ba1a8220158eb054a441f36fe)), closes [#66](https://github.com/tinogo/uc-intg-stormaudio/issues/66)


### Bug Fixes

* Fix the dB-based sensor state when it has a value of "0" ([1f1f8d5](https://github.com/tinogo/uc-intg-stormaudio/commit/1f1f8d54011dd96b037e1232052cf74d83faed8d))


### Miscellaneous

* Refactor the internals of the Sensor entity ([890563f](https://github.com/tinogo/uc-intg-stormaudio/commit/890563f7516aaf25a47713451aec8483134566ab))
* Remove the create_sensors helper function ([20d1dff](https://github.com/tinogo/uc-intg-stormaudio/commit/20d1dff0353cc2094dd4f8d8d7b985a15d167bfd))

## [0.19.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.19.1...v0.19.2) (2026-01-26)


### Miscellaneous

* Always pull the latest docker images ([960bb7b](https://github.com/tinogo/uc-intg-stormaudio/commit/960bb7b70cdaa28c7663978e9f848f127e4462c6))
* **deps:** Update the UCAPI-Framework to version 1.7.2 ([e0f6424](https://github.com/tinogo/uc-intg-stormaudio/commit/e0f64242f60fb59dffdff682799ef56cd88d0709))
* **docs:** Add the newly added sensors to the readme ([5949f83](https://github.com/tinogo/uc-intg-stormaudio/commit/5949f837b1ed577e339f1d171309f14512783af7))

## [0.19.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.19.0...v0.19.1) (2026-01-24)


### Bug Fixes

* Send fewer commands to the ISP to reduce the load ([2968167](https://github.com/tinogo/uc-intg-stormaudio/commit/29681678703656bcfd7da654bc96b40231d27553))

## [0.19.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.18.0...v0.19.0) (2026-01-24)


### Features

* Add SimpleCommands for Auro-Matic the preset selection ([8704976](https://github.com/tinogo/uc-intg-stormaudio/commit/870497638547a74b8692247a48a5db711c1d0962))
* Add support for various new sensors ([3eb9cc3](https://github.com/tinogo/uc-intg-stormaudio/commit/3eb9cc33c0a904acbf18cd59a2203f9285abb579)), closes [#59](https://github.com/tinogo/uc-intg-stormaudio/issues/59) [#60](https://github.com/tinogo/uc-intg-stormaudio/issues/60) [#61](https://github.com/tinogo/uc-intg-stormaudio/issues/61) [#62](https://github.com/tinogo/uc-intg-stormaudio/issues/62) [#63](https://github.com/tinogo/uc-intg-stormaudio/issues/63) [#64](https://github.com/tinogo/uc-intg-stormaudio/issues/64)


### Bug Fixes

* **#84:** (Hopefully) fix the volume reporting when a maximum volume has been configured in the ISP ([7b0d0ef](https://github.com/tinogo/uc-intg-stormaudio/commit/7b0d0efebca85f1cc0d1d67f2de6d25e51764ee6))
* **docs:** Fix a typo ([af02436](https://github.com/tinogo/uc-intg-stormaudio/commit/af02436604a3ce5942b8fe6efdd31efb034a83da))


### Miscellaneous

* **deps:** Update the UCAPI-Framework to version 1.5.0 ([05333e7](https://github.com/tinogo/uc-intg-stormaudio/commit/05333e765acea7d64b826e63937be69cf4ef89b6))
* **deps:** Update the ucapi-framework to version 1.6.3 ([e170a3b](https://github.com/tinogo/uc-intg-stormaudio/commit/e170a3b0fe1b64e062c77895ac034a7afc0dcc8c))
* **deps:** Update the ucapi-framework to version 1.6.5 ([eb9718b](https://github.com/tinogo/uc-intg-stormaudio/commit/eb9718bae84f7785a5c5f7ff2bcb219be0fe593a))
* **deps:** Update the ucapi-framework to version 1.6.6 ([a119f8e](https://github.com/tinogo/uc-intg-stormaudio/commit/a119f8edad85bbc4c0c79d2dad1efc04f71e851a))
* **docs:** Add a table of contents + missing a sensor to the readme ([778d270](https://github.com/tinogo/uc-intg-stormaudio/commit/778d270da14c9874ebdab206d3bf2c9dc2fcfbb3))
* Drop the custom override regarding the connection handling ([2db7692](https://github.com/tinogo/uc-intg-stormaudio/commit/2db76920907362d2473efd22b86f9d805e722367))
* Extract the device state/attributes into a separate dataclass ([#80](https://github.com/tinogo/uc-intg-stormaudio/issues/80)) ([0a0701e](https://github.com/tinogo/uc-intg-stormaudio/commit/0a0701e1b7c6120a6a932d106f123238948ed09f))
* Fix a deprecation warning ([05505c7](https://github.com/tinogo/uc-intg-stormaudio/commit/05505c7c2f5477b1335a07fae149c86788121885))
* Renamed StormAudioDeviceState to StormAudioDeviceAttributes ([5ccbdd8](https://github.com/tinogo/uc-intg-stormaudio/commit/5ccbdd8d718416868f455a9c0fd2ccfab034935c))
* Use the UCAPI-Framework Entity-class ([#83](https://github.com/tinogo/uc-intg-stormaudio/issues/83)) ([9c629ef](https://github.com/tinogo/uc-intg-stormaudio/commit/9c629ef3473919a541f1682bba82d5212c6d07ba))

## [0.18.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.17.1...v0.18.0) (2026-01-16)


### Features

* **#65:** Add a sensor for "Loudness" ([b9c00ca](https://github.com/tinogo/uc-intg-stormaudio/commit/b9c00ca7501f360d1896d3eff538b1bde93ff425))
* Add a "Current source" sensor ([d1b4ed9](https://github.com/tinogo/uc-intg-stormaudio/commit/d1b4ed99de542e0ca54fa7b32ff1d86f94050b3e))
* Add support for direct source selection via the Remote entity ([3c49460](https://github.com/tinogo/uc-intg-stormaudio/commit/3c49460415bed7583ad6c4fa05025ff2077b185f))


### Miscellaneous

* **docs:** Extend the Readme with more information for the entities ([3c1312e](https://github.com/tinogo/uc-intg-stormaudio/commit/3c1312e8e2d4f1cbfd8f1e7c92176de8610dc20e))

## [0.17.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.17.0...v0.17.1) (2026-01-15)


### Miscellaneous

* **#58:** Optimize emitting the device update events ([#76](https://github.com/tinogo/uc-intg-stormaudio/issues/76)) ([f96d18d](https://github.com/tinogo/uc-intg-stormaudio/commit/f96d18d9ae45ea7fd0b2299e689289b83431cfe9))

## [0.17.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.16.1...v0.17.0) (2026-01-14)


### Features

* Add the entity type suffix to the media player and remote default names ([f642b85](https://github.com/tinogo/uc-intg-stormaudio/commit/f642b854d70001bfa9b093be27a70e8a9bdb24be))

## [0.16.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.16.0...v0.16.1) (2026-01-14)


### Bug Fixes

* Add missing command handlers for some SimpleCommands ([9b1b59c](https://github.com/tinogo/uc-intg-stormaudio/commit/9b1b59c5e67fea2d2e2aab1b747ac3e07d23bfff))

## [0.16.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.15.1...v0.16.0) (2026-01-13)


### Features

* Add a logger for the Remote entity ([222b8cb](https://github.com/tinogo/uc-intg-stormaudio/commit/222b8cb7b6cd5a2d7912dffd378bb74a5b998061))


### Bug Fixes

* Fix sending commands via the Remote Entity ([33a53d0](https://github.com/tinogo/uc-intg-stormaudio/commit/33a53d0e6e9bd1fa8cc17a5908a33554892b1c0e))


### Miscellaneous

* **deps:** Update the dependencies ([77271a1](https://github.com/tinogo/uc-intg-stormaudio/commit/77271a16cead5b89ad8d6540fb9fd671d415eff1))
* Initialize all logers ([d6bc2c5](https://github.com/tinogo/uc-intg-stormaudio/commit/d6bc2c5888ec11d7f7fee0c1a36734f5a5360c70))
* Remove the network_mode property from the compose.yml ([af6a2ea](https://github.com/tinogo/uc-intg-stormaudio/commit/af6a2eae2a0edd26d8f2ac6034d70f1802561898))

## [0.15.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.15.0...v0.15.1) (2026-01-11)


### Bug Fixes

* **ci:** Fix the build ([57cf270](https://github.com/tinogo/uc-intg-stormaudio/commit/57cf27064a9d24d62dc066a1d8e8adf02d38acff))

## [0.15.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.14.0...v0.15.0) (2026-01-11)


### Features

* **#47:** Add Remote entity ([#56](https://github.com/tinogo/uc-intg-stormaudio/issues/56)) ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))


### Bug Fixes

* Fixed waiting for the volume response. This should hopefully fix the volume slider's behavior ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))
* Renamed all "Simple Commands", so that they adhere to the restrictions given by the Unfoldedcircle API-Docs ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))


### Miscellaneous

* separate the StormIntegrationDriver from the main entrypoint ([a42bd91](https://github.com/tinogo/uc-intg-stormaudio/commit/a42bd91f5fd5dfe2813471941f4869088a053463))

## [0.14.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.13.2...v0.14.0) (2026-01-10)


### Features

* **#42:** Add support for a "Current preset" sensor ([#54](https://github.com/tinogo/uc-intg-stormaudio/issues/54)) ([fcef3aa](https://github.com/tinogo/uc-intg-stormaudio/commit/fcef3aa0ef8409d58cef238d72ba30bd4497514f))


### Bug Fixes

* **#51:** Persist the sources in the device config ([#52](https://github.com/tinogo/uc-intg-stormaudio/issues/52)) ([9aed792](https://github.com/tinogo/uc-intg-stormaudio/commit/9aed79222f741d90bda669bce8d003c5646fd5e0))

## [0.13.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.13.1...v0.13.2) (2026-01-09)


### Bug Fixes

* Prevent multiple connections to the ISP ([ca78214](https://github.com/tinogo/uc-intg-stormaudio/commit/ca7821474fbd03e183b18eed8559fcf3414e4971))


### Miscellaneous

* **#26:** Add pre-commit hooks ([#48](https://github.com/tinogo/uc-intg-stormaudio/issues/48)) ([a7d4531](https://github.com/tinogo/uc-intg-stormaudio/commit/a7d4531b8b15c7b7043b98fe9fc3f0220484b2ec))
* **#45:** Differentiate between the device states and entity states ([#50](https://github.com/tinogo/uc-intg-stormaudio/issues/50)) ([23dd333](https://github.com/tinogo/uc-intg-stormaudio/commit/23dd333a50dca3bbbd21803c585e7f0ab948c9c1)), closes [#45](https://github.com/tinogo/uc-intg-stormaudio/issues/45)
* Improve the wording of a comment ([85abfc3](https://github.com/tinogo/uc-intg-stormaudio/commit/85abfc3b6d12e3f05964124122addc171011c579))
* Reduce the cyclomatic complexity of retrieving the the entity attributes ([b9c2317](https://github.com/tinogo/uc-intg-stormaudio/commit/b9c231760ecda8c53eddd5b36d3343fa4a0d01f0))
* use a StringEnum for the StormAudioStates ([c50112f](https://github.com/tinogo/uc-intg-stormaudio/commit/c50112fc8411a486d87092117ea6db368e9b73cc))

## [0.13.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.13.0...v0.13.1) (2026-01-08)


### Bug Fixes

* Fix the sound mode media_player attribute ([466ba4e](https://github.com/tinogo/uc-intg-stormaudio/commit/466ba4e16b347838bcf255e516ea99fdc7f284e3))
* Fix the StormXT sensor data ([e0d626b](https://github.com/tinogo/uc-intg-stormaudio/commit/e0d626b8e1ccaa7e411c23093fed05355229e7c1))


### Miscellaneous

* Use EAFP-approach to check the existence of a key ([561a8f4](https://github.com/tinogo/uc-intg-stormaudio/commit/561a8f4dff886bb620ef3f05f9edd50d2c2028cd))

## [0.13.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.12.0...v0.13.0) (2026-01-08)


### Features

* Add the current source to the media_player attributes ([baebe33](https://github.com/tinogo/uc-intg-stormaudio/commit/baebe338154087cd274cb66b2041953b4ecd209b))


### Miscellaneous

* Optimize building the initial sensor attributes ([1628fdc](https://github.com/tinogo/uc-intg-stormaudio/commit/1628fdc3bd10bca0eab779a8a4537228d305b200))

## [0.12.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.11.0...v0.12.0) (2026-01-08)


### Features

* Publish the current sound mode to the media player attributes, too ([015fb2b](https://github.com/tinogo/uc-intg-stormaudio/commit/015fb2b4566b95ca345f21fa9b0e4cfc87fbaea2))

## [0.11.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.10.5...v0.11.0) (2026-01-08)


### Features

* **#6:** Add support for sensors ([#40](https://github.com/tinogo/uc-intg-stormaudio/issues/40)) ([1b13f70](https://github.com/tinogo/uc-intg-stormaudio/commit/1b13f709e425c29ac53997c68dc6c56dd07cc674)), closes [#6](https://github.com/tinogo/uc-intg-stormaudio/issues/6)

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
