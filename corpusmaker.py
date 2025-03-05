import argparse

def combine_files(input_files, output_file):
    """ Combines multiple text files into one output file. """
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file in input_files:
                try:
                    with open(file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content + "\n\n")  # Add spacing between files
                    print(f"[✓] Added '{file}' to '{output_file}'")
                except FileNotFoundError:
                    print(f"[!] Warning: File '{file}' not found, skipping.")
        
        print(f"[✓] All valid files merged into '{output_file}'")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine multiple text files into one")
    parser.add_argument("-f", "--files", nargs="+", required=True, help="List of input text files")
    parser.add_argument("-o", "--output", required=True, help="Output file to save merged content")

    args = parser.parse_args()

    combine_files(args.files, args.output)