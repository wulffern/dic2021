#!/usr/bin/env python3

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("microprocessor_tech.csv")

print(df["Max clock"])

def engConv(ss):
    if(type(ss) is str):

        if(ss == "-"):
            return np.nan
        if("–" in ss):
            ss = re.sub("^.*–","",ss)
        if("-" in ss):
            ss = re.sub("^.*-","",ss)

        ss = re.sub("\xa0","",ss)
        if("GHz" in ss):
            ss = ss.replace("GHz","")
            ss = float(ss)*1e9
        elif("MHz" in ss):
            ss = ss.replace("MHz","")
            ss = float(ss)*1e6
        elif("kHz" in ss):
            ss = ss.replace("kHz","")
            ss = float(ss)*1e3

    else:
        print(ss)
    return ss

df = df.set_index("Date")
speed = df["Max clock"].apply(engConv).dropna()/1e9

speed.plot()
plt.xlabel("Date")
plt.ylabel("CPU Max clock [GHz]")
plt.grid()
plt.title("https://en.wikipedia.org/wiki/Microprocessor_chronology")

ax = plt.gca()
ax.set_yscale("log")

plt.savefig("cpumax.pdf")
#plt.show()
print(speed)
