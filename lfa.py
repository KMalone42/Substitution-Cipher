import argparse
import string
from collections import Counter

def letter_frequency(input_file, output_file=None):
    """ Reads a file, calculates letter frequency, and optionally saves results to a file. """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        # Filter only alphabetic characters
        text = [char for char in text if char in string.ascii_lowercase]
        total_analyzed = len(text)
        # Count letter occurrences
        letter_counts = Counter(text)

        # Sort by frequency (descending)
        sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

        # Prepare output
        output_text = "\nLetter Frequency Analysis:\n"
        output_text +=f"Total characters analyzed: {total_analyzed}\n" 
        output_text += "\n".join(f"{letter}: {count}" for letter, count in sorted_counts)

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output_text)
            print(f"[✓] Results saved to '{output_file}'")
        else:
            print(output_text)

    except FileNotFoundError:
        print(f"[!] Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Letter Frequency Analysis (LFA)")
    parser.add_argument("-f", "--file", required=True, help="Input text file for analysis")
    parser.add_argument("-o", "--output", help="Output file to save results (optional)")

    args = parser.parse_args()

    letter_frequency(args.file, args.output)