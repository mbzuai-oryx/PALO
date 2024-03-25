#!/bin/bash

IMAGES=$1
MODEL=$2
QUESTIONS=$3
ANSWERS=$4
CONTEXT=$5
OUTPUT_DIR=$6
OUTPUT_FILE=$7

python palo/eval/model_vqa.py \
    --model-path "$MODEL" \
    --question-file "$QUESTIONS" \
    --image-folder "$IMAGES" \
    --answers-file "$OUTPUT_DIR/$OUTPUT_FILE" \
    --temperature 0 \
    --conv-mode vicuna_v1

mkdir -p "$OUTPUT_DIR/reviews"

python palo/eval/eval_gpt_review_bench.py \
    --question "$QUESTIONS" \
    --context "$CONTEXT" \
    --rule palo/eval/table/rule.json \
    --answer-list \
        "$ANSWERS" \
        "$OUTPUT_DIR/$OUTPUT_FILE" \
    --output \
        "$OUTPUT_DIR/reviews/$OUTPUT_FILE"

python palo/eval/summarize_gpt_review.py -f "$OUTPUT_DIR/reviews/$OUTPUT_FILE"
