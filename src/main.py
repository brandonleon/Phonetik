"""
CLI tool to transform text into the NATO phonetic alphabet for oral transmission.
"""

import argparse
from constants import nato_combined

def transform_text_to_nato_phonetic(text: str) -> str:
    """
    Transform a text into the NATO phonetic alphabet for oral transmission, one word on each line.
    TODO: Add support for color coding numbers, symbols, and letters.
    Args:
        text (str): Text to transform.

    Returns:
        str: Text transformed into the NATO phonetic alphabet.
    """
    return '\n'.join([nato_combined[letter.upper()] for letter in text if letter.upper() in nato_combined])

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Transform text into the NATO phonetic alphabet for oral transmission.')

    # Add the arguments
    parser.add_argument('text', type=str, help='Text to transform into the NATO phonetic alphabet.')

    # Parse the arguments
    args = parser.parse_args()

    # Transform the text into the NATO phonetic alphabet
    nato_phonetic_text = f"{transform_text_to_nato_phonetic(args.text)}"

    # Print the transformed text
    print(nato_phonetic_text)

if __name__ == '__main__':
    main()