# ogimg

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

A Python CLI for downloading metadata images (e.g., [OG](https://ogp.me/) images) from web pages.

## References

- [OpenGraph.xyz](https://www.opengraph.xyz/).
- [`imghdr` module](https://docs.python.org/3.7/library/imghdr.html).
- [PDM-VSCode](https://github.com/frostming/pdm-vscode) plugin.

## Development

- `pdm config python.use_venv False` + `pdm config python.use_venv`
- `pdm install`
- `pdm run ogimg --help`
- `pdm run ogimg https://github.com/joaopalmeiro/nbadge`
- `pdm run black .` + `pdm run isort .`

## Notes

- [Pyflow](https://github.com/David-OConnor/pyflow):
  - Commands:
    - `pip install wheel` ([GitHub issue](https://github.com/David-OConnor/pyflow/issues/177)).
    - `pyflow init` or `pyflow new ogimg`.
    - `pyflow install metadata_parser click`.
    - `pyflow install black --dev` and `pyflow install isort --dev`.
    - `pyflow clear` and `pyflow reset`.
    - `pyflow -V`.
    - `pyflow install`.
    - `pyflow ogimg --help` or `pyflow ogimg https://github.com/joaopalmeiro/nbadge`.
    - `pyflow black .` and `pyflow isort . --profile black`.
  - [tools like `black` don't work with VSCode](https://github.com/David-OConnor/pyflow/issues/31) (open) issue.
  - [Incomplete package install](https://github.com/David-OConnor/pyflow/issues/32) issue.
  - [Running ipython fails with `No module named 'pexpect'`](https://github.com/David-OConnor/pyflow/issues/168) (open) issue. `pyflow install tomli typed-ast --dev`.
  - [pyflow randomizes the order of pyflow.lock every time I run a script through it](https://github.com/David-OConnor/pyflow/issues/178) (open) issue.
- [Twine](https://twine.readthedocs.io/en/stable/) documentation.
- `pdm add -dG format black isort`.
- `pdm add metadata_parser click`.
- `pdm config python.use_venv`.
