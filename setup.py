from setuptools import setup

setup(
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    name="torrent-cli",
    version="0.0.2",
    license="MIT",
    url="https://github.com/chenjiandongx/torrent-cli",
    py_modules=['torrent',],
    install_requires=['bs4', 'requests', 'lxml'],
    description="Magnets-Getter CLI Tools",
    entry_points={
        'console_scripts':['torrent-cli=torrent:command_line_runner']
    }
)
