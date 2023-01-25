# SPDX-FileCopyrightText: 2023-present Heath Brown <heathd.brown@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from ..__about__ import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="isdown")
@click.pass_context
def isdown(ctx: click.Context):
    click.echo("Hello world!")
