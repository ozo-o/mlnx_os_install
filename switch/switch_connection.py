"""

switch = ConnectHandler(**cisco_881)


"""
from netmiko import ConnectHandler
import json
import time

class BadImageName(Exception):
    pass


class FailedToInstallImage(Exception):
    pass


class SwitchConnection:
    def __init__(self, switch_name: str = '', switch_ip: str = '',
                 username: str = 'admin', password: str = 'admin'):
        if switch_name and switch_ip:
            assert "User have to provide switch_name or switch_ip"

        self.switch_name = switch_name
        self.switch_ip = switch_ip

        # {'device_type': 'mellanox', 'host': 'egl-zeus-05', 'username': 'admin', 'password': 'admin'}
        mellanox_config = {
                           'device_type': 'mellanox',
                           'host': self.switch_name if self.switch_name else self.switch_ip,
                           'username': username,
                           'password': password
                           }
        self.conn = ConnectHandler(**mellanox_config)
        self.conn.enable()
        self.conn.config_mode()

    def run_command(self, command: str) -> str:
        result = self.conn.send_command(command)
        return result

    def image_fetch(self, image_path: str, image_name: str, server: str, password: str):
        """
        image fetch scp://root:password@server/path_to_file/image-X86_64 3.9.0454.img
        :return:
        """
        cmd = f"image fetch scp://root:{password}@{server}{image_path}{image_name}"
        image_fetch_result = self.conn.send_command(cmd, delay_factor=5)
        cmd = f"show images | include Image | include {image_name}"
        show_image_result = self.conn.send_command(cmd)

        if show_image_result.strip() == '':
            raise BadImageName(f'Failed to load image: {image_path}{image_name}\noutput: {image_fetch_result}')

        return image_fetch_result, show_image_result.strip()

    def image_install(self, image_name: str) -> str:
        """
        image install image-X86_64 3.9.0454.img
        :return:
        """
        cmd = f"image install {image_name}"
        result = self.conn.send_command(cmd, delay_factor=5)
        return result

    def switch_version(self) -> str:
        result = self.run_command('show version | json')
        show_version_json = json.loads(result)
        return show_version_json['Product release'].strip()

    def save_configuration(self):
        cmds = ['image boot next', 'configuration write']
        for cmd in cmds:
            self.conn.send_command(cmd)

    def establish_connection(self):
        self.conn.establish_connection()
        self.conn.enable()
        self.conn.config_mode()

    def reload(self):
        self.conn.send_command('reload')
        time.sleep(120)

    def cleanup(self):
        self.conn.cleanup()