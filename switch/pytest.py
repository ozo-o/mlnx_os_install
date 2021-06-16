
import json

from switch_connection import SwitchConnection, BadImageName
import time
import pytest


def test_reboot():
    switch = SwitchConnection('egl-zeus-05')
    switch.reload()
    switch.cleanup()


def test_version():
    switch = SwitchConnection('egl-zeus-05')
    result = switch.switch_version()
    switch.cleanup()
    assert result == '3.9.2400'


def test_fetch():
    image_path = "/tmp/"
    image_name = "image-X86_64-3.9.2400.img"
    switch = SwitchConnection('egl-zeus-05')
    image_fetch_result, show_image_result = switch.image_fetch(image_path, image_name, "10.130.14.9", "3tango")
    assert show_image_result == f'Image  : {image_name}'
    switch.cleanup()


def test_install():
    # image_name = "image-X86_64-3.9.2302.img"
    image_name = "image-X86_64-3.9.2400.img"
    image_path = "/tmp/"
    switch = SwitchConnection('egl-zeus-05')
    image_fetch_result, show_image_result = switch.image_fetch(image_path, image_name, "10.130.14.9", "3tango")
    switch_version_before_install = switch.switch_version()
    switch.image_install(image_name)
    switch.save_configuration()
    switch.reload()
    time.sleep(120)
    switch = SwitchConnection('egl-zeus-05')
    switch_version_after_install = switch.switch_version()
    assert switch_version_before_install != switch_version_after_install
    switch.cleanup()


def test_bad_image_name():
    image_name = "image-X86_64-3.9.2400aa.img"
    image_path = "/tmp/"
    switch = SwitchConnection('egl-zeus-05')
    with pytest.raises(BadImageName):
        image_fetch_result, show_image_result = switch.image_fetch(image_path, image_name, "10.130.14.9", "3tango")

def test_connection_establish():
    pass
