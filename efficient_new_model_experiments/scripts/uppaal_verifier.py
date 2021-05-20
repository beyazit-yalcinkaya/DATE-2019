import os

"""
    A general function that can be applied to any framework using UPPAAL.
    All parameters of the function must be provided by the user.
    Output format:
        File Name, Result, Number of jobs in hyperperiod, Explored states, Time (seconds), Virtual memory (KB), Resident memory (KB), Minimum period, Maximum period
"""

def verify_xml_file(N, xml_file_name , q_file_name, min_period, max_period, number_of_jobs, csv_file_name, timeout_value):
    output = os.popen("timeout " + timeout_value + " ./../scripts/verifyta -C -S1 -b -u " + xml_file_name + " " + q_file_name).read()
    return_value = 0
    if "Formula is satisfied." in output:
        Result = "1"
    elif "Formula MAY be satisfied." in output:
        Result = "May be schedulable"
    elif "Formula MAY NOT be satisfied." in output:
        Result = "May not be schedulable"
    elif "Formula is NOT satisfied." in output:
        Result = "0"
    else:
        return_value = 1
        Result = "Timedout"
    if Result == "Timedout":
        output_line = csv_file_name + ", " + Result + ", " + number_of_jobs + ", -, -, -, -, " + min_period + ", " + max_period
    else:
        output = output.split("\n")
        time = str(float(output[11].split(" ")[-2]) * 0.001)
        states_explored = output[10].split(" ")[-2]
        virtual_memory = output[12].split(" ")[-2]
        resident_memory = output[13].split(" ")[-2]
        output_line = csv_file_name + ", " + Result + ", " + number_of_jobs + ", " + states_explored + ", " + time + ", " + virtual_memory + ", " + resident_memory + ", " + min_period + ", " + max_period
    print output_line
    os.system("rm " + xml_file_name)
    os.system("rm " + q_file_name)
    return return_value

