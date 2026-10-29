import pathlib, tomllib

CFG = tomllib.loads(pathlib.Path(__file__).with_name("config.toml").read_text())


def attempts():
    return CFG["retry"]["attempts"]
