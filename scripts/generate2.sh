#! /bin/bash

scripts=$(dirname "$0")
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools
samples=$base/samples

mkdir -p $samples

num_threads=4
device=""

# Run model3
(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python generate.py \
        --data $data/grimm \
        --words 100 \
        --checkpoint $models/model3.pt \  # Adjusted checkpoint to model3
        --outf $samples/model3_sample  # Adjusted output file name
)

# Run model5
(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python generate.py \
        --data $data/grimm \
        --words 100 \
        --checkpoint $models/model5.pt \  # Adjusted checkpoint to model5
        --outf $samples/model5_sample  # Adjusted output file name
)
