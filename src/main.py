"""
CLI tool to transform text into the NATO phonetic alphabet for oral transmission.
"""

import argparse
from rich.console import Console
from rich.text import Text

from constants import nato_phonetic_alphabet, phonetic_symbols, nato_phonetic_numbers

def transform_text_to_nato_phonetic(text: str) -> None:
    """
    Transform a text into the NATO phonetic alphabet for oral transmission, one word on each line.
    TODO: Add support for color coding numbers, symbols, and letters.
    Args:
        text (str): Text to transform.

    Returns:
        None
    """
    console = Console()
    result = []

    for letter in text:
        upper_letter = letter.upper()
        # If letter, white, if symbol red, if number blue
        if upper_letter in nato_phonetic_alphabet:
            result.append(Text(f"{nato_phonetic_alphabet[upper_letter]}", style="#FFFFFF`"))
        elif upper_letter in phonetic_symbols:
            result.append(Text(f"{phonetic_symbols[upper_letter]}", style="#E24E4E"))
        elif upper_letter in nato_phonetic_numbers:
            result.append(Text(f"{nato_phonetic_numbers[upper_letter]}", style="#74A9E0"))
    console.print(*result, sep="\n")




def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Transform text into the NATO phonetic alphabet for oral transmission.')

    # Add the arguments
    parser.add_argument('text', type=str, help='Text to transform into the NATO phonetic alphabet.')

    # Parse the arguments
    args = parser.parse_args()

    # Transform the text into the NATO phonetic alphabet
    nato_phonetic_text = f"{transform_text_to_nato_phonetic(args.text)}"


if __name__ == '__main__':
    main()
