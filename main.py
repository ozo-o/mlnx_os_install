#!/usr/bin/env python

import argparse
import sys

from switch.switch_connection import SwitchConnection, FailedToInstallImage
def get_args():
    """
    add and parse program arguments
    """
    parser = argparse.ArgumentParser(description='This tool is for installing mellanox-os')
    parser.add_argument('-s', '--switch-name', help='Switch name to connect', required=True)
    parser.add_argument('-u', '--switch-username', help='Switch name to connect', default='admin')
    parser.add_argument('-sp', '--switch-password', help='Switch name to connect', default='admin')
    parser.add_argument('-i', '--switch_ip', help='Switch ip to connect')
    parser.add_argument('-b', '--install', action='store_true', help='Install mellanox-os')
    parser.add_argument('-d', '--fetch', action='store_true', help='fetch mellanox-os')

    parser.add_argument('-l', '--image-path',  help='image path location')
    parser.add_argument('-n', '--image-name', help='image name')

    parser.add_argument('-m', '--master-ip', help='master ip to fetch the image from')
    parser.add_argument('-p', '--master-password', help='master password to connect from the switch')

    try:
        args_obj = parser.parse_args()
        # breakpoint()
        if args_obj.install is True and args_obj.image_name is None or args_obj.image_path is None:
            parser.error('--install can only be used when image-path and image-name are provided.')
        if args_obj.fetch is True and args_obj.master_ip is None or args_obj.master_password is None:
            parser.error('--fetch can only be used when master-ip and master-password are provided.')


    except IOError as exc:
        parser.error(str(exc))
    return args_obj


def main():
    """
    main function
    """
    args = get_args()
    sw = SwitchConnection(switch_name=args.switch_name, switch_ip=args.switch_ip,
                          username=args.switch_username, password=args.switch_password)
    try:
        if args.fetch:
            sw.image_fetch(args.image_path, args.image_name, args.master_ip, args.master_password)
        if args.install:
            sw.image_install(image_name=args.image_name)
            sw.save_configuration()
            sw.reload()
        sw = SwitchConnection(switch_name=args.switch_name, switch_ip=args.switch_ip)
        version = sw.switch_version()
        if version not in args.image_name:
            raise FailedToInstallImage("switch version is not as the required image")
    except Exception as e:
        print(f"Failed to install image\nException: {e}")
    finally:
        sw.cleanup()


if __name__ == "__main__":
    sys.exit(main())