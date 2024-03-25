#!/bin/bash

export PYTHONPATH="./:$PYTHONPATH"

BASE_LLM_PATH=$1
JSON_PATH=$2
PROJECTOR_CKPT_PATH=$3
PROJECTION_NAME=$4
OUTPUT_PATH=$5
ZERO_LEVEL=$6
LR=$7


deepspeed palo/train/train_mem.py \
    --lora_enable True --lora_r 128 --lora_alpha 256 --mm_projector_lr 2e-5 \
    --deepspeed ./scripts/"zero$ZERO_LEVEL.json" \
    --model_name_or_path "$BASE_LLM_PATH" \
    --version v1 \
    --data_path "$JSON_PATH" \
    --image_folder ./data \
    --vision_tower openai/clip-vit-large-patch14-336 \
    --pretrain_mm_mlp_adapter "$PROJECTOR_CKPT_PATH" \
    --mm_projector_type "$PROJECTION_NAME" \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio pad \
    --group_by_modality_length True \
    --bf16 True \
    --output_dir "$OUTPUT_PATH" \
    --num_train_epochs 1 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 50000 \
    --save_total_limit 1 \
    --learning_rate "$LR" \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True \
    --report_to none
