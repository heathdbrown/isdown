# SPDX-FileCopyrightText: 2023-present Heath Brown <heathd.brown@gmail.com>
#
# SPDX-License-Identifier: MIT
import pathlib
import time

# import click
import httpx
from rich.console import Console
from rich.table import Column, Table
from rich.live import Live
import asyncclick as click
import anyio

console = Console()

from ..__about__ import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="isdown")
@click.pass_context
def isdown(ctx: click.Context):
    pass


def read_file(file: str) -> list[str]:
    if not pathlib.Path(file).exists():
        print(f"Error {file} does not exist")
    with open(file, "r") as f:
        lines = f.readlines()
    return lines


async def http_connect(site: str) -> tuple[str, str]:

    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(site)
    except httpx.ConnectError:
        return site, "Connection Error"
    except Exception as e:
        return site, f"{type(e)}"

    if not r:
        return site, "Error"
    if r.status_code in range(200, 400):
        return site, "OK"
    if r.status_code in [401, 403]:
        return site, "Authentication or Authorization Needed"
    if r.status_code in [400, 402, range(404, 500)]:
        return site, "Client Error"
    if r.status_code in range(500, 600):
        return site, "Server Error"


@isdown.command()
@click.argument("sites", nargs=-1, required=False)
@click.option("-i", "--input-file", "input_file", required=False)
async def check(sites, input_file):
    if sites and input_file:
        isites = tuple(read_file(input_file))
        sites = sites + isites
    elif not sites and input_file:
        sites = tuple(read_file(input_file))
    elif sites and not input_file:
        sites = sites

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Site", style="dim")
    table.add_column("Status")

    with click.progressbar(
        sites,
    ) as click_sites:
        for site in click_sites:
            table.add_row(*await http_connect(site))
    console.print(table)


if __name__ == "__main__":
    check(_anyio_backend="trio")
