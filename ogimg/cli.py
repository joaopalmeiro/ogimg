import imghdr

import click
import metadata_parser
import requests


@click.command()
@click.argument("url")
def main(url: str) -> None:
    page = metadata_parser.MetadataParser(url=url, search_head_only=True)

    img_url = page.get_metadatas("image", strategy=["og"])[0]

    img_data = requests.get(img_url).content
    img_extension = imghdr.what("", h=img_data)

    with open(f"teste.{img_extension}", "wb") as handler:
        handler.write(img_data)

    click.echo("\n✨ Done!")
