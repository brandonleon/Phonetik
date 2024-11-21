import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version

import typer
from rich.console import Console
from rich.text import Text

from .constants import (
    nato_phonetic_alphabet,
    nato_phonetic_numbers,
    phonetic_symbols,
)

app = typer.Typer()


def version_callback(value: bool):
    """Print the version of the application if requested."""
    if value:
        try:
            version_number = get_version(
                "text2nato"
            )  # Ensure the package name is correct
            typer.echo(f"text2nato version {version_number}")
        except PackageNotFoundError:
            typer.echo("Version information not found.")
        raise typer.Exit()


def get_phonetic_representation(letter: str, plain: bool) -> Text:
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
    result = [get_phonetic_representation(letter, plain) for letter in text]
    if single_line:
        console.print(*result, sep=" ")
    else:
        console.print(*result, sep="\n")


# noinspection PyUnusedLocal
@app.command()
def main(
    text: str = typer.Argument(
        None,
        help="Text to convert to NATO phonetic alphabet, will read from stdin if not provided.",
    ),
    plain: bool = typer.Option(False, help="Output plain text without formatting."),
    single_line: bool = typer.Option(False, help="Output the text in a single line."),
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback),
):
    """Main function to run the text to NATO phonetic conversion."""

    if text is None:
        if sys.stdin.isatty():
            typer.echo("Error: No text provided. Use --help for more information.")
            raise typer.Exit()

        else:
            text = sys.stdin.read()

    transform_text_to_nato_phonetic(text, plain, single_line)


if __name__ == "__main__":
    app()