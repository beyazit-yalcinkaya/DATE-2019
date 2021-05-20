import math
import random
import numpy
import fractions
import os

def StaffordRandFixedSum(n, u, nsets):
    if n == 1:
        return numpy.tile(numpy.array([u]),[nsets,1])
    k = numpy.floor(u)
    s = u
    step = 1 if k < (k-n+1) else -1
    s1 = s - numpy.arange( k, (k-n+1)+step, step )
    step = 1 if (k+n) < (k-n+1) else -1
    s2 = numpy.arange( (k+n), (k+1)+step, step ) - s
    tiny = numpy.finfo(float).tiny
    huge = numpy.finfo(float).max
    w = numpy.zeros((n, n+1))
    w[0,1] = huge
    t = numpy.zeros((n-1,n))
    for i in numpy.arange(2, (n+1)):
        tmp1 = w[i-2, numpy.arange(1,(i+1))] * s1[numpy.arange(0,i)]/float(i)
        tmp2 = w[i-2, numpy.arange(0,i)] * s2[numpy.arange((n-i),n)]/float(i)
        w[i-1, numpy.arange(1,(i+1))] = tmp1 + tmp2;
        tmp3 = w[i-1, numpy.arange(1,(i+1))] + tiny;
        tmp4 = numpy.array( (s2[numpy.arange((n-i),n)] > s1[numpy.arange(0,i)]) )
        t[i-2, numpy.arange(0,i)] = (tmp2 / tmp3) * tmp4 + (1 - tmp1/tmp3) * (numpy.logical_not(tmp4))
    m = nsets
    x = numpy.zeros((n,m))
    rt = numpy.random.uniform(size=(n-1,m))
    rs = numpy.random.uniform(size=(n-1,m))
    s = numpy.repeat(s, m);
    j = numpy.repeat(int(k+1), m);
    sm = numpy.repeat(0, m);
    pr = numpy.repeat(1, m);
    for i in numpy.arange(n-1,0,-1):
        e = ( rt[(n-i)-1,...] <= t[i-1,j-1] )
        sx = rs[(n-i)-1,...] ** (1/float(i))
        sm = sm + (1-sx) * pr * s/float(i+1)
        pr = sx * pr
        x[(n-i)-1,...] = sm + pr * e
        s = s - e
        j = j - e
    x[n-1,...] = sm + pr * s
    for i in xrange(0,m):
        x[...,i] = x[numpy.random.permutation(n),i]
    return numpy.transpose(x).tolist()

def lcm(x, y):
   lcm = (x * y) / fractions.gcd(x,y)
   return lcm

def pick():
    temp = random.randint(0, 84)
    if temp < 3:
        return 0
    elif temp < 5:
        return 1
    elif temp < 7:
        return 2
    elif temp < 32:
        return 3
    elif temp < 57:
        return 4
    elif temp < 60:
        return 5
    elif temp < 80:
        return 6
    elif temp < 81:
        return 7
    elif temp < 85:
        return 8

def task_set_generator():
    #### Uniprocessor Case ####
    U = 0.3
    M = 1
    period_values = [10, 20, 50, 100, 200, 500, 1000, 2000, 10000]
    path = os.getcwd() + "/../inputs/"
    print M
    for N in [2, 4, 5, 7, 8, 10]:
        print N
        for i in range(1, 101, 1):
            output_file = open(path + "vary_N_N=" + str(N) + "_M=" + str(M) + "_U=" + str(U) + "_task_set_" + str(i) + ".csv" , "w+")
            while True:
                periods = []
                for j in range(N):
                    periods.append(period_values[pick()])
                periods = sorted(periods)
                u_list = StaffordRandFixedSum(N, U * M, 1)[0]
                wcets = [math.ceil(u_list[0] * periods[0])]
                t_1 = periods[0]
                c_1_max = wcets[0]
                f = True
                for j in range(1, N):
                    wcets.append(math.ceil(u_list[j] * periods[j]))
                    if wcets[j] > 2 * (t_1 - c_1_max):
                        f = False
                        break
                if f:
                    break
            for j in range(N):
                output_file.write("T, " + str(j + 1) + ", " + str(periods[j]) + ", " + str(periods[j]) + "\n")
                output_file.write("V, " + str(j + 1) + ", 1, 0.0, 0.0, " + str(math.floor(0.1 * wcets[j])) + ", " + str(wcets[j]) + "\n")
            output_file.close()
    #### Multiprocessor Case ####
    for M in [2]:
        print M
        for N in [2, 4, 5, 7, 8, 10]:
            print N
            for i in range(1, 101, 1):
                while True:
                    periods = []
                    for j in range(N):
                        periods.append(period_values[pick()])
                    periods = sorted(periods)
                    u_list = StaffordRandFixedSum(N, U * M, 1)[0]
                    wcets = map(lambda x, y: math.ceil(x * y), u_list, periods)
                    output_file = open(path + "vary_N_N=" + str(N) + "_M=" + str(M) + "_U=" + str(U) + "_task_set_" + str(i) + ".csv" , "w+")
                    for j in range(N):
                        output_file.write("T, " + str(j + 1) + ", " + str(periods[j]) + ", " + str(periods[j]) + "\n")
                        output_file.write("V, " + str(j + 1) + ", 1, 0.0, 0.0, " + str(wcets[j]) + ", " + str(wcets[j]) + "\n")
                    output_file.close()
                    schedulable = True#bool(int(os.popen("/RTS/cluster/work/bbb/exp/rtss18/tool/scripts/analyze-global-dag-task-set.sh -m " + str(M) + " --policy RM " + path + "vary_N_N=" + str(N) + "_M=" + str(M) + "_U=" + str(U) + "_task_set_" + str(i) + ".csv").read().split(", ")[1][1]))
                    if schedulable:
                        break
                output_file = open(path + "vary_N_N=" + str(N) + "_M=" + str(M) + "_U=" + str(U) + "_task_set_" + str(i) + ".csv" , "w+")
                for j in range(N):
                    output_file.write("T, " + str(j + 1) + ", " + str(periods[j]) + ", " + str(periods[j]) + "\n")
                    output_file.write("V, " + str(j + 1) + ", 1, 0.0, 0.0, " + str(math.floor(0.1 * wcets[j])) + ", " + str(wcets[j]) + "\n")
                output_file.close()
            
task_set_generator()
