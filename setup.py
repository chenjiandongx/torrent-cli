from setuptools import setup
from torrent import __version__

setup(
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    name="torrent-cli",
    version=__version__,
    license="MIT",
    url = "https://github.com/chenjiandongx/torrent-cli",
    py_modules=['torrent',],
    description="Magnets-Getter CLI Tools",
    entry_points={
        'console_scripts':['torrent-cli=torrent:command_line_runner']
    }
)
