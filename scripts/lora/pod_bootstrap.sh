#!/bin/bash
# Install kohya sd-scripts on a RunPod 4090 and train a photoreal SDXL LoRA.
# Usage: pod_bootstrap.sh [--dry-run]
#
# Required environment:
#   CIVITAI_TOKEN   CivitAI API token (never echoed, never written to disk)
#   MODEL_URL       download URL of the SDXL checkpoint (e.g. Lustify V8)
#   DATASET_DIR     folder holding img_NN.jpg + img_NN.txt (default /workspace/dataset)
#   TRIGGER         the trigger word used in the captions (default mysubject)
#
# Optional environment:
#   OUTPUT_DIR      default /workspace/lora-out
#   STEPS           default 1200 (low, because a small set overfits fast)
#   RANK            default 16
#   LR              default 5e-5

set -euo pipefail

DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *)
      echo "error: unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

DATASET_DIR=${DATASET_DIR:-/workspace/dataset}
OUTPUT_DIR=${OUTPUT_DIR:-/workspace/lora-out}
TRIGGER=${TRIGGER:-mysubject}
STEPS=${STEPS:-1200}
RANK=${RANK:-16}
LR=${LR:-5e-5}
MODEL_PATH=/workspace/models/base.safetensors

if [ "$DRY_RUN" -eq 0 ]; then
  if [ -z "${CIVITAI_TOKEN:-}" ]; then
    echo "error: CIVITAI_TOKEN is not set" >&2
    exit 1
  fi
  if [ -z "${MODEL_URL:-}" ]; then
    echo "error: MODEL_URL is not set" >&2
    exit 1
  fi
  if [ ! -d "$DATASET_DIR" ]; then
    echo "error: DATASET_DIR does not exist: $DATASET_DIR" >&2
    exit 1
  fi
  CAPS=$(find "$DATASET_DIR" -maxdepth 1 -name '*.txt' | wc -l | tr -d ' ')
  IMGS=$(find "$DATASET_DIR" -maxdepth 1 \( -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' \) | wc -l | tr -d ' ')
  if [ "$CAPS" -ne "$IMGS" ]; then
    echo "error: $IMGS images but $CAPS captions — every image needs a .txt" >&2
    exit 1
  fi
  if grep -lq '\[' "$DATASET_DIR"/*.txt 2>/dev/null; then
    echo "warn: some captions still contain [placeholders]. Fill them in before training." >&2
  fi
fi

run() {
  if [ "$DRY_RUN" -eq 1 ]; then
    printf '[dry-run]'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

if [ "$DRY_RUN" -eq 0 ]; then
  if python3 -c "import torch" 2>/dev/null; then
    echo "torch already present, leaving it alone"
  else
    pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cu124
  fi
else
  echo "[dry-run] pip install torch torchvision only if missing"
fi
if [ "$DRY_RUN" -eq 0 ] && [ -f /workspace/.deps-ok ]; then
  echo "dependencies already installed, skipping"
else
  run bash -c 'cd /workspace/sd-scripts && python3 -m pip install -q -r requirements.txt'
  # sd-scripts predates transformers 5.x, which moved CLIPTextModel and breaks the import.
  run python3 -m pip install -q "transformers>=4.44,<4.50" "tokenizers>=0.20,<0.21" "diffusers>=0.28,<0.32"
  if [ "$DRY_RUN" -eq 0 ]; then touch /workspace/.deps-ok; fi
fi

if [ ! -d /workspace/sd-scripts/.git ]; then
  run git clone --depth 1 https://github.com/kohya-ss/sd-scripts.git /workspace/sd-scripts
fi

run mkdir -p /workspace/models "$OUTPUT_DIR"

if [ "$DRY_RUN" -eq 1 ]; then
  echo '[dry-run] curl -fL -H "Authorization: Bearer $CIVITAI_TOKEN" -o '"$MODEL_PATH"' "$MODEL_URL"'
else
  EXISTING=0
  [ -f "$MODEL_PATH" ] && EXISTING=$(wc -c < "$MODEL_PATH" | tr -d ' ')
  if [ "$EXISTING" -gt 1000000000 ]; then
    echo "checkpoint already present ($EXISTING bytes), skipping download"
  else
    curl -fL -H "Authorization: Bearer $CIVITAI_TOKEN" -o "$MODEL_PATH" "$MODEL_URL"
    SIZE=$(wc -c < "$MODEL_PATH" | tr -d ' ')
    if [ "$SIZE" -lt 1000000000 ]; then
      echo "error: checkpoint is only $SIZE bytes — download failed" >&2
      exit 1
    fi
  fi
fi

TRAIN_ARGS=(
  "--pretrained_model_name_or_path=$MODEL_PATH"
  "--train_data_dir=$DATASET_DIR"
  "--output_dir=$OUTPUT_DIR"
  "--output_name=likeness"
  "--resolution=1024"
  "--train_batch_size=1"
  "--max_train_steps=$STEPS"
  "--learning_rate=$LR"
  "--text_encoder_lr=1e-5"
  "--lr_scheduler=cosine"
  "--network_module=networks.lora"
  "--network_dim=$RANK"
  "--network_alpha=$((RANK / 2))"
  "--optimizer_type=AdamW8bit"
  "--mixed_precision=fp16"
  "--save_every_n_steps=250"
  "--save_model_as=safetensors"
  "--caption_extension=.txt"
  "--shuffle_caption"
  "--seed=42"
)

if [ "$DRY_RUN" -eq 1 ]; then
  echo '[dry-run] cd /workspace/sd-scripts && python3 sdxl_train_network.py'
  printf '  %s\n' "${TRAIN_ARGS[@]}"
  exit 0
fi

cd /workspace/sd-scripts
python3 sdxl_train_network.py "${TRAIN_ARGS[@]}"

echo "training finished. checkpoints:"
ls -1 "$OUTPUT_DIR"/*.safetensors
echo "pick one by test render, then pull it back with pull_lora.sh"
