# Add the functions in this file
import json
import math
import sys


def load_journal(journal):
    file = open(journal)
    data = json.load(file)
    return data


def compute_phi(journal, eve):
    data = load_journal(journal)
    n11 = 0
    n00 = 0
    n10 = 0
    n01 = 0
    n1_ = 0
    n0_ = 0
    n_1 = 0
    n_0 = 0
    for i in data:
        if (i['squirrel']):
            n1_ += 1
            if (eve in i["events"]):
                n11 += 1
                n_1 += 1
            else:
                n_0 += 1
                n10 += 1
        else:
            n0_ += 1
            if eve in i["events"]:
                n01 += 1
                n_1 += 1
            else:
                n00 += 1
                n_0 += 1
    phi = (n11*n00-n10*n01)/math.sqrt(n1_*n0_*n_1*n_0)
    return phi


def compute_correlations(journal):
    data = load_journal(journal)
    corr = {}
    for i in data:
        for j in i["events"]:
            if j not in corr.keys():
                corr[j] = compute_phi(journal, j)
    return corr


def diagnose(journal):
    corr = compute_correlations(journal)
    max_eve = max(corr, key=corr.get)
    min_eve = min(corr, key=corr.get)
    return max_eve, min_eve
