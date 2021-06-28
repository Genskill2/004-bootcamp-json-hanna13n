# Add the functions in this file
import json
import math


def load_journal(journal):
    file = open(journal)
    data = json.load(file)
    return data


def compute_phi(data, eve):
    n11 = 0
    n00 = 0
    n10 = 0
    n01 = 0
    n1_ = 0
    n0_ = 0
    n_1 = 0
    n_0 = 0
    for i in data:
        if (i["squirrel"] and eve in i["events"]):
            n11 += 1
            n1_ += 1
            n_1 += 1
        elif (not i["squirrel"] and eve not in i["events"]):
            n00 += 1
            n0_ += 1
            n_0 += 1
        elif(i["squirrel"] and eve not in i["events"]):
            n10 += 1
            n1_ += 1
            n_0 += 1
        elif(not i["squirrel"] and eve in i["events"]):
            n01 += 1
            n0_ += 1
            n_1 += 1
    phi = (n11*n00-n10*n01)/math.sqrt(n1_*n0_*n_1*n_0)
    return phi


def compute_correlations(journal):
    data = load_journal(journal)
    corr = {}
    for i in data:
        for j in i["events"]:
            if j not in corr.keys():
                corr[j] = compute_phi(data, j)
    return corr


def diagnose(journal):
    corr = compute_correlations(journal)
    max_eve = ""
    max = -2
    min = 2
    min_eve = ""
    for key, value in corr.items():
        if(value > max):
            max = value
            max_eve = key
        if(value < min):
            min = value
            min_eve = key
    return max_eve, min_eve
