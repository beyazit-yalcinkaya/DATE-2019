#!/bin/bash

#Get the number of CPUs we can use
NUM_CPUS=`getconf _NPROCESSORS_ONLN`

INPUT_DIR="/RTS/cluster/work/beyazit/efficient_new_model_experiments/inputs" # Placeholder!
OUTPUT_DIR="/RTS/cluster/work/beyazit/efficient_new_model_experiments/outputs" # Placeholder!

ANALYSIS_CMD="python /RTS/cluster/work/beyazit/efficient_new_model_experiments/scripts/test_beyazit.py"

# Create output directory if it doesn't exist yet.
mkdir -p $OUTPUT_DIR
# Go there
cd $OUTPUT_DIR
find ${INPUT_DIR} -iname *.csv \
    | sort -R                        \
    | xargs -n 1 --max-procs=${NUM_CPUS} /RTS/cluster/work/beyazit/efficient_new_model_experiments/scripts/launch-exp.sh $ANALYSIS_CMD