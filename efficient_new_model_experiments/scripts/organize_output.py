import os
import pybootstrap as pb
import numpy as np

vary_M_and_U_results = open("../results/vary_M_and_U_results.csv", "w+")
vary_N_results = open("../results/vary_N_results.csv", "w+")
vary_N_Jitter_results = open("../results/vary_N_Jitter_results.csv", "w+")
vary_Segment_results = open("../results/vary_Segment_results.csv", "w+")
vary_U_prime_and_b_results = open("../results/vary_U_prime_and_b_results.csv", "w+")
vary_M_and_U_n2_results = open("../results/vary_M_and_U_for_N=2_results.csv", "w+")

vary_M_and_U_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")
vary_N_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")
vary_N_Jitter_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")
vary_Segment_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")
vary_U_prime_and_b_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")
vary_M_and_U_n2_results.write("N, M, U, U_prime, b, S, Sporadic Count, Schedulability Percentage, Timeout Percentage, Time (Average), Time (Lower Bootstrap Average), Time (Upper Bootstrap Average), Time (Median), Time (First Quantile), Time (Third Quantile), Time (5 Percentile), Time (95 Percentile), Only Schedulable Time (Average), Only Schedulable Time (Lower Bootstrap Average), Only Schedulable Time (Upper Bootstrap Average), Only Schedulable Time (Median), Only Schedulable Time (First Quantile), Only Schedulable Time (Third Quantile), Only Schedulable Time (5 Percentile), Only Schedulable Time (95 Percentile), Time with timeouts (Average), Time with timeouts (Lower Bootstrap Average), Time with timeouts (Upper Bootstrap Average), Time with timeouts (Median), Time with timeouts (First Quantile), Time with timeouts (Third Quantile), Time with timeouts (5 Percentile), Time with timeouts (95 Percentile)\n")

def organize(file_name, results_file, N, M, U, U_prime, b, S, k, Sp):
	schedulability_count = 0
	timeout_count = 0
	list_time = []
	list_time_schedulable = []
	list_time_timeouts = []
	for i in range(1, k + 1):
		result = open("../outputs/" + file_name + str(i) + ".out", "r").read().split(", ")
		if len(result) == 1:
			continue
		schedulability_result = result[1].strip()
		try:
			old_result = open("../old_outputs/" + file_name + str(i) + ".out", "r").read().split(", ")
			old_schedulability_result = old_result[1]
			if (old_schedulability_result == "1" and schedulability_result == "0") or (old_schedulability_result == "0" and schedulability_result == "1"):
				print file_name + str(i) + ".out", "Old:", old_schedulability_result, "New:", schedulability_result
		except:
			pass
		number_of_jobs_in_hyperperiod = result[2].strip()
		explored_states = result[3]
		time = result[4]
		virtual_memory = result[5]
		resident_memory = result[6]
		if schedulability_result != "Timedout":
			memory = float(virtual_memory) + float(resident_memory)
		else: memory = '-'
		minimum_period = result[7]
		maximum_period = result[8][:-1]
		
		if schedulability_result != "Timedout":
			list_time.append(float(time))
			list_time_timeouts.append(float(time))
			if '1' in schedulability_result:
				schedulability_count += 1
				list_time_schedulable.append(float(time))
		else:
			timeout_count += 1
			list_time_timeouts.append(3600.0)


	results_file.write(str(N) + ", " + str(M) + ", " + str(U) + ", " + str(U_prime) + ", " + str(b) + ", " + str(S) + ", " + str(Sp) + ", " + str(float(schedulability_count) / float(k) * 100) + ", " + str(float(timeout_count) / float(k) * 100))
	
	list_time = sorted(list_time)
	list_time_schedulable = sorted(list_time_schedulable)
	list_time_timeouts = sorted(list_time_timeouts)

	if len(list_time) > 0:

		average_time = np.average(list_time)
		lower_time, upper_time = pb.bootstrap(list_time)
		median_time = np.median(list_time)
		first_quantile_time = np.percentile(list_time, 25)
		third_quantile_time = np.percentile(list_time, 75)
		five_percentile_time = np.percentile(list_time, 5)
		ninety_five_percentile_time = np.percentile(list_time, 95)
		results_file.write(", " + str(average_time) + ", " + str(lower_time) + ", " + str(upper_time) + ", " + str(median_time) + ", " + str(first_quantile_time) + ", " + str(third_quantile_time) + ", " + str(five_percentile_time) + ", " + str(ninety_five_percentile_time))

	else:
		results_file.write(", -, -, -, -, -, -, -, -")

	if len(list_time_schedulable) > 0:

		average_time_schedulable = np.average(list_time_schedulable)
		lower_time_schedulable, upper_time_schedulable = pb.bootstrap(list_time_schedulable)
		median_time_schedulable = np.median(list_time_schedulable)
		first_quantile_time_schedulable = np.percentile(list_time_schedulable, 25)
		third_quantile_time_schedulable = np.percentile(list_time_schedulable, 75)
		five_percentile_time_schedulable = np.percentile(list_time_schedulable, 5)
		ninety_five_percentile_time_schedulable = np.percentile(list_time_schedulable, 95)
		results_file.write(", " + str(average_time_schedulable) + ", " + str(lower_time_schedulable) + ", " + str(upper_time_schedulable) + ", " + str(median_time_schedulable) + ", " + str(first_quantile_time_schedulable) + ", " + str(third_quantile_time_schedulable) + ", " + str(five_percentile_time_schedulable) + ", " + str(ninety_five_percentile_time_schedulable))

	else:
		results_file.write(", -, -, -, -, -, -, -, -")

	if len(list_time_timeouts) > 0:

		average_time_timeouts = np.average(list_time_timeouts)
		lower_time_timeouts, upper_time_timeouts = pb.bootstrap(list_time_timeouts)
		median_time_timeouts = np.median(list_time_timeouts)
		first_quantile_time_timeouts = np.percentile(list_time_timeouts, 25)
		third_quantile_time_timeouts = np.percentile(list_time_timeouts, 75)
		five_percentile_time_timeouts = np.percentile(list_time_timeouts, 5)
		ninety_five_percentile_time_timeouts = np.percentile(list_time_timeouts, 95)
		results_file.write(", " + str(average_time_timeouts) + ", " + str(lower_time_timeouts) + ", " + str(upper_time_timeouts) + ", " + str(median_time_timeouts) + ", " + str(first_quantile_time_timeouts) + ", " + str(third_quantile_time_timeouts) + ", " + str(five_percentile_time_timeouts) + ", " + str(ninety_five_percentile_time_timeouts) + "\n")

	else:
		results_file.write(", -, -, -, -, -, -, -, -\n")

	return False

N = 10
U_prime = 0
b = 0
S = 1
for U in [0.3, 0.5, 0.7]:
	for M in [1, 2, 4, 8]:
		if organize("vary_M_and_U_N=10_M=" + str(M) + "_U=" + str(U) + "_task_set_", vary_M_and_U_results, N, M, U, U_prime, b, S, 500, 0):
			break
vary_M_and_U_results.close()
print "vary_M_and_U Finished"

U = 0.3
U_prime = 0
b = 0
S = 1
for M in [1, 2, 4, 8]:
	for N in range(3, 61, 3):
		if organize("vary_N_N=" + str(N) + "_M=" + str(M) + "_U=0.3_task_set_", vary_N_results, N, M, U, U_prime, b, S, 500, 0):
			break
vary_N_results.close()
print "vary_N Finished"


U = 0.3
U_prime = 0
b = 0
S = 1
for M in [1, 2, 4, 8]:
	for N in range(3, 16, 3):
		if M == 16 and N == 3: continue
		if organize("vary_N_Jitter_N=" + str(N) + "_M=" + str(M) + "_U=0.3_task_set_", vary_N_Jitter_results, N, M, U, U_prime, b, S, 100, 0):
			break
vary_N_Jitter_results.close()
print "vary_N_Jitter Finished"
		

N = 10
U = 0.3
U_prime = 0
b = 0
for S in [1, 4, 7, 10, 13, 16]:
	for M in [1, 2]:
		if organize("vary_Segment_N=10_M=" + str(M) + "_U=0.3_segment=" + str(S) + "_task_set_", vary_Segment_results, N, M, U, U_prime, b, S, 100, 0):
			break

vary_Segment_results.close()
print "vary_Segment Finished"



N = 5
U = 0
S = 1
for M in [1, 2]:
	for U_prime in [0.5, 0.7, 0.9]:
		for b in [0.3, 0.5, 0.7]:
			if organize("vary_U_prime_and_b_N=5_M=" + str(M) + "_U_prime=" + str(U_prime) + "_b=" + str(b) + "_task_set_", vary_U_prime_and_b_results, N, M, U, U_prime, b, S, 100, 0):
				break
vary_U_prime_and_b_results.close()
print "vary_U_prime_and_b Finished"

N = 2
U_prime = 0
b = 0
S = 1
for U in [0.3, 0.5, 0.7]:
	for M in [1]:
		if organize("vary_N_N=2_M=" + str(M) + "_U=" + str(U) + "_task_set_", vary_M_and_U_n2_results, N, M, U, U_prime, b, S, 500, 0):
			break
vary_M_and_U_n2_results.close()
print "vary_M_and_U_n2 Finished"

