import argparse
import string
from collections import Counter

def letter_frequency(input_file, output_file=None):
    """ Reads a file, calculates letter frequency, and optionally saves results in a formatted style. """
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

        # Generate predicted keypairs (5 most frequent)
        frequency_order = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
        predicted_keypairs = {}
        for i in range(min(5, len(sorted_counts))):  # Only process if at least 5 letters exist
            predicted_keypairs[sorted_counts[i][0]] = frequency_order[i]


        # Prepare formatted output
        output_text = "# Letter Frequency Analysis\n"
        output_text += f"# Total characters analyzed: {total_analyzed:,}\n"
        output_text += "\n# LET   COUNT      PERCENT   BAR GRAPH\n"

        max_count = sorted_counts[0][1]  # Highest frequency for scaling bar graph

        for letter, count in sorted_counts:
            percent = (count / total_analyzed) * 100
            bar_length = int((count / max_count) * 20)  # Scale bar graph to 20 max units
            bar = "█" * bar_length  # Create bar graph using Unicode block

            # Format output with right-aligned columns
            output_text += f"  {letter.upper()}  {count/1e9:6.1f} B   {percent:6.2f}%   {bar}\n"

        # Append Predicted Key Mappings
        output_text += "\n# Predicted Key Pairs (Top 5 Most Frequent Letters)\n"
        output_text += f"  Most popular char -> {sorted_counts[0][0].upper()} -> {predicted_keypairs[sorted_counts[0][0]]}\n"
        output_text += f"  2nd popular char -> {sorted_counts[1][0].upper()} -> {predicted_keypairs[sorted_counts[1][0]]}\n"
        output_text += f"  3rd popular char -> {sorted_counts[2][0].upper()} -> {predicted_keypairs[sorted_counts[2][0]]}\n"
        output_text += f"  4th popular char -> {sorted_counts[3][0].upper()} -> {predicted_keypairs[sorted_counts[3][0]]}\n"
        output_text += f"  5th popular char -> {sorted_counts[4][0].upper()} -> {predicted_keypairs[sorted_counts[4][0]]}\n"

        # Save or display results
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
    parser = argparse.ArgumentParser(description="Letter Frequency Analysis (LFA) with formatted output")
    parser.add_argument("-f", "--file", required=True, help="Input text file for analysis")
    parser.add_argument("-o", "--output", help="Output file to save results (optional)")

    args = parser.parse_args()

    letter_frequency(args.file, args.output)


