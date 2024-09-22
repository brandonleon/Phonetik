import argparse
from rich.console import Console
from rich.text import Text

from constants import nato_phonetic_alphabet, phonetic_symbols, nato_phonetic_numbers

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

def transform_text_to_nato_phonetic(text: str, plain: bool) -> None:
    """
    Transform a text into the NATO phonetic alphabet for oral transmission, one word on each line.

    Args:
        text (str): Text to transform.
        plain (bool): Flag to indicate if the output should be plain text.

    Returns:
        None
    """
    console = Console(no_color=plain)
    result = [get_phonetic_representation(letter, plain) for letter in text]
    console.print(*result, sep="\n")

def main():
    parser = argparse.ArgumentParser(description='Transform text into the NATO phonetic alphabet for oral transmission.')
    parser.add_argument('text', type=str, help='Text to transform into the NATO phonetic alphabet.')
    parser.add_argument('--plain', action='store_true', help='Output plain text without formatting.')
    args = parser.parse_args()
    transform_text_to_nato_phonetic(args.text, args.plain)

if __name__ == '__main__':
    main()