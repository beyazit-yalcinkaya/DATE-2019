#An Exact Schedulability Test for Non-Preemptive Self-Suspending Real-Time Tasks

This repository has the models and experiments of our DATE 2019 paper: [An Exact Schedulability Test for Non-Preemptive Self-Suspending Real-Time Tasks](https://people.mpi-sws.org/~bbb/papers/pdf/date19.pdf).

##Models

UPPAAL models for periodic and sporadic tasks are in the `models/` directory.

##Experiments for Periodic Tasks
Experiments for periodic tasks are in the `efficient_new_model_experiments/` directory. To run the experiments follow the instructions below.

	cd efficient_new_model_experiments
	unzip inputs.zip
	cd scripts
	./test_beyazit.sh

After running these steps, the outputs of the experiments should be in the `outputs/` directory.


##Experiments for Sporadic Tasks
Experiments for sporadic tasks are in the `SPORADIC_efficient_new_model_experiments/` directory. To run the experiments follow the instructions below.

	cd SPORADIC_efficient_new_model_experiments
	unzip inputs.zip
	cd scripts
	./test_beyazit.sh
	
After running these steps, the outputs of the experiments should be in the `outputs/` directory.



##Output Format
Output fields of the `*.out` files are in the following order.

	1. Input File Name
	2. Schedulability Result
	3. Number of Jobs in Hyperperiod
	4. Explored States
	5. Time
	6. Virtual Memory
	7. Resident Memory
	8. Minimum Period
	9. Maximum Period
	
In corresponding `scripts/` directories, there are Python scripts called `organize_output.py` for output processing.

This project uses Python2 and it is developed on/for Linux systems.