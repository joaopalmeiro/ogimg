# ogimg

A Python CLI for downloading metadata images (e.g., [OG](https://ogp.me/) images) from web pages.

## References

- [OpenGraph.xyz](https://www.opengraph.xyz/).
- [`imghdr` module](https://docs.python.org/3.7/library/imghdr.html).
- [PDM-VSCode](https://github.com/frostming/pdm-vscode) plugin.

## Notes

- Commands:
  - `pip install wheel` ([GitHub issue](https://github.com/David-OConnor/pyflow/issues/177)).
  - `pyflow init` or `pyflow new ogimg`.
  - `pyflow install`.
  - `pyflow install metadata_parser click`.
  - `pyflow install black --dev` and `pyflow install isort --dev`.
  - `pyflow ogimg`.
  - `pyflow black .` and `pyflow isort . --profile black`.
  - `pyflow clear` and `pyflow reset`.
- [tools like `black` don't work with VSCode](https://github.com/David-OConnor/pyflow/issues/31) (open) issue.
- [Incomplete package install](https://github.com/David-OConnor/pyflow/issues/32) issue.
- [Running ipython fails with `No module named 'pexpect'`](https://github.com/David-OConnor/pyflow/issues/168) (open) issue. `pyflow install tomli typed-ast --dev`.
