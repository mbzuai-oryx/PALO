import argparse
import json
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import glob
import re


def parse_args():
    parser = argparse.ArgumentParser(description="Script to create training json file from the raw translations.")

    parser.add_argument("--json_dir_path", required=False, default="spanish_translation")
    parser.add_argument("--output_json_path", required=False, default="llava_instruct_150K_spanish_GPT3.5.json")
    parser.add_argument("--language", required=False, default="spanish")
    parser.add_argument("--append_coco", required=False, action="store_true")

    args = parser.parse_args()

    return args


def count_angle_brackets_with_re(input_string):
    pattern = r'<[^>]*>'
    matches = re.findall(pattern, input_string)
    return len(matches)


def filter_json(list_data_dict):
    image_conversations = 0
    non_image_conversations = 0
    corrupt_conversations = []

    for i in tqdm(range(len(list_data_dict))):
        sources = list_data_dict[i]
        if isinstance(i, int):
            sources = [sources]
        if 'image' in sources[0]:
            image_conversations += 1
            image_file = list_data_dict[i]['image']

            conversation = sources[0]['conversations']
            release = False
            if "english_conversations" in sources[0].keys():
                english_conversation = sources[0]['english_conversations']
            else:
                english_conversation = conversation
                release = True

            for conv, eng_conv in zip(conversation, english_conversation):
                if conv['from'] == "gpt":
                    if '<image>' in conv['value']:
                        corrupt_conversations.append(-100)
                        list_data_dict[i]['corrupt'] = True
                        print(f"Removed conversation as it contains <image> in gpt.")
                        break

                    angle_brackets_with_re = count_angle_brackets_with_re(conv['value'])
                    if angle_brackets_with_re > 1:
                        eng_angle_bracktes_with_re = count_angle_brackets_with_re(eng_conv['value'])
                        if angle_brackets_with_re != eng_angle_bracktes_with_re:
                            if not release:
                                corrupt_conversations.append(angle_brackets_with_re)
                                list_data_dict[i]['corrupt'] = True
                                break

            if 'corrupt' not in list_data_dict[i].keys():
                list_data_dict[i]['corrupt'] = False

        elif "<image>" in sources[0]['conversations'][0]['value']:
            print(f"{list_data_dict[i]} - 'image' not in sources however <image> in sources[0]")
        else:
            non_image_conversations += 1
    print(image_conversations, non_image_conversations, len(corrupt_conversations))

    return list_data_dict


def process_file(json_file_path):
    args = parse_args()
    language = args.language

    with open(json_file_path, 'r') as file:
        content = json.load(file)

    conversation_key = f"{language}_conversation"

    if 'image' in content.keys():
        if args.append_coco:
            content['image'] = f"coco/train2017/{content['image']}"
        else:
            content['image'] = f"{content['image']}"
    content['english_conversations'] = content['conversations']
    content['conversations'] = content[conversation_key]

    return content


def main():
    args = parse_args()

    # Use glob to find all JSON files in the directory and subdirectories
    json_files = glob.glob(f"{args.json_dir_path}/**/*.json", recursive=True)

    with Pool(cpu_count()) as p:
        merge_json_content = list(tqdm(p.imap(process_file, json_files), total=len(json_files)))

    merge_filtered_json_content = filter_json(merge_json_content)
    with open(args.output_json_path, 'w') as f:
        json.dump(merge_filtered_json_content, f)


if __name__ == "__main__":
    main()
