from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


install_requires = [
    'netmiko>=3.4.0',
]

setup_args = dict(
    name='mlnxos',
    version='0.1',
    description='Useful tool to install mellanox-os',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Oz Ohayon',
    author_email='ozo@nvidia.com',
    keywords=['mlnxos', 'mellanox'],
    url='https://github.com/ozo-o/mlnx_os_install.git',
    download_url='https://pypi.org/project/elastictools/',
    install_requires=install_requires,
)


if __name__ == '__main__':
    setup(**setup_args)