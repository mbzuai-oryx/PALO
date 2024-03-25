#!/bin/bash

export MULTILINGUAL_LLAVA_BENCH_PATH="data/multilingual-llava-bench-in-the-wild"
export OUTPUT_DIR="evaluation"
export IMAGES=p"$MULTILINGUAL_LLAVA_BENCH_PATH/images"

#export MODEL="/path/to/palo-v1.5-7b-665en_150K_of_arr_chi_hin_spa_ben_fr_jap_rus_ur"
#export MODEL_NAME="palo-v1.5-7b-665en_150K_of_arr_chi_hin_spa_ben_fr_jap_rus_ur"
#export OPENAI_API_KEY="write your open-ai key"

MODEL=$1
MODEL_NAME=$2
export OPENAI_API_KEY=$3

export PYTHONPATH="./:$PYTHONPATH"

# 1.English
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/english/questions.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/english/answers_gpt4.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/english/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_English.jsonl

# 2.Chinese
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/chinese/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/chinese/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/chinese/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Chinese.jsonl

# 3.Spanish
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/spanish/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/spanish/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/spanish/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Spanish.jsonl

# 4.French
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/french/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/french/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/french/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_French.jsonl

# 6.Russian
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/russian/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/russian/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/russian/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Russian.jsonl

# 7.Arabic
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/arabic/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/arabic/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/arabic/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Arabic.jsonl

# 8.Bengali
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/bengali/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/bengali/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/bengali/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Bengali.jsonl

# 9.Hindi
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/hindi/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/hindi/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/hindi/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Hindi.jsonl

# 10.Urdu
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/urdu/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/urdu/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/urdu/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Urdu.jsonl

# 11.Japanese
bash scripts/eval/llavabench.sh "$IMAGES" "$MODEL" "$MULTILINGUAL_LLAVA_BENCH_PATH"/japanese/corrected/question.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/japanese/corrected/answers.jsonl "$MULTILINGUAL_LLAVA_BENCH_PATH"/japanese/corrected/context.jsonl "$OUTPUT_DIR" "$MODEL_NAME"_Japanese.jsonl
