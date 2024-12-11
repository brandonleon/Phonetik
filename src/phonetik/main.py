"""Main module for the Phonetik application."""

import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version
from typing import Optional

import typer
from rich.console import Console
from rich.text import Text

from .constants import (
    nato_phonetic_alphabet,
    nato_phonetic_numbers,
    phonetic_symbols,
)

app = typer.Typer(rich_markup_mode="markdown")


def version_callback(value: bool) -> None:
    """Print the version of the application if requested."""
    if value:
        try:
            version_number = get_version(
                "phonetik"
            )  # Ensure the package name is correct
            typer.echo(f"Phonetik version {version_number}")
        except PackageNotFoundError:
            typer.echo("Version information not found.")
        raise typer.Exit()


def get_phonetic_representation(letter: str) -> Text:
    """Get the phonetic representation of a letter."""
    upper_letter = letter.upper()
    if upper_letter in nato_phonetic_alphabet:
        return Text(nato_phonetic_alphabet[upper_letter], style="#FFFFFF")
    elif upper_letter in phonetic_symbols:
        return Text(phonetic_symbols[upper_letter], style="#E24E4E")
    elif upper_letter in nato_phonetic_numbers:
        return Text(nato_phonetic_numbers[upper_letter], style="#74A9E0")
    else:
        return Text(letter, style="#FFFFFF")


def transform_text_to_nato_phonetic(text: str, plain: bool, single_line: bool) -> None:
    """Transform text into the NATO phonetic alphabet."""
    console = Console(no_color=plain)
    result = [get_phonetic_representation(letter) for letter in text]

    if single_line:
        console.print(*result, sep=" ")
    else:
        console.print(*result, sep="\n")


# noinspection PyUnusedLocal
@app.command()
def main(
    text: Optional[str] = typer.Argument(
        None,
        help="The text to convert into the NATO phonetic alphabet. Use quotes for phrases.",
    ),
    plain: bool = typer.Option(
        False, help="Disables colored output for plain terminal compatibility."
    ),
    single_line: bool = typer.Option(
        False, help="Displays the phonetic alphabet output in a single line."
    ),
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        callback=version_callback,
        help="Print the version of the application.",
    ),
) -> None:
    """Convert text to NATO phonetic alphabet.

    This command accepts input as a command-line argument or reads from standard input if no argument is provided.
    If no input is provided and standard input is empty, an error message will be displayed.

    """
    if text is None:
        if sys.stdin.isatty():
            typer.echo("Error: No text provided. Use --help for more information.")
            raise typer.Exit()
        else:
            text = sys.stdin.read().strip()
            if not text:
                typer.echo("Error: Empty input provided.")
                raise typer.Exit()

    transform_text_to_nato_phonetic(text, plain, single_line)


if __name__ == "__main__":
    app()
