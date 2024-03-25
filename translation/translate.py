import json
import argparse
import os
import random
from tqdm import tqdm
import openai
from openai import AsyncOpenAI
import asyncio
from utils import *


# Function to get the ChatGPT prompt
def get_chatgpt_prompt(language, english_str):
    if language.lower() == "arabic":
        return get_chatgpt_prompt_to_arabic(english_str)
    elif language.lower() == "chinese":
        return get_chatgpt_prompt_chinese(english_str)
    elif language.lower() == "spanish":
        return get_chatgpt_prompt_spanish(english_str)
    elif language.lower() == "hindi":
        return get_chatgpt_prompt_hindi(english_str)
    elif language.lower() == "french":
        return get_chatgpt_prompt_french(english_str)
    elif language.lower() == "german":
        return get_chatgpt_prompt_german(english_str)
    elif language.lower() == "russian":
        return get_chatgpt_prompt_russian(english_str)
    elif language.lower() == "urdu":
        return get_chatgpt_prompt_urdu(english_str)
    elif language.lower() == "bengali":
        return get_chatgpt_prompt_bengali(english_str)
    elif language.lower() == "japanese":
        return get_chatgpt_prompt_japanese(english_str)
    else:
        raise NotImplementedError


# Asynchronous function to translate text to Arabic using GPT-3.5
async def translate(client, language, english_str):
    chat_completion = await client.chat.completions.create(
        messages=get_chatgpt_prompt(language, english_str),
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content
    return response.strip()


# Asynchronous worker function to process a chunk of data
async def async_worker(language, data_chunk, chunk, api_key, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)  # Create the output directory if not exists already

    local_cache = {}

    client = AsyncOpenAI(api_key=api_key)
    counter = 0
    for sample in tqdm(data_chunk, desc=f"Process {os.getpid()} ({chunk})"):
        sample_id = str(sample['id']).split('/')[-1]
        counter += 1
        if os.path.exists(f"{output_dir_path}/{counter}_{sample_id}.json"):
            continue
        conversations = sample['conversations']
        sample[f"{language}_conversation"] = []
        try:
            for conv in conversations:
                this_conversation = {}
                for key, value in conv.items():
                    if key == "value":
                        if "<image>" in value:
                            value = value.replace("<image>\n", "").replace("\n<image>", "").strip()

                            if value in local_cache.keys():
                                value_translated = local_cache[value]
                            else:
                                value_translated = await translate(client, language, value)
                                local_cache[value] = value_translated

                            if random.randint(0, 100) % 2 == 0:
                                value_translated = f"{value_translated}\n<image>"
                            else:
                                value_translated = f"<image>\n{value_translated}"

                        else:
                            if value in local_cache.keys():
                                value_translated = local_cache[value]
                            else:
                                value_translated = await translate(client, language, value)
                                local_cache[value] = value_translated
                    else:
                        value_translated = value

                    this_conversation[key] = value_translated
                sample[f"{language}_conversation"].append(this_conversation)

            with open(f"{output_dir_path}/{counter}_{sample_id}.json", 'w') as f:
                json.dump(sample, f, ensure_ascii=False)
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.response)


# Synchronous wrapper to run the asynchronous worker
def run_async_worker(language, data_chunk, chunk, api_key, output_dir_path):
    asyncio.run(async_worker(language, data_chunk, chunk, api_key, output_dir_path))


# Main function to set up and execute the script
def parse_args():
    parser = argparse.ArgumentParser(description="Translation")
    parser.add_argument("--input_json_path", required=True)
    parser.add_argument("--output_dir_path", required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--openai_api_key", required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    os.makedirs(args.output_dir_path, exist_ok=True)

    with open(args.input_json_path, 'r') as f:
        data = json.load(f)

    chunk = os.path.basename(args.input_json_path)
    run_async_worker(args.language, data, chunk, args.openai_api_key, args.output_dir_path)


if __name__ == "__main__":
    main()
