This repository contains all experiments conducted for DATE 2019 paper and all the related TA models.

# TA_models Folder

It contains three sub-folder; models_for_UPPAAL, models_in_PDF_format, and models_to_put_paper.

## models_for_UPPAAL folder
Both periodic and sporadic models of exact test and the model of David 2009 can be found as well as the related queries for schedulability tests.

## models_in_PDF_format folder
pdf versions of all TA model can be found.

## models_to_put_paper

Modified version od exact test can be found in both xml and pdf format, it also contains a jpeg file of some code segments for the paper.


# experiments Folder

## task_set_generators Folder

All Python scripts for task set generatiom can be found in this folder. Before using any scripts please do not forget the change parameters and paths.

## exact_test Folder

input.zip and output.zip contain all task sets and the outputs, respectively. Results folder, contains both a raw results file and a file with time averages (also median, first quantile, etc.) for each experiment. Scripts folder, contains all the scripts for experiments. The experiments are parallelized. Before starting any experiments do not forget the change paths for input, output, and scripts in all folders. After making necesary changes for a new experiment, just run the script "test_beyazit.sh" (I did not have time to change name of the script so you can change the name of the script but if you change the name of the related python script too, please do not forget to modify other scripts too.)

## mitra_ecrts_2018 Folder

This folder has the same structure as exact_test Folder. Notice that, the input.zip contains task sets for only the experiments vary_N, vary_N_Jitter, and vary_M_and_U; however, existing task sets are same as the ones in the exact_test/inputs.zip.


## david_2009 Folder

This folder has a similar structure as exact_test and mitra_ecrts_2018 folders; however, experiments are sequential.


# Experiment Setup

Bosch periods x 10 is used in all experiments (due to UPPAAL's int limitations). for M = 1 the necessary test and for M > 1 we made a simulation with wcets (we only included task sets that are found to be schedulable after simulation). randfixedsum is used for splitting execution times and suspension times.

## vary M and U
M is from {1, 2, 4, 8}.
U is {0.3, 0.5, 0.7}.
N = 10.
Segment count = 1.
No sporadic task.
No suspension.
500 trials per case
## vary N
M is from {1, 2, 4, 8}.
U is {0.3}.
N = {3, 6, ..., 60}.
Segment count = 1.
No sporadic task.
No suspension.
500 trials per case.
## vary N with Jitter
M is from {1, 2, 4, 8}.
U is {0.3}.
N = {3, 6, ..., 60}.
Segment count = 1.
No sporadic task.
Jitter is picked randomly from [1, 5].
100 trials per case.
## vary Segment
M is from {1, 2}.
U is {0.3}.
N = 10.
Max segment count (S) is from {1, 4, 7, ... 16}. Segment count of each task is picked randomly from [1, min(S, total wcet)].
No sporadic task.
No suspension.
100 trials per case.
## vary Sporadic
M is from {1, 2}.
U is {0.3}.
N = 5.
Segment count = 1.
Sporadic task count is form [0, 5].
No suspension.
100 trials per case.
## vary U prime and b
M is from {1, 2}.
U_prime is from {0.5, 0.7, 0.9}.
b is from {0.3, 0.5, 0.7}.
N = 5.
Segment count is pick randomly form [1, min(5, total wcst, total wcet)].
No sporadic task.
Total suspension time = U * (b - 1), Total execution time = U * b, and they are splitted by randfixedsum. 
100 trials per case.

