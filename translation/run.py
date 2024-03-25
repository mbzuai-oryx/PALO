import json
import os
import random
import argparse
import subprocess
from math import ceil


def parse_args():
    parser = argparse.ArgumentParser(description="Translate LLaVA Instruct")
    parser.add_argument("--llava_instruct_path", required=True)
    parser.add_argument("--temp_dir_path", required=True)
    parser.add_argument("--output_dir_path", required=True)
    parser.add_argument("--language", required=True, help="Supported languages are arabic, chinese, "
                                                          "spanish, hindi, french, german, russian, urdu, bengali "
                                                          "and japanese")
    parser.add_argument("--split", required=False, action="store_true")
    parser.add_argument("--openai_api_keys", required=True, type=lambda k: k.split(","),
                        help="Comma separated OpenAI API keys. More the keys, faster the translation will be.")
    args = parser.parse_args()
    return args


def split_data(input_json_path, num_splits, temp_dir_path):
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    # Shuffle the data list randomly
    random.shuffle(data)

    chunk_size = ceil(len(data) / num_splits)
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    file_paths = []
    for i, chunk in enumerate(chunks):
        chunk_file_path = os.path.join(temp_dir_path, f"chunk_{i}.json")
        with open(chunk_file_path, 'w') as f:
            json.dump(chunk, f, ensure_ascii=True)
        file_paths.append(chunk_file_path)

    return file_paths


def main():
    args = parse_args()

    os.makedirs(args.temp_dir_path, exist_ok=True)
    os.makedirs(args.output_dir_path, exist_ok=True)

    if args.split:
        file_paths = split_data(args.llava_instruct_path, len(args.openai_api_keys), args.temp_dir_path)
    else:
        file_paths = [f"{args.temp_dir_path}/{file}" for file in os.listdir(args.temp_dir_path)]

    processes = []
    for file_path, api_key in zip(file_paths, args.openai_api_keys):
        process = subprocess.Popen([
            "python", "translate.py",
            "--input_json_path", file_path,
            "--output_dir_path", f"{args.output_dir_path}/{os.path.basename(file_path)[:-5]}",
            "--openai_api_key", api_key,
            "--language", args.language
        ])
        processes.append(process)

    # Wait for all processes to complete
    for process in processes:
        process.wait()


if __name__ == "__main__":
    main()
