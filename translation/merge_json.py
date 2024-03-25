import json
import argparse
from tqdm import tqdm
import random


def parse_args():
    parser = argparse.ArgumentParser(description="Merge multiple json files into one.")
    parser.add_argument("--json_paths", required=True, help="Comma-separated paths of JSON files")
    parser.add_argument("--output_file", required=True, help="Output file name")
    return parser.parse_args()


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    args = parse_args()

    # Split the input paths and remove any whitespace
    json_paths = [path.strip() for path in args.json_paths.split(',')]

    merged_content = []

    for path in tqdm(json_paths):
        merged_content += load_json(path)

    random.shuffle(merged_content)

    with open(args.output_file, 'w') as output_file:
        json.dump(merged_content, output_file, ensure_ascii=True)


if __name__ == "__main__":
    main()
