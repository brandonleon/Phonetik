import argparse
import tomllib
from rich.console import Console
from rich.text import Text

from constants import nato_phonetic_alphabet, phonetic_symbols, nato_phonetic_numbers

__version__ = "1.0.0"


def get_phonetic_representation(letter: str, plain: bool) -> Text:
    """
    Get the phonetic representation of a letter with appropriate color coding.

    Args:
        letter (str): The letter to transform.
        plain (bool): Flag to indicate if the output should be plain text.

    Returns:
        Text: The phonetic representation with or without color coding.
    """
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
    """
    Transform a text into the NATO phonetic alphabet for oral transmission, one word on each line.

    Args:
        text (str): Text to transform.
        plain (bool): Flag to indicate if the output should be plain text.
        single_line (bool): Flag to indicate if the output should be in a single line.

    Returns:
        None
    """
    console = Console(no_color=plain)
    result = [get_phonetic_representation(letter, plain) for letter in text]
    if single_line:
        console.print(*result, sep=" ")
    else:
        console.print(*result, sep="\n")


def main():
    parser = argparse.ArgumentParser(
        description="Transform text into the NATO phonetic alphabet for oral transmission."
    )
    parser.add_argument(
        "text", type=str, help="Text to transform into the NATO phonetic alphabet."
    )
    parser.add_argument(
        "-p",
        "--plain",
        action="store_true",
        help="Output plain text without formatting.",
    )
    parser.add_argument(
        "-s",
        "--single-line",
        action="store_true",
        help="Output the text in a single line.",
    )
    parser.add_argument(
        "-v ",
        "--version",
        action="version",
        version=__version__,su
        help="Show the version.",
    )
    args = parser.parse_args()
    transform_text_to_nato_phonetic(args.text, args.plain, args.single_line)


if __name__ == "__main__":
    main()
