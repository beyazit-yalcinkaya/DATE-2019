#!/bin/bash

#Get the number of CPUs we can use
NUM_CPUS=`getconf _NPROCESSORS_ONLN`

INPUT_DIR="${PWD}/../inputs" # Placeholder!
OUTPUT_DIR="${PWD}/../outputs" # Placeholder!

ANALYSIS_CMD="python ${PWD}/../scripts/test_beyazit.py"

mkdir -p ${PWD}/../scripts/temp_models

# Create output directory if it doesn't exist yet.
mkdir -p $OUTPUT_DIR
# Go there
cd $OUTPUT_DIR
find ${INPUT_DIR} -iname *.csv \
    | sort -R                        \
    | xargs -n 1 --max-procs=${NUM_CPUS} ${PWD}/../scripts/launch-exp.sh $ANALYSIS_CMD