# Integration Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

_Changes in the next release_

---

## [0.27.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.26.3...v0.27.0) (2026-09-05)


### Features

* **#1:** Introduce Google Release please ([61c36da](https://github.com/tinogo/uc-intg-stormaudio/commit/61c36dac922a6a3133c04119ad02ee4308c8c124))
* **#1:** Rely solely on Google Release Please ([6a5a78d](https://github.com/tinogo/uc-intg-stormaudio/commit/6a5a78dbd8f36964fe34fd4b55389454dd95cb63))
* **#2:** add and configure dependabot ([66812b5](https://github.com/tinogo/uc-intg-stormaudio/commit/66812b59ff704b05932e00aa1b5974c7fd317307)), closes [#2](https://github.com/tinogo/uc-intg-stormaudio/issues/2)
* **#3:** Add a proper connection check to the setup flow ([#20](https://github.com/tinogo/uc-intg-stormaudio/issues/20)) ([f548a92](https://github.com/tinogo/uc-intg-stormaudio/commit/f548a9281fe838d4af14d2c0826c2e670fd83780))
* **#42:** Add support for a "Current preset" sensor ([#54](https://github.com/tinogo/uc-intg-stormaudio/issues/54)) ([fcef3aa](https://github.com/tinogo/uc-intg-stormaudio/commit/fcef3aa0ef8409d58cef238d72ba30bd4497514f))
* **#47:** Add Remote entity ([#56](https://github.com/tinogo/uc-intg-stormaudio/issues/56)) ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))
* **#4:** re-enable mDNS auto-discovery and try to use another mDNS name ([1f78279](https://github.com/tinogo/uc-intg-stormaudio/commit/1f78279f66277209db4ef78ed6d3ce149f62aaf7))
* **#5:** Prepare the Zone-Management ([3e0798b](https://github.com/tinogo/uc-intg-stormaudio/commit/3e0798b0593326485ae523107d288c4c6fbd9dfa))
* **#65:** Add a sensor for "Loudness" ([b9c00ca](https://github.com/tinogo/uc-intg-stormaudio/commit/b9c00ca7501f360d1896d3eff538b1bde93ff425))
* **#66:** Add a sensor for the current dolby mode ([d4ed8a4](https://github.com/tinogo/uc-intg-stormaudio/commit/d4ed8a4e9b064f4ba1a8220158eb054a441f36fe)), closes [#66](https://github.com/tinogo/uc-intg-stormaudio/issues/66)
* **#67:** Add a sensor which displays the current audio stream ([db869bd](https://github.com/tinogo/uc-intg-stormaudio/commit/db869bdaac5ea944da95261624a8c1da628085a6))
* **#68:** Add sensors for the current Video Stream ([#108](https://github.com/tinogo/uc-intg-stormaudio/issues/108)) ([124d615](https://github.com/tinogo/uc-intg-stormaudio/commit/124d6159633ab397762fece44a281a22970a84da))
* **#6:** Add support for sensors ([#40](https://github.com/tinogo/uc-intg-stormaudio/issues/40)) ([1b13f70](https://github.com/tinogo/uc-intg-stormaudio/commit/1b13f709e425c29ac53997c68dc6c56dd07cc674)), closes [#6](https://github.com/tinogo/uc-intg-stormaudio/issues/6)
* **#71:** Add select entities for presets and surround-mode ([#91](https://github.com/tinogo/uc-intg-stormaudio/issues/91)) ([053094c](https://github.com/tinogo/uc-intg-stormaudio/commit/053094c0c4dc1e5bf6cb9a8a54920d57622c104c))
* **#7:** add center enhance, surround enhance and LFE enhance commands ([3f2449c](https://github.com/tinogo/uc-intg-stormaudio/commit/3f2449cff82f3cf47eda65474ec9ff11aae941b2))
* **#7:** add dolby mode commands ([5e89ab7](https://github.com/tinogo/uc-intg-stormaudio/commit/5e89ab7fccd14a9e62c6d01178f9cbb6c8957b1e))
* **#86:** Add support for Auro-Matic strength selection ([a5d8166](https://github.com/tinogo/uc-intg-stormaudio/commit/a5d8166cc4815fadb3c059b654620147540367a3)), closes [#86](https://github.com/tinogo/uc-intg-stormaudio/issues/86)
* Add a "Current source" sensor ([d1b4ed9](https://github.com/tinogo/uc-intg-stormaudio/commit/d1b4ed99de542e0ca54fa7b32ff1d86f94050b3e))
* Add a logger for the Remote entity ([222b8cb](https://github.com/tinogo/uc-intg-stormaudio/commit/222b8cb7b6cd5a2d7912dffd378bb74a5b998061))
* Add asensor which shows the current Dolby Center Spread status ([24a3828](https://github.com/tinogo/uc-intg-stormaudio/commit/24a3828f8a7cb7fe1a0f9ecaa080dc6a7325602a))
* Add device discovery to the setup flow ([138c564](https://github.com/tinogo/uc-intg-stormaudio/commit/138c5641c5b4c3242181f49eef882662552b6fde))
* Add DPAD handling ([6dcb802](https://github.com/tinogo/uc-intg-stormaudio/commit/6dcb8025fa2363d9d79cedb17107a16dfda7d46b))
* Add mute, unmute and mute toggle ([dca05ad](https://github.com/tinogo/uc-intg-stormaudio/commit/dca05ad6bdfae4807b736dfef7c8a0ef1b846fab))
* Add preset handling ([bd51bb7](https://github.com/tinogo/uc-intg-stormaudio/commit/bd51bb74804477c7258b925b728385dcc18e08ac))
* Add simple commands for bass, treble and brightness ([e6ca763](https://github.com/tinogo/uc-intg-stormaudio/commit/e6ca76328980c046227f00c0d1e30cdb5dd3e20c))
* Add simple commands for the loudness handling ([4e42b0c](https://github.com/tinogo/uc-intg-stormaudio/commit/4e42b0cc6a604f5f594790627fb8ec0392d47ba6))
* Add SimpleCommands for Auro-Matic the preset selection ([8704976](https://github.com/tinogo/uc-intg-stormaudio/commit/870497638547a74b8692247a48a5db711c1d0962))
* Add SimpleCommands for the Dolby Center Spread ([48e8074](https://github.com/tinogo/uc-intg-stormaudio/commit/48e8074ecdffef58e38391bfe94736be5dd3d860))
* Add some translations + use a better fitting icon ([3b3b4e4](https://github.com/tinogo/uc-intg-stormaudio/commit/3b3b4e42d342fc7e72fe295638edcba67c9fbe72))
* Add source list + input switching support ([833c4c3](https://github.com/tinogo/uc-intg-stormaudio/commit/833c4c36e074afa261384afe7b4b2e8956454469))
* Add support for direct source selection via the Remote entity ([3c49460](https://github.com/tinogo/uc-intg-stormaudio/commit/3c49460415bed7583ad6c4fa05025ff2077b185f))
* Add support for the Dolby virtualizer (Simple Commands, Sensor) ([2471038](https://github.com/tinogo/uc-intg-stormaudio/commit/24710388c23346d46565e73887ac8cee3a57c26a))
* Add support for various new sensors ([3eb9cc3](https://github.com/tinogo/uc-intg-stormaudio/commit/3eb9cc33c0a904acbf18cd59a2203f9285abb579)), closes [#59](https://github.com/tinogo/uc-intg-stormaudio/issues/59) [#60](https://github.com/tinogo/uc-intg-stormaudio/issues/60) [#61](https://github.com/tinogo/uc-intg-stormaudio/issues/61) [#62](https://github.com/tinogo/uc-intg-stormaudio/issues/62) [#63](https://github.com/tinogo/uc-intg-stormaudio/issues/63) [#64](https://github.com/tinogo/uc-intg-stormaudio/issues/64)
* Add the current source to the media_player attributes ([baebe33](https://github.com/tinogo/uc-intg-stormaudio/commit/baebe338154087cd274cb66b2041953b4ecd209b))
* Add the entity type suffix to the media player and remote default names ([f642b85](https://github.com/tinogo/uc-intg-stormaudio/commit/f642b854d70001bfa9b093be27a70e8a9bdb24be))
* Add the sound mode command ([b2620c4](https://github.com/tinogo/uc-intg-stormaudio/commit/b2620c46a7ebd47b29f6545993bf959635ca1638))
* Add volume up and volume down ([18a3e09](https://github.com/tinogo/uc-intg-stormaudio/commit/18a3e0970d6e7cd39346218136f2b48cc52167b3))
* begin to build out the MediaPlayer class ([8fb0eda](https://github.com/tinogo/uc-intg-stormaudio/commit/8fb0edaff1b76d23a206e2ca45854caad71ae8e8))
* **ci-cd:** Create the release in parallel to the docker container build step ([2e788b6](https://github.com/tinogo/uc-intg-stormaudio/commit/2e788b62229867c670fb54a89f5bd1bc00620fea))
* **ci-cd:** use a ARM-native CI-runner to build the artifact ([c5dabaa](https://github.com/tinogo/uc-intg-stormaudio/commit/c5dabaa3ccb84188d6e8816fec9c3c87a9631911))
* **ci:** Add actionlint and PR-title linter ([cfde9ff](https://github.com/tinogo/uc-intg-stormaudio/commit/cfde9ffad1e8bd0b51ec33d4f6a632a58337b3a1))
* **ci:** Check the code against flake8 ([#28](https://github.com/tinogo/uc-intg-stormaudio/issues/28)) ([be69f78](https://github.com/tinogo/uc-intg-stormaudio/commit/be69f78a8ef95f15e43925c6966b36f5ee342d45))
* configure automatic device discovery ([1255c79](https://github.com/tinogo/uc-intg-stormaudio/commit/1255c79f82b48818dd8188d2d20ce42111fac20f))
* Customize build Github workflow ([b9a0338](https://github.com/tinogo/uc-intg-stormaudio/commit/b9a033855d8dceaa7e6f12e67f8a9c69235a2de4))
* Customize the driver.json ([bac5d23](https://github.com/tinogo/uc-intg-stormaudio/commit/bac5d231cf922a15aaf26dca60487cd72043f1dc))
* Disable the auto discovery for now ([74fb58b](https://github.com/tinogo/uc-intg-stormaudio/commit/74fb58bc48ab7dc98a99fe4f8b985eb49a6d878b))
* Implement the power on and power off methods ([70ba860](https://github.com/tinogo/uc-intg-stormaudio/commit/70ba860aa4c9150174918ceb0e8aaa77f0b8ff24))
* Implement the power_toggle method ([aa0dfa7](https://github.com/tinogo/uc-intg-stormaudio/commit/aa0dfa723e6df557a5cf06a517b0e32da47ad3dd))
* Make the establishing the connection even more robust ([5dcde83](https://github.com/tinogo/uc-intg-stormaudio/commit/5dcde83aca03ea887c3ae3212526a014c47be4ae))
* move the port config into the Config-class ([56b6ae0](https://github.com/tinogo/uc-intg-stormaudio/commit/56b6ae0c02746e18b90005c1c52e66f2e49d4c01))
* optimize various methods to wait for their command responses ([9689461](https://github.com/tinogo/uc-intg-stormaudio/commit/96894618713f624dc477b9636619ea68fbfc76a4))
* Publish the current sound mode to the media player attributes, too ([015fb2b](https://github.com/tinogo/uc-intg-stormaudio/commit/015fb2b4566b95ca345f21fa9b0e4cfc87fbaea2))
* Reintroduce the volume feature ([78a95b2](https://github.com/tinogo/uc-intg-stormaudio/commit/78a95b27dbc023096bd502260ec3d5c9759b8794))
* Remove the auto-discovery for now + only require the IP address ([2b37d72](https://github.com/tinogo/uc-intg-stormaudio/commit/2b37d720ca253ea913501e0a171aa261712c7866))
* Restrict the Loggers to specific types ([46906bb](https://github.com/tinogo/uc-intg-stormaudio/commit/46906bb5c149f847a89f1d9f9b3e0e890a938117))
* use the PersistentConnectionDevice for StormAudio devices ([edff6e8](https://github.com/tinogo/uc-intg-stormaudio/commit/edff6e84e6e1fdaeaccfd585c064f025eb1ca6ee))
* Wait for the response after selecting the input source ([265d11c](https://github.com/tinogo/uc-intg-stormaudio/commit/265d11cbc14255b5fc6aa216ec3fbda5deacb1a3))


### Bug Fixes

* **#1:** Fix the artifact name ([1dd6058](https://github.com/tinogo/uc-intg-stormaudio/commit/1dd605880f92cc1202497aeef22b46cb42d4adab))
* **#51:** Persist the sources in the device config ([#52](https://github.com/tinogo/uc-intg-stormaudio/issues/52)) ([9aed792](https://github.com/tinogo/uc-intg-stormaudio/commit/9aed79222f741d90bda669bce8d003c5646fd5e0))
* **#67:** Display a fallback value if there is currently no audio stream ([949ec89](https://github.com/tinogo/uc-intg-stormaudio/commit/949ec89507a0956551c3caa85d83adedb6c5a863))
* **#84:** (Hopefully) fix the volume reporting when a maximum volume has been configured in the ISP ([7b0d0ef](https://github.com/tinogo/uc-intg-stormaudio/commit/7b0d0efebca85f1cc0d1d67f2de6d25e51764ee6))
* **#8:** Fix device initialization ([#29](https://github.com/tinogo/uc-intg-stormaudio/issues/29)) ([9308398](https://github.com/tinogo/uc-intg-stormaudio/commit/93083988d3032ac18a3b164a60423c936c486219))
* **#8:** Revert the multiple connections prevention ([1730c6e](https://github.com/tinogo/uc-intg-stormaudio/commit/1730c6effc3918a948009b57d8fc8ad8e59e0c9a))
* **#98:** apply the first restrictions on the allowed upmixer modes ([9b6c917](https://github.com/tinogo/uc-intg-stormaudio/commit/9b6c91771096b9cce2e05e31d6a17eab42393547))
* **#98:** Take the allowed upmixer mode into account for the Auro-Matic select- and sensor-entities ([9194865](https://github.com/tinogo/uc-intg-stormaudio/commit/9194865ba0ea2a6b4b3806978c5de25c32cb7d46))
* Add a debug log for invalid Auro-Matic strength values ([447da03](https://github.com/tinogo/uc-intg-stormaudio/commit/447da03e5c69994be34ce7261821911749654cba))
* add a missing Response constant ([9bce8ad](https://github.com/tinogo/uc-intg-stormaudio/commit/9bce8ad103fb88608502f7cb5c79c3d3e5e329ce))
* Add missing command handlers for some SimpleCommands ([9b1b59c](https://github.com/tinogo/uc-intg-stormaudio/commit/9b1b59c5e67fea2d2e2aab1b747ac3e07d23bfff))
* **ci-cd:** Fix creating the Github release (hopefully) ([a6866b5](https://github.com/tinogo/uc-intg-stormaudio/commit/a6866b5c8038de4b2a9c5057cf338dfeb6f5a1c5))
* **ci-cd:** maybe this time... ([c43818b](https://github.com/tinogo/uc-intg-stormaudio/commit/c43818b7a9cf888bbdf4511b5c521b96e1c0179a))
* **ci-cd:** Move the artifact_name var extract into a differen job ([eea7173](https://github.com/tinogo/uc-intg-stormaudio/commit/eea7173083cc9c9689e5396268b7c629735b9cce))
* **ci-cd:** Use the correct job-id ([fb43f47](https://github.com/tinogo/uc-intg-stormaudio/commit/fb43f4760c95fbef6a2c698c94990aba7585bdee))
* **ci:** Fix the build ([57cf270](https://github.com/tinogo/uc-intg-stormaudio/commit/57cf27064a9d24d62dc066a1d8e8adf02d38acff))
* **ci:** Only check the unsorted imports in the CI-env, but don't fix them ([bd5ba89](https://github.com/tinogo/uc-intg-stormaudio/commit/bd5ba8957f64a3edc1812fe6972518fc8df69bcd))
* **ci:** Restrict the permissions in the CI-pipeline a bit ([6638550](https://github.com/tinogo/uc-intg-stormaudio/commit/66385509f09cab8cd7e3eb3afa108a425b6bcbd2))
* **ci:** Satisfy actionlint ([#17](https://github.com/tinogo/uc-intg-stormaudio/issues/17)) ([cd03acb](https://github.com/tinogo/uc-intg-stormaudio/commit/cd03acb1df824c44533cb7b3a638ec470167c889))
* **deps:** Update the requirements.txt ([d1f0f0c](https://github.com/tinogo/uc-intg-stormaudio/commit/d1f0f0cdff99e4a7698efd00db160b43c4db51e5))
* **docs:** Fix a typo ([af02436](https://github.com/tinogo/uc-intg-stormaudio/commit/af02436604a3ce5942b8fe6efdd31efb034a83da))
* **docs:** Fix the coding guidelines ([430870f](https://github.com/tinogo/uc-intg-stormaudio/commit/430870fbc94f7aeeb950c56293e6638b53bfa8ee))
* Emit only a single event after building the source_list ([a1abc01](https://github.com/tinogo/uc-intg-stormaudio/commit/a1abc01893189e8aa36a019906dbd5d29de0c291))
* Fix select attribute updates ([9ba349f](https://github.com/tinogo/uc-intg-stormaudio/commit/9ba349f22d46f4bb457211a37281826b9c16a800))
* Fix sending commands via the Remote Entity ([33a53d0](https://github.com/tinogo/uc-intg-stormaudio/commit/33a53d0e6e9bd1fa8cc17a5908a33554892b1c0e))
* Fix the Auro-Matic strength select entity ([bcdeac9](https://github.com/tinogo/uc-intg-stormaudio/commit/bcdeac90ef72793c801dd81325e587a4928594fc))
* Fix the dB-based sensor state when it has a value of "0" ([1f1f8d5](https://github.com/tinogo/uc-intg-stormaudio/commit/1f1f8d54011dd96b037e1232052cf74d83faed8d))
* Fix the default names of the decibel-based sensors ([89e08df](https://github.com/tinogo/uc-intg-stormaudio/commit/89e08dfc114294883c32e7625f69159881f965ce))
* fix the dependabot config for updating github actions ([058d0fd](https://github.com/tinogo/uc-intg-stormaudio/commit/058d0fd4cd6b916af5186fcec5f6b4016522f605))
* Fix the dolby_center_spread_off simple-command ([26286ed](https://github.com/tinogo/uc-intg-stormaudio/commit/26286ed2b44f5824f8a29567f6752a90662bc5b1))
* Fix the entity states after powering the ISP off ([22dba28](https://github.com/tinogo/uc-intg-stormaudio/commit/22dba284334ada09e6268f260043946d6f3956f3))
* Fix the media player entity power state ([2c6c704](https://github.com/tinogo/uc-intg-stormaudio/commit/2c6c7045aca68738052edcf191d629c73d0e7ba6))
* Fix the reporting of the color depth ([0b4b6ad](https://github.com/tinogo/uc-intg-stormaudio/commit/0b4b6add2e7e1657d95cb6fcd029e28f192d86ec))
* Fix the select- and remote-entity attributes ([2f25f55](https://github.com/tinogo/uc-intg-stormaudio/commit/2f25f55b9ba9b97633dc5c102e601db80a34a394))
* Fix the sound mode media_player attribute ([466ba4e](https://github.com/tinogo/uc-intg-stormaudio/commit/466ba4e16b347838bcf255e516ea99fdc7f284e3))
* Fix the StormXT sensor data ([e0d626b](https://github.com/tinogo/uc-intg-stormaudio/commit/e0d626b8e1ccaa7e411c23093fed05355229e7c1))
* Fixed waiting for the volume response. This should hopefully fix the volume slider's behavior ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))
* Force a connection to the device during entity registration ([48568dc](https://github.com/tinogo/uc-intg-stormaudio/commit/48568dc01786f5e78b0cbfa9b710fd09eee0bc87))
* gracefully handle TCP-Connection errors in close_connection ([fd31ebd](https://github.com/tinogo/uc-intg-stormaudio/commit/fd31ebd0d82a16c7036d1791950da104b652e432))
* Improve the output of the audio stream sensor ([079e009](https://github.com/tinogo/uc-intg-stormaudio/commit/079e009215087062366d1abc60512c63c91a74ec))
* Prevent multiple connections to the ISP ([ca78214](https://github.com/tinogo/uc-intg-stormaudio/commit/ca7821474fbd03e183b18eed8559fcf3414e4971))
* Prevent restarts of the integration container for changes to the config.json file ([c0fbb22](https://github.com/tinogo/uc-intg-stormaudio/commit/c0fbb227fa18c05dfece00b5a7c3a5de9e725b48))
* Reduce the maximum timeout for the power-on command ([#39](https://github.com/tinogo/uc-intg-stormaudio/issues/39)) ([6912372](https://github.com/tinogo/uc-intg-stormaudio/commit/691237260c0cb433d5db02350bea70f56cc32f31))
* Renamed all "Simple Commands", so that they adhere to the restrictions given by the Unfoldedcircle API-Docs ([a99d6dc](https://github.com/tinogo/uc-intg-stormaudio/commit/a99d6dcd912891b3581b55b960ebf7fd5853bf5a))
* Send fewer commands to the ISP to reduce the load ([2968167](https://github.com/tinogo/uc-intg-stormaudio/commit/29681678703656bcfd7da654bc96b40231d27553))
* Use the max waiting time when powering off the ISP ([f317fb3](https://github.com/tinogo/uc-intg-stormaudio/commit/f317fb3050b8c80250dd131994a26c6f7ee8db2e))


### Documentation

* document how to update a single package ([3754088](https://github.com/tinogo/uc-intg-stormaudio/commit/375408817367e0546a8c2f2b7e6fea99d7eb2d03))
* Extend the docker compose command ([8bf0ea1](https://github.com/tinogo/uc-intg-stormaudio/commit/8bf0ea1746fae6bd3b723077b7d7ed69101c17eb))
* fix some typos ([2388443](https://github.com/tinogo/uc-intg-stormaudio/commit/2388443d9f597fcee56dae8be2a6bb2c15516beb))
* remove a non-existing file from the README.md ([da7dc39](https://github.com/tinogo/uc-intg-stormaudio/commit/da7dc39104844f07a33a10169d991905d1b5c5b5))
* Update the coding guidelines ([78b524b](https://github.com/tinogo/uc-intg-stormaudio/commit/78b524bddfd85384b599aa8d46ef8688977906e5))
* Update the project structure ([1858c26](https://github.com/tinogo/uc-intg-stormaudio/commit/1858c266e32164ea044095f735467415ecbf776e))
* Update the readme ([b5d4a10](https://github.com/tinogo/uc-intg-stormaudio/commit/b5d4a105813e246709d87c51938e6a4092996d30))
* Update the README ([1fb58e3](https://github.com/tinogo/uc-intg-stormaudio/commit/1fb58e32a9675ce08a400109deabea7db19dbaa9))
* Update the README ([ce678ec](https://github.com/tinogo/uc-intg-stormaudio/commit/ce678ec6cfca0a1f1619bae905f603bc4c7bd336))
* Update the README once more ([92342b9](https://github.com/tinogo/uc-intg-stormaudio/commit/92342b95b6c931a46eecc58a712d22f681dce95e))


### Miscellaneous

* **#26:** Add pre-commit hooks ([#48](https://github.com/tinogo/uc-intg-stormaudio/issues/48)) ([a7d4531](https://github.com/tinogo/uc-intg-stormaudio/commit/a7d4531b8b15c7b7043b98fe9fc3f0220484b2ec))
* **#45:** Differentiate between the device states and entity states ([#50](https://github.com/tinogo/uc-intg-stormaudio/issues/50)) ([23dd333](https://github.com/tinogo/uc-intg-stormaudio/commit/23dd333a50dca3bbbd21803c585e7f0ab948c9c1)), closes [#45](https://github.com/tinogo/uc-intg-stormaudio/issues/45)
* **#58:** Optimize emitting the device update events ([#76](https://github.com/tinogo/uc-intg-stormaudio/issues/76)) ([f96d18d](https://github.com/tinogo/uc-intg-stormaudio/commit/f96d18d9ae45ea7fd0b2299e689289b83431cfe9))
* Always pull the latest docker images ([960bb7b](https://github.com/tinogo/uc-intg-stormaudio/commit/960bb7b70cdaa28c7663978e9f848f127e4462c6))
* Apply some minor code changes ([80518ca](https://github.com/tinogo/uc-intg-stormaudio/commit/80518ca9fcda4432594ac9daf22a6d2d62f5d951))
* Build the entity_id once ([bf84dc0](https://github.com/tinogo/uc-intg-stormaudio/commit/bf84dc0036e14d3ce6df17c2f5ec7713f93118e7))
* **ci-cd:** optimize building the integration ([b8ef902](https://github.com/tinogo/uc-intg-stormaudio/commit/b8ef9022ef174668380e6754ff888bc89485bdc6))
* **ci-cd:** Update the PyInstaller image ([c90b499](https://github.com/tinogo/uc-intg-stormaudio/commit/c90b499335dfe44651ae84bebc6b8833c7e37ae4))
* **ci:** Lint the code against Pylint within the CI-Pipeline ([2f5f57c](https://github.com/tinogo/uc-intg-stormaudio/commit/2f5f57c7845add11b46819715df56c15356cdee1))
* consistently use positional parameters in the media_player ([b555e1a](https://github.com/tinogo/uc-intg-stormaudio/commit/b555e1a388f9b1b468703e499683ecd075d6db10))
* Delete the uv.lock ([0025639](https://github.com/tinogo/uc-intg-stormaudio/commit/0025639c99e09b6c2330c7d159a91cc2b65f4b50))
* **deps:** Add requirements for uv ([9236aa5](https://github.com/tinogo/uc-intg-stormaudio/commit/9236aa57635f98e943ab199644800421c73f00f2))
* **deps:** bump actions/checkout from 4 to 6 ([#9](https://github.com/tinogo/uc-intg-stormaudio/issues/9)) ([53a27a0](https://github.com/tinogo/uc-intg-stormaudio/commit/53a27a06a576609365f345e2613b24e3fc770e92))
* **deps:** bump actions/checkout from 6 to 7 in /.github/workflows ([#144](https://github.com/tinogo/uc-intg-stormaudio/issues/144)) ([bdc57f7](https://github.com/tinogo/uc-intg-stormaudio/commit/bdc57f7e427bc64187a527e42a9d921829566379))
* **deps:** bump actions/download-artifact from 4 to 7 ([#11](https://github.com/tinogo/uc-intg-stormaudio/issues/11)) ([dfca9e8](https://github.com/tinogo/uc-intg-stormaudio/commit/dfca9e81888dd82972cd6f90508e1d75a775cbb9))
* **deps:** bump actions/setup-python from 6 to 7 in /.github/workflows ([#148](https://github.com/tinogo/uc-intg-stormaudio/issues/148)) ([f524ae0](https://github.com/tinogo/uc-intg-stormaudio/commit/f524ae0962f6c9ed6a2cedefd36180b528ffb7ee))
* **deps:** bump actions/upload-artifact from 4 to 6 ([#10](https://github.com/tinogo/uc-intg-stormaudio/issues/10)) ([ef5f855](https://github.com/tinogo/uc-intg-stormaudio/commit/ef5f855eeb0938f482a031ecd2a6c018e1b6adf9))
* **deps:** bump aiohttp from 3.13.2 to 3.13.3 ([#30](https://github.com/tinogo/uc-intg-stormaudio/issues/30)) ([06cbfd4](https://github.com/tinogo/uc-intg-stormaudio/commit/06cbfd49d2bc6c6d83455d1761c34d272ec4903a))
* **deps:** bump docker/build-push-action from 5 to 6 ([#12](https://github.com/tinogo/uc-intg-stormaudio/issues/12)) ([c5dd763](https://github.com/tinogo/uc-intg-stormaudio/commit/c5dd76314f9869ddcbe2fd542af22716834e2e75))
* **deps:** bump googleapis/release-please-action from 4 to 5 ([#126](https://github.com/tinogo/uc-intg-stormaudio/issues/126)) ([c4d74f4](https://github.com/tinogo/uc-intg-stormaudio/commit/c4d74f413f2e2603f42732703bc7a513abaec657))
* **deps:** bump ucapi-framework from 1.4.0 to 1.4.1 ([#23](https://github.com/tinogo/uc-intg-stormaudio/issues/23)) ([6f5c534](https://github.com/tinogo/uc-intg-stormaudio/commit/6f5c5345164440b85deb655e3fe217c2c43aa6b2))
* **deps:** let dependabot update the uv.lock ([6f6e302](https://github.com/tinogo/uc-intg-stormaudio/commit/6f6e302d47f18577f4ee5e586151f612c4c7ed47))
* **deps:** Update integration for 1.4.2 ucapi-framework ([#33](https://github.com/tinogo/uc-intg-stormaudio/issues/33)) ([d42f89f](https://github.com/tinogo/uc-intg-stormaudio/commit/d42f89f46e21d96db39b2ad241bf22ec91712ac2))
* **deps:** Update the dependencies ([33b9887](https://github.com/tinogo/uc-intg-stormaudio/commit/33b988747f2a9414451922c87dad1226954287a5))
* **deps:** Update the dependencies ([5ab1af8](https://github.com/tinogo/uc-intg-stormaudio/commit/5ab1af892afa7d4f5d5adff4682a73d3e2e1e7a2))
* **deps:** Update the dependencies ([d1e12b5](https://github.com/tinogo/uc-intg-stormaudio/commit/d1e12b5d1211369647e21ee70725ff2cdcb42d76))
* **deps:** Update the dependencies ([bdf7634](https://github.com/tinogo/uc-intg-stormaudio/commit/bdf7634a4ed9d041bb28c70f8c1de11e9ca1c0a4))
* **deps:** Update the dependencies ([5c1d809](https://github.com/tinogo/uc-intg-stormaudio/commit/5c1d809eb2e891f4fd592a1ca8b1b61b250a7065))
* **deps:** Update the dependencies ([9347203](https://github.com/tinogo/uc-intg-stormaudio/commit/93472031dd08d963ae0d9b80ae696196a0cc59f9))
* **deps:** Update the dependencies ([9f3e00e](https://github.com/tinogo/uc-intg-stormaudio/commit/9f3e00ebe2f32f4d5530b21b328f72b1b4b961d0))
* **deps:** Update the dependencies ([aca0c49](https://github.com/tinogo/uc-intg-stormaudio/commit/aca0c49e219fd5f05622ffb32cc901984bbafd97))
* **deps:** Update the dependencies ([77271a1](https://github.com/tinogo/uc-intg-stormaudio/commit/77271a16cead5b89ad8d6540fb9fd671d415eff1))
* **deps:** update the r2-pyinstaller docker image ([cdafb97](https://github.com/tinogo/uc-intg-stormaudio/commit/cdafb979a573832ad43de7917ee919fdf8aa420b))
* **deps:** Update the required uv version to 0.12.7 ([c2a4c73](https://github.com/tinogo/uc-intg-stormaudio/commit/c2a4c7382e5fedc90365189a506387d162f6422d))
* **deps:** Update the UCAPI-Framework to version 1.5.0 ([05333e7](https://github.com/tinogo/uc-intg-stormaudio/commit/05333e765acea7d64b826e63937be69cf4ef89b6))
* **deps:** Update the ucapi-framework to version 1.6.3 ([e170a3b](https://github.com/tinogo/uc-intg-stormaudio/commit/e170a3b0fe1b64e062c77895ac034a7afc0dcc8c))
* **deps:** Update the ucapi-framework to version 1.6.5 ([eb9718b](https://github.com/tinogo/uc-intg-stormaudio/commit/eb9718bae84f7785a5c5f7ff2bcb219be0fe593a))
* **deps:** Update the ucapi-framework to version 1.6.6 ([a119f8e](https://github.com/tinogo/uc-intg-stormaudio/commit/a119f8edad85bbc4c0c79d2dad1efc04f71e851a))
* **deps:** Update the UCAPI-Framework to version 1.7.2 ([e0f6424](https://github.com/tinogo/uc-intg-stormaudio/commit/e0f64242f60fb59dffdff682799ef56cd88d0709))
* **deps:** Update the ucapi-framework to version 1.9.1 ([421af73](https://github.com/tinogo/uc-intg-stormaudio/commit/421af73ded270e31e5dce5bb37816891feb1d73c))
* **deps:** update the ucapi-framework to version 1.9.6 ([fdefcec](https://github.com/tinogo/uc-intg-stormaudio/commit/fdefcec5a974c3cbd880570e265844dea731ccd7))
* **deps:** Update the uv.lock ([b866eb5](https://github.com/tinogo/uc-intg-stormaudio/commit/b866eb5ad9da71c03772994de5737998ae3120c3))
* **deps:** Update uv to version 0.10.0 ([8f35c2c](https://github.com/tinogo/uc-intg-stormaudio/commit/8f35c2c4299d544c70421bb537dc12c80ae9e10b))
* **docs:** Add a table of contents + missing a sensor to the readme ([778d270](https://github.com/tinogo/uc-intg-stormaudio/commit/778d270da14c9874ebdab206d3bf2c9dc2fcfbb3))
* **docs:** Add the newly added sensors to the readme ([5949f83](https://github.com/tinogo/uc-intg-stormaudio/commit/5949f837b1ed577e339f1d171309f14512783af7))
* **docs:** Adds docs for updating all dependencies ([59a2445](https://github.com/tinogo/uc-intg-stormaudio/commit/59a24454ff7fe34d70f389d488de66dbaad6403b))
* **docs:** Extend the Readme with more information for the entities ([3c1312e](https://github.com/tinogo/uc-intg-stormaudio/commit/3c1312e8e2d4f1cbfd8f1e7c92176de8610dc20e))
* **docs:** Update the readme ([345863b](https://github.com/tinogo/uc-intg-stormaudio/commit/345863bbd52187c59cab741d7e28eb901c773ed6))
* **docs:** Update the readme ([0b71325](https://github.com/tinogo/uc-intg-stormaudio/commit/0b71325ca8665df4cd418308f70c565c8ff39545))
* **docs:** Update the README ([991d767](https://github.com/tinogo/uc-intg-stormaudio/commit/991d767ceb7c9478a05e9af30aa3c5dcaa699aae))
* don't emit any unnecessary events to the UC remote ([494d990](https://github.com/tinogo/uc-intg-stormaudio/commit/494d9905e9293cbb8bd2f2ba1ae3238ac4b0cf20))
* Drop the custom override regarding the connection handling ([2db7692](https://github.com/tinogo/uc-intg-stormaudio/commit/2db76920907362d2473efd22b86f9d805e722367))
* Eliminate the duplicated code regarding the simple commands ([dbaf55c](https://github.com/tinogo/uc-intg-stormaudio/commit/dbaf55c1c80c097642bf4047b7e7646f21a72c9f))
* Extend the release-please config ([38da8c1](https://github.com/tinogo/uc-intg-stormaudio/commit/38da8c1f6593c9a17f6ea2cd7100acb575db11f2))
* extract magic strings into enums ([5e9d02c](https://github.com/tinogo/uc-intg-stormaudio/commit/5e9d02c638d5fdad3a171b708d62f7a96c6de242))
* Extract the device state/attributes into a separate dataclass ([#80](https://github.com/tinogo/uc-intg-stormaudio/issues/80)) ([0a0701e](https://github.com/tinogo/uc-intg-stormaudio/commit/0a0701e1b7c6120a6a932d106f123238948ed09f))
* Fix a deprecation warning ([05505c7](https://github.com/tinogo/uc-intg-stormaudio/commit/05505c7c2f5477b1335a07fae149c86788121885))
* Fix a typo ([1174ecf](https://github.com/tinogo/uc-intg-stormaudio/commit/1174ecff27e2ae7ae64c81565a9b8fb93790fcbf))
* Format the code ([45acff4](https://github.com/tinogo/uc-intg-stormaudio/commit/45acff48021d2912bb4469dc50badd5a237b1d8a))
* Format the code ([cd745d0](https://github.com/tinogo/uc-intg-stormaudio/commit/cd745d0e715f3ff4c98cf8820b3ac16f5a4b0e89))
* Ignore the .idea folder ([d86b7fa](https://github.com/tinogo/uc-intg-stormaudio/commit/d86b7fa9b611f67a725d785d3198f201563bc88b))
* ignore updates to protobuf ([2170e55](https://github.com/tinogo/uc-intg-stormaudio/commit/2170e553507536b1a9e2511bf27e899c26d9b6e4))
* Improve the Docker (Compose) setup ([053867c](https://github.com/tinogo/uc-intg-stormaudio/commit/053867c6e85d1aa7da6fa4fcaaa66411b8420d3a))
* Improve the wording of a comment ([85abfc3](https://github.com/tinogo/uc-intg-stormaudio/commit/85abfc3b6d12e3f05964124122addc171011c579))
* Initialize all logers ([d6bc2c5](https://github.com/tinogo/uc-intg-stormaudio/commit/d6bc2c5888ec11d7f7fee0c1a36734f5a5360c70))
* Let the core simulator depend on the stormaudio service ([ecd5be4](https://github.com/tinogo/uc-intg-stormaudio/commit/ecd5be43a5416e7056604a2bed2c32498d04fa9c))
* leverage immutable releases ([73edc02](https://github.com/tinogo/uc-intg-stormaudio/commit/73edc02fc1ee9f90d491f31ec2c89655243f7292))
* **main:** release 0.10.0 ([#27](https://github.com/tinogo/uc-intg-stormaudio/issues/27)) ([f8d78b6](https://github.com/tinogo/uc-intg-stormaudio/commit/f8d78b63dfd941349b030e429256d6b36ba2b56b))
* **main:** release 0.10.1 ([#31](https://github.com/tinogo/uc-intg-stormaudio/issues/31)) ([9c48e04](https://github.com/tinogo/uc-intg-stormaudio/commit/9c48e04c0c4232d1a286cad3482528278669d594))
* **main:** release 0.10.2 ([#32](https://github.com/tinogo/uc-intg-stormaudio/issues/32)) ([c2661ef](https://github.com/tinogo/uc-intg-stormaudio/commit/c2661ef86f238babef30368829c81cd6dd6e5893))
* **main:** release 0.10.3 ([#35](https://github.com/tinogo/uc-intg-stormaudio/issues/35)) ([c9e9a02](https://github.com/tinogo/uc-intg-stormaudio/commit/c9e9a028ead2b93d12ee8c331c676e666d7296e7))
* **main:** release 0.10.4 ([#37](https://github.com/tinogo/uc-intg-stormaudio/issues/37)) ([7f7841b](https://github.com/tinogo/uc-intg-stormaudio/commit/7f7841b7b7cc7e09e06caccf1d7ea092974a737c))
* **main:** release 0.10.5 ([#38](https://github.com/tinogo/uc-intg-stormaudio/issues/38)) ([289db53](https://github.com/tinogo/uc-intg-stormaudio/commit/289db536acb6ce685be1c3364cd51f906b9f1b67))
* **main:** release 0.11.0 ([#41](https://github.com/tinogo/uc-intg-stormaudio/issues/41)) ([9a1f69f](https://github.com/tinogo/uc-intg-stormaudio/commit/9a1f69f5e65d5a20992de255d093fe8d4a82e50b))
* **main:** release 0.12.0 ([#43](https://github.com/tinogo/uc-intg-stormaudio/issues/43)) ([9cd0364](https://github.com/tinogo/uc-intg-stormaudio/commit/9cd0364344bafc2a713dcea08f1593d105dc5199))
* **main:** release 0.13.0 ([#44](https://github.com/tinogo/uc-intg-stormaudio/issues/44)) ([31c3476](https://github.com/tinogo/uc-intg-stormaudio/commit/31c3476e291a591bb2863533b299a237a6feb253))
* **main:** release 0.13.1 ([#46](https://github.com/tinogo/uc-intg-stormaudio/issues/46)) ([91845ac](https://github.com/tinogo/uc-intg-stormaudio/commit/91845ac4f028672b2b5bc3495088bcebedb7a091))
* **main:** release 0.13.2 ([#49](https://github.com/tinogo/uc-intg-stormaudio/issues/49)) ([476ab85](https://github.com/tinogo/uc-intg-stormaudio/commit/476ab856fecdb27d096817b5f7dd45b0242c0d16))
* **main:** release 0.14.0 ([#53](https://github.com/tinogo/uc-intg-stormaudio/issues/53)) ([0f79f0d](https://github.com/tinogo/uc-intg-stormaudio/commit/0f79f0dea96c26eb788f854b1841d3ddeb0000c3))
* **main:** release 0.15.0 ([#55](https://github.com/tinogo/uc-intg-stormaudio/issues/55)) ([d169adb](https://github.com/tinogo/uc-intg-stormaudio/commit/d169adb4dbc110d4b42b129c10f561b582637989))
* **main:** release 0.15.1 ([#57](https://github.com/tinogo/uc-intg-stormaudio/issues/57)) ([9552fb1](https://github.com/tinogo/uc-intg-stormaudio/commit/9552fb1fe1320151bc45760fefd993dc5be6ec63))
* **main:** release 0.16.0 ([#73](https://github.com/tinogo/uc-intg-stormaudio/issues/73)) ([00b21ea](https://github.com/tinogo/uc-intg-stormaudio/commit/00b21ea7da39b641e65465ecae5d55d58e1f4519))
* **main:** release 0.16.1 ([#74](https://github.com/tinogo/uc-intg-stormaudio/issues/74)) ([1434f17](https://github.com/tinogo/uc-intg-stormaudio/commit/1434f173e0715b9a852f43bb3f2a3adfce82ea2a))
* **main:** release 0.17.0 ([#75](https://github.com/tinogo/uc-intg-stormaudio/issues/75)) ([295b035](https://github.com/tinogo/uc-intg-stormaudio/commit/295b035bef049be759b7f783a1055c94356b07ba))
* **main:** release 0.17.1 ([#77](https://github.com/tinogo/uc-intg-stormaudio/issues/77)) ([9977fcb](https://github.com/tinogo/uc-intg-stormaudio/commit/9977fcbe0afa3af39e3c4125fbef93059dd928b3))
* **main:** release 0.18.0 ([#78](https://github.com/tinogo/uc-intg-stormaudio/issues/78)) ([bb13b69](https://github.com/tinogo/uc-intg-stormaudio/commit/bb13b6960a1e33c6774a0da019b9151678bad062))
* **main:** release 0.19.0 ([#79](https://github.com/tinogo/uc-intg-stormaudio/issues/79)) ([70e8c86](https://github.com/tinogo/uc-intg-stormaudio/commit/70e8c86218e166c2287764858c7c3613720e4f39))
* **main:** release 0.19.1 ([#87](https://github.com/tinogo/uc-intg-stormaudio/issues/87)) ([9fa6c74](https://github.com/tinogo/uc-intg-stormaudio/commit/9fa6c7414d2a090e8e7832263b3115c8c6e8db10))
* **main:** release 0.19.2 ([#90](https://github.com/tinogo/uc-intg-stormaudio/issues/90)) ([f338bd8](https://github.com/tinogo/uc-intg-stormaudio/commit/f338bd8c8b0b0c8c67793821343cdc10784394f2))
* **main:** release 0.20.0 ([#92](https://github.com/tinogo/uc-intg-stormaudio/issues/92)) ([fe629ce](https://github.com/tinogo/uc-intg-stormaudio/commit/fe629cefa5e8894ff1afa129bba8589d7d38d45b))
* **main:** release 0.21.0 ([#95](https://github.com/tinogo/uc-intg-stormaudio/issues/95)) ([f8d013a](https://github.com/tinogo/uc-intg-stormaudio/commit/f8d013ace76967ae7a1988bbe68a4492fa2bd401))
* **main:** release 0.21.1 ([#96](https://github.com/tinogo/uc-intg-stormaudio/issues/96)) ([1ed6d35](https://github.com/tinogo/uc-intg-stormaudio/commit/1ed6d357c3d48c60d5d6882459eb042f8fdbb609))
* **main:** release 0.22.0 ([#97](https://github.com/tinogo/uc-intg-stormaudio/issues/97)) ([4fe2f18](https://github.com/tinogo/uc-intg-stormaudio/commit/4fe2f18924e35031181742154eee36525222405b))
* **main:** release 0.22.1 ([#99](https://github.com/tinogo/uc-intg-stormaudio/issues/99)) ([b623f8c](https://github.com/tinogo/uc-intg-stormaudio/commit/b623f8ce1a8c262b3a7aacede0c1ceccf7277210))
* **main:** release 0.22.2 ([#100](https://github.com/tinogo/uc-intg-stormaudio/issues/100)) ([71030e6](https://github.com/tinogo/uc-intg-stormaudio/commit/71030e69d90a680aba0bc8aed0cf0dec829e4fad))
* **main:** release 0.23.0 ([#101](https://github.com/tinogo/uc-intg-stormaudio/issues/101)) ([81bd8e8](https://github.com/tinogo/uc-intg-stormaudio/commit/81bd8e8821def3b289befc3870879a3289ad2bb7))
* **main:** release 0.23.1 ([#102](https://github.com/tinogo/uc-intg-stormaudio/issues/102)) ([1044788](https://github.com/tinogo/uc-intg-stormaudio/commit/10447880b0e1e322768ef3ff64419c4baf5d3aac))
* **main:** release 0.23.2 ([#103](https://github.com/tinogo/uc-intg-stormaudio/issues/103)) ([61ea279](https://github.com/tinogo/uc-intg-stormaudio/commit/61ea279c4190fd051a299a9f2d1905932d0215c3))
* **main:** release 0.23.3 ([#104](https://github.com/tinogo/uc-intg-stormaudio/issues/104)) ([7c687a9](https://github.com/tinogo/uc-intg-stormaudio/commit/7c687a92242997ba78de5563863d3097cad700a9))
* **main:** release 0.23.4 ([#105](https://github.com/tinogo/uc-intg-stormaudio/issues/105)) ([b76806c](https://github.com/tinogo/uc-intg-stormaudio/commit/b76806ca00dedef1fc46d27514aa0b0f8f4540d9))
* **main:** release 0.24.0 ([#106](https://github.com/tinogo/uc-intg-stormaudio/issues/106)) ([2d11b23](https://github.com/tinogo/uc-intg-stormaudio/commit/2d11b2371509f41edb334250e48ddb3062edf024))
* **main:** release 0.25.0 ([#109](https://github.com/tinogo/uc-intg-stormaudio/issues/109)) ([604d7d3](https://github.com/tinogo/uc-intg-stormaudio/commit/604d7d3a12eba3e0507b439b81fbe1cd71092614))
* **main:** release 0.25.1 ([#110](https://github.com/tinogo/uc-intg-stormaudio/issues/110)) ([12f1991](https://github.com/tinogo/uc-intg-stormaudio/commit/12f199178db3567b5e8d13ed75d46c8f4bf82373))
* **main:** release 0.25.2 ([#112](https://github.com/tinogo/uc-intg-stormaudio/issues/112)) ([b9b7455](https://github.com/tinogo/uc-intg-stormaudio/commit/b9b74550c52336c3a3e0d158791e1701fb97d4e7))
* **main:** release 0.25.3 ([#116](https://github.com/tinogo/uc-intg-stormaudio/issues/116)) ([9db29d1](https://github.com/tinogo/uc-intg-stormaudio/commit/9db29d1bde0f4d7c83ce46aec6335dcaf63efea5))
* **main:** release 0.25.4 ([#117](https://github.com/tinogo/uc-intg-stormaudio/issues/117)) ([36c684c](https://github.com/tinogo/uc-intg-stormaudio/commit/36c684c3eead78e3ea5d6ab8ae39e5bd1e7ab7c3))
* **main:** release 0.25.5 ([#119](https://github.com/tinogo/uc-intg-stormaudio/issues/119)) ([daff0d1](https://github.com/tinogo/uc-intg-stormaudio/commit/daff0d12b28fcfc0cbe95d926ca73bef6b8f1de8))
* **main:** release 0.25.6 ([#125](https://github.com/tinogo/uc-intg-stormaudio/issues/125)) ([3f5010c](https://github.com/tinogo/uc-intg-stormaudio/commit/3f5010cc1b64319cf175f7486ab3790641b6ab2e))
* **main:** release 0.25.7 ([#133](https://github.com/tinogo/uc-intg-stormaudio/issues/133)) ([480740f](https://github.com/tinogo/uc-intg-stormaudio/commit/480740fa1905342035d69a4e426df1a9765556c2))
* **main:** release 0.25.8 ([#145](https://github.com/tinogo/uc-intg-stormaudio/issues/145)) ([ba74536](https://github.com/tinogo/uc-intg-stormaudio/commit/ba7453656ca958a1106b3e2f83a8add3b52f4e35))
* **main:** release 0.26.0 ([#153](https://github.com/tinogo/uc-intg-stormaudio/issues/153)) ([35e726a](https://github.com/tinogo/uc-intg-stormaudio/commit/35e726a772ac46135f636ccb8a7d874bfb7bf0b5))
* **main:** release 0.26.1 ([#158](https://github.com/tinogo/uc-intg-stormaudio/issues/158)) ([8213426](https://github.com/tinogo/uc-intg-stormaudio/commit/8213426c68380072845b94c1e8264704479cd962))
* **main:** release 0.26.2 ([#161](https://github.com/tinogo/uc-intg-stormaudio/issues/161)) ([570f6bd](https://github.com/tinogo/uc-intg-stormaudio/commit/570f6bd87ca2ac46e5b4c481772162b053b29908))
* **main:** release 0.26.3 ([#166](https://github.com/tinogo/uc-intg-stormaudio/issues/166)) ([660ac05](https://github.com/tinogo/uc-intg-stormaudio/commit/660ac055e24f9444f96b4f98f11f4f0ebff8e74f))
* **main:** release 0.4.0 ([#13](https://github.com/tinogo/uc-intg-stormaudio/issues/13)) ([f9c2c82](https://github.com/tinogo/uc-intg-stormaudio/commit/f9c2c82a8d275b9d1224c4c7bd0a68a6202e90e4))
* **main:** release 0.4.1 ([#14](https://github.com/tinogo/uc-intg-stormaudio/issues/14)) ([ecd06fa](https://github.com/tinogo/uc-intg-stormaudio/commit/ecd06fa733480dac8a91e10e485490d21d3d4895))
* **main:** release 0.4.2 ([#15](https://github.com/tinogo/uc-intg-stormaudio/issues/15)) ([2470090](https://github.com/tinogo/uc-intg-stormaudio/commit/2470090d8a32760d393512c57e699a6d3943ee10))
* **main:** release 0.5.0 ([#16](https://github.com/tinogo/uc-intg-stormaudio/issues/16)) ([b9e00c0](https://github.com/tinogo/uc-intg-stormaudio/commit/b9e00c05b910c2464f5bfdb96c38529770073fb1))
* **main:** release 0.6.0 ([#18](https://github.com/tinogo/uc-intg-stormaudio/issues/18)) ([d4cb973](https://github.com/tinogo/uc-intg-stormaudio/commit/d4cb9730b3bba6c3cf9007c3c3c36f353bfbb580))
* **main:** release 0.7.0 ([#21](https://github.com/tinogo/uc-intg-stormaudio/issues/21)) ([9ec6a23](https://github.com/tinogo/uc-intg-stormaudio/commit/9ec6a23b55306ff00edfe81a8205105596601e7d))
* **main:** release 0.8.0 ([#22](https://github.com/tinogo/uc-intg-stormaudio/issues/22)) ([1d20ef1](https://github.com/tinogo/uc-intg-stormaudio/commit/1d20ef12a6b5b2aa0e3a671daf63ecbd56dce9e3))
* **main:** release 0.8.1 ([#24](https://github.com/tinogo/uc-intg-stormaudio/issues/24)) ([d28e16e](https://github.com/tinogo/uc-intg-stormaudio/commit/d28e16e719a4a28a09c12c76c776e32ba39f42dd))
* **main:** release 0.9.0 ([#25](https://github.com/tinogo/uc-intg-stormaudio/issues/25)) ([dae2ed0](https://github.com/tinogo/uc-intg-stormaudio/commit/dae2ed022f93a1a72755d4b16375e47151626211))
* Make documentation updates visible in the changelog ([4d18e86](https://github.com/tinogo/uc-intg-stormaudio/commit/4d18e8660d69118ac9017d4bb542a3c2e1d12f60))
* Make use of the entity argument ([4dc81da](https://github.com/tinogo/uc-intg-stormaudio/commit/4dc81dab16f33ae4c4c2ab3dd69067d9743a0fdc))
* Make use of the newly introduced coordinator pattern ([710db40](https://github.com/tinogo/uc-intg-stormaudio/commit/710db40c53e6800f852ae3847b09058146283a1d))
* Manage the packages with uv ([85a66e9](https://github.com/tinogo/uc-intg-stormaudio/commit/85a66e96d88ac564d9dd93b82c44238b5dd3d878))
* Move the compose env one level up ([0af3dea](https://github.com/tinogo/uc-intg-stormaudio/commit/0af3deaebda0236d83b2c8a91c2082341bbeb776))
* Move the sound_mode_list into the device config ([a21d4e3](https://github.com/tinogo/uc-intg-stormaudio/commit/a21d4e3fb2f81272edab8a01f7afa566d2644e4f))
* Optimize building the initial sensor attributes ([1628fdc](https://github.com/tinogo/uc-intg-stormaudio/commit/1628fdc3bd10bca0eab779a8a4537228d305b200))
* Optimize the close connection handling ([292b9ee](https://github.com/tinogo/uc-intg-stormaudio/commit/292b9ee5343912f733c5f6f0d97203ba616fcabb))
* Optimize the compose setup ([7d06df9](https://github.com/tinogo/uc-intg-stormaudio/commit/7d06df949d4cec7db6c954f6d8b5c3c6bf72fb02))
* Reduce code duplication between the power_toggle and mute_toggle methods ([0a7eaf0](https://github.com/tinogo/uc-intg-stormaudio/commit/0a7eaf03348b6c06ed23fe169b3a8f78dd591bb5))
* reduce code duplication for the Select entities ([07c3379](https://github.com/tinogo/uc-intg-stormaudio/commit/07c33795b3b2b12752ade92e81624289d5da0b1f))
* reduce code duplication for the Sensor entities ([238f4bd](https://github.com/tinogo/uc-intg-stormaudio/commit/238f4bd3f0d1e5c032245b46aff8f6d5d87d8663))
* Reduce the code complexity within the media player ([40cc0fa](https://github.com/tinogo/uc-intg-stormaudio/commit/40cc0fa62c29d5b98149684ee6ed8d9d4738d8a1))
* Reduce the cyclomatic complexity in sensor and select entities ([9847a6c](https://github.com/tinogo/uc-intg-stormaudio/commit/9847a6cb5dba83fbac3846bda04353fd5f4ff24d))
* Reduce the cyclomatic complexity of retrieving the the entity attributes ([b9c2317](https://github.com/tinogo/uc-intg-stormaudio/commit/b9c231760ecda8c53eddd5b36d3343fa4a0d01f0))
* Refactor some code ([ecb38d0](https://github.com/tinogo/uc-intg-stormaudio/commit/ecb38d091bdb548ed0d2ceefc0c7b305c8001aeb))
* Refactor the internals of the Sensor entity ([890563f](https://github.com/tinogo/uc-intg-stormaudio/commit/890563f7516aaf25a47713451aec8483134566ab))
* Refactor the power state handling to reduce code duplication ([2b711e9](https://github.com/tinogo/uc-intg-stormaudio/commit/2b711e953c58d5b013f3c6bd6efce484ef574ea6))
* Remove obsolete code ([3e4c7dc](https://github.com/tinogo/uc-intg-stormaudio/commit/3e4c7dc57e5ede09e63c940c03d06db0a0e044af))
* Remove some obsolete code from the StormAudioDriver ([995d628](https://github.com/tinogo/uc-intg-stormaudio/commit/995d628393774b95ee8b3686f94282abe19bd4cd))
* Remove some unnecessary _wait_for_response calls ([3d0f285](https://github.com/tinogo/uc-intg-stormaudio/commit/3d0f2852709f7a766886a986471cf046471ab4cb))
* remove some unnecessary files ([16ac164](https://github.com/tinogo/uc-intg-stormaudio/commit/16ac16415dfa71b21de28f1cfb22ea4543e39161))
* Remove the _toggle_helper helper function ([9a31de0](https://github.com/tinogo/uc-intg-stormaudio/commit/9a31de00212e65e09dc02bcfe8aaf16cf114892e))
* Remove the black package ([c934701](https://github.com/tinogo/uc-intg-stormaudio/commit/c9347012e87d0dca9b3f148e53d635c7a811a5ea))
* Remove the create_sensors helper function ([20d1dff](https://github.com/tinogo/uc-intg-stormaudio/commit/20d1dff0353cc2094dd4f8d8d7b985a15d167bfd))
* Remove the network_mode property from the compose.yml ([af6a2ea](https://github.com/tinogo/uc-intg-stormaudio/commit/af6a2eae2a0edd26d8f2ac6034d70f1802561898))
* Remove the telnetlib3 dependency ([c6cbc3f](https://github.com/tinogo/uc-intg-stormaudio/commit/c6cbc3f39c461015cae0780e6dc042f53bb43899))
* Remove the volume feature from media_player.py ([bc66f35](https://github.com/tinogo/uc-intg-stormaudio/commit/bc66f357c90c480aa34611199275d5da151394b6))
* Rename docker-compose.yml to compose.yml ([bae3a5a](https://github.com/tinogo/uc-intg-stormaudio/commit/bae3a5af33d3008fa487ddafb736220f4a3099ed))
* Rename intg-template to intg-stormaudio ([ddb651a](https://github.com/tinogo/uc-intg-stormaudio/commit/ddb651a011dc8c2aef744409954c3674e4c62d02))
* rename the SetupFlow class ([7aa4a71](https://github.com/tinogo/uc-intg-stormaudio/commit/7aa4a71faf60001650bb7b5c5aac2b42c6c7fb65))
* Renamed StormAudioDeviceState to StormAudioDeviceAttributes ([5ccbdd8](https://github.com/tinogo/uc-intg-stormaudio/commit/5ccbdd8d718416868f455a9c0fd2ccfab034935c))
* Reuse some more code from the device within the media_player ([237d5b8](https://github.com/tinogo/uc-intg-stormaudio/commit/237d5b80ed9e2c07aa9d408938c7292672cfd009))
* Satisfy Pylint ([7fc8847](https://github.com/tinogo/uc-intg-stormaudio/commit/7fc8847151a8c1766b0dfac8e9c61173bde59898))
* separate the StormIntegrationDriver from the main entrypoint ([a42bd91](https://github.com/tinogo/uc-intg-stormaudio/commit/a42bd91f5fd5dfe2813471941f4869088a053463))
* Simplify the sound_mode handling ([7d9e37a](https://github.com/tinogo/uc-intg-stormaudio/commit/7d9e37afce470ac018a3cb81fb5a90c7c806eedc))
* slightly improve some wording ([667b716](https://github.com/tinogo/uc-intg-stormaudio/commit/667b716584778d5fb644f8fa8013595d52fdf829))
* some move code around ([373bda6](https://github.com/tinogo/uc-intg-stormaudio/commit/373bda688f4e6cccd9aaeba7f807a7c1ecd380f2))
* Update the dependencies ([f9f8eb2](https://github.com/tinogo/uc-intg-stormaudio/commit/f9f8eb2452f4edc45cea0230e7546c26325ebf4b))
* Update the hostname of the dev integration ([b1ce8b4](https://github.com/tinogo/uc-intg-stormaudio/commit/b1ce8b4c3688543204829a1a59efd71536313e1c))
* Update the version numbers ([17bc204](https://github.com/tinogo/uc-intg-stormaudio/commit/17bc204763bf59125afd16d3c925288541d48027))
* Update the version numbers ([b21ce60](https://github.com/tinogo/uc-intg-stormaudio/commit/b21ce60308ba62604aabd91b3153944fc1d450f7))
* Update the version numbers ([5f5d35a](https://github.com/tinogo/uc-intg-stormaudio/commit/5f5d35ac430f8738f9101c402384097bc2c328f7))
* Update the version numbers ([d95e309](https://github.com/tinogo/uc-intg-stormaudio/commit/d95e30999e36a860a1fb33e09ed578e961e36c32))
* Update the version numbers ([ad32935](https://github.com/tinogo/uc-intg-stormaudio/commit/ad32935ff8721a7361c2280978cdf385f1f0ff63))
* Update the version numbers ([15f133d](https://github.com/tinogo/uc-intg-stormaudio/commit/15f133d8d1c6f0a9ccaf8dce3e64d2058eeca0de))
* Update the version numbers ([6e16d00](https://github.com/tinogo/uc-intg-stormaudio/commit/6e16d00d971aafaf8fb92df2fc00800372bbc4b0))
* use a StringEnum for the StormAudioStates ([c50112f](https://github.com/tinogo/uc-intg-stormaudio/commit/c50112fc8411a486d87092117ea6db368e9b73cc))
* Use EAFP-approach to check the existence of a key ([561a8f4](https://github.com/tinogo/uc-intg-stormaudio/commit/561a8f4dff886bb620ef3f05f9edd50d2c2028cd))
* Use host networking for the core-simulator ([330aa44](https://github.com/tinogo/uc-intg-stormaudio/commit/330aa44eaa9d9f6f93fc8e5ac7b786dbeab8ecbd))
* Use keyword args in the media-player again ([0c6243a](https://github.com/tinogo/uc-intg-stormaudio/commit/0c6243a733550da0ddd4fd054ae2122466265d8b))
* Use the StormAudioClient instead of instantiating the complete device ([89e9636](https://github.com/tinogo/uc-intg-stormaudio/commit/89e963618755748f8c0e6d17e9f11dd17d56dd05))
* Use the UCAPI-Framework Entity-class ([#83](https://github.com/tinogo/uc-intg-stormaudio/issues/83)) ([9c629ef](https://github.com/tinogo/uc-intg-stormaudio/commit/9c629ef3473919a541f1682bba82d5212c6d07ba))


### Reverts

* Remove the websocket parameter from the handle_command method again ([6e2acf8](https://github.com/tinogo/uc-intg-stormaudio/commit/6e2acf8e8eea56e20915c20d3d04f9c0b48698ab))
* Revert the changes related to the connection handling ([b84c858](https://github.com/tinogo/uc-intg-stormaudio/commit/b84c858af58d5dc4aebaaf3c2059c9f520f2c8ba))

## [0.26.3](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.26.2...v0.26.3) (2026-09-05)


### Miscellaneous

* **ci-cd:** optimize building the integration ([b8ef902](https://github.com/tinogo/uc-intg-stormaudio/commit/b8ef9022ef174668380e6754ff888bc89485bdc6))

## [0.26.2](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.26.1...v0.26.2) (2026-08-29)


### Documentation

* remove a non-existing file from the README.md ([da7dc39](https://github.com/tinogo/uc-intg-stormaudio/commit/da7dc39104844f07a33a10169d991905d1b5c5b5))


### Miscellaneous

* **deps:** Update the dependencies ([33b9887](https://github.com/tinogo/uc-intg-stormaudio/commit/33b988747f2a9414451922c87dad1226954287a5))
* **deps:** Update the required uv version to 0.12.7 ([c2a4c73](https://github.com/tinogo/uc-intg-stormaudio/commit/c2a4c7382e5fedc90365189a506387d162f6422d))

## [0.26.1](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.26.0...v0.26.1) (2026-08-28)


### Documentation

* document how to update a single package ([3754088](https://github.com/tinogo/uc-intg-stormaudio/commit/375408817367e0546a8c2f2b7e6fea99d7eb2d03))
* fix some typos ([2388443](https://github.com/tinogo/uc-intg-stormaudio/commit/2388443d9f597fcee56dae8be2a6bb2c15516beb))


### Miscellaneous

* **deps:** update the ucapi-framework to version 1.9.6 ([fdefcec](https://github.com/tinogo/uc-intg-stormaudio/commit/fdefcec5a974c3cbd880570e265844dea731ccd7))
* leverage immutable releases ([73edc02](https://github.com/tinogo/uc-intg-stormaudio/commit/73edc02fc1ee9f90d491f31ec2c89655243f7292))
* reduce code duplication for the Select entities ([07c3379](https://github.com/tinogo/uc-intg-stormaudio/commit/07c33795b3b2b12752ade92e81624289d5da0b1f))
* reduce code duplication for the Sensor entities ([238f4bd](https://github.com/tinogo/uc-intg-stormaudio/commit/238f4bd3f0d1e5c032245b46aff8f6d5d87d8663))
* some move code around ([373bda6](https://github.com/tinogo/uc-intg-stormaudio/commit/373bda688f4e6cccd9aaeba7f807a7c1ecd380f2))

## [0.26.0](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.8...v0.26.0) (2026-07-28)


### Features

* **ci-cd:** use a ARM-native CI-runner to build the artifact ([c5dabaa](https://github.com/tinogo/uc-intg-stormaudio/commit/c5dabaa3ccb84188d6e8816fec9c3c87a9631911))


### Miscellaneous

* **deps:** bump actions/setup-python from 6 to 7 in /.github/workflows ([#148](https://github.com/tinogo/uc-intg-stormaudio/issues/148)) ([f524ae0](https://github.com/tinogo/uc-intg-stormaudio/commit/f524ae0962f6c9ed6a2cedefd36180b528ffb7ee))
* **deps:** Update the dependencies ([5ab1af8](https://github.com/tinogo/uc-intg-stormaudio/commit/5ab1af892afa7d4f5d5adff4682a73d3e2e1e7a2))

## [0.25.8](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.7...v0.25.8) (2026-07-01)


### Bug Fixes

* gracefully handle TCP-Connection errors in close_connection ([fd31ebd](https://github.com/tinogo/uc-intg-stormaudio/commit/fd31ebd0d82a16c7036d1791950da104b652e432))


### Miscellaneous

* **deps:** bump actions/checkout from 6 to 7 in /.github/workflows ([#144](https://github.com/tinogo/uc-intg-stormaudio/issues/144)) ([bdc57f7](https://github.com/tinogo/uc-intg-stormaudio/commit/bdc57f7e427bc64187a527e42a9d921829566379))
* **deps:** Update the dependencies ([d1e12b5](https://github.com/tinogo/uc-intg-stormaudio/commit/d1e12b5d1211369647e21ee70725ff2cdcb42d76))

## [0.25.7](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.6...v0.25.7) (2026-05-19)


### Bug Fixes

* **ci:** Restrict the permissions in the CI-pipeline a bit ([6638550](https://github.com/tinogo/uc-intg-stormaudio/commit/66385509f09cab8cd7e3eb3afa108a425b6bcbd2))


### Miscellaneous

* Update the dependencies ([f9f8eb2](https://github.com/tinogo/uc-intg-stormaudio/commit/f9f8eb2452f4edc45cea0230e7546c26325ebf4b))

## [0.25.6](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.5...v0.25.6) (2026-05-05)


### Bug Fixes

* fix the dependabot config for updating github actions ([058d0fd](https://github.com/tinogo/uc-intg-stormaudio/commit/058d0fd4cd6b916af5186fcec5f6b4016522f605))


### Miscellaneous

* **deps:** Add requirements for uv ([9236aa5](https://github.com/tinogo/uc-intg-stormaudio/commit/9236aa57635f98e943ab199644800421c73f00f2))
* **deps:** bump googleapis/release-please-action from 4 to 5 ([#126](https://github.com/tinogo/uc-intg-stormaudio/issues/126)) ([c4d74f4](https://github.com/tinogo/uc-intg-stormaudio/commit/c4d74f413f2e2603f42732703bc7a513abaec657))
* **deps:** let dependabot update the uv.lock ([6f6e302](https://github.com/tinogo/uc-intg-stormaudio/commit/6f6e302d47f18577f4ee5e586151f612c4c7ed47))
* **deps:** Update the dependencies ([bdf7634](https://github.com/tinogo/uc-intg-stormaudio/commit/bdf7634a4ed9d041bb28c70f8c1de11e9ca1c0a4))
* **deps:** update the r2-pyinstaller docker image ([cdafb97](https://github.com/tinogo/uc-intg-stormaudio/commit/cdafb979a573832ad43de7917ee919fdf8aa420b))
* ignore updates to protobuf ([2170e55](https://github.com/tinogo/uc-intg-stormaudio/commit/2170e553507536b1a9e2511bf27e899c26d9b6e4))

## [0.25.5](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.4...v0.25.5) (2026-03-13)


### Miscellaneous

* **deps:** Update the ucapi-framework to version 1.9.1 ([421af73](https://github.com/tinogo/uc-intg-stormaudio/commit/421af73ded270e31e5dce5bb37816891feb1d73c))

## [0.25.4](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.3...v0.25.4) (2026-03-09)


### Miscellaneous

* Eliminate the duplicated code regarding the simple commands ([dbaf55c](https://github.com/tinogo/uc-intg-stormaudio/commit/dbaf55c1c80c097642bf4047b7e7646f21a72c9f))
* Reduce the cyclomatic complexity in sensor and select entities ([9847a6c](https://github.com/tinogo/uc-intg-stormaudio/commit/9847a6cb5dba83fbac3846bda04353fd5f4ff24d))

## [0.25.3](https://github.com/tinogo/uc-intg-stormaudio/compare/v0.25.2...v0.25.3) (2026-03-09)


### Miscellaneous

* **deps:** Update the dependencies ([5c1d809](https://github.com/tinogo/uc-intg-stormaudio/commit/5c1d809eb2e891f4fd592a1ca8b1b61b250a7065))
* Make use of the newly introduced coordinator pattern ([710db40](https://github.com/tinogo/uc-intg-stormaudio/commit/710db40c53e6800f852ae3847b09058146283a1d))

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
