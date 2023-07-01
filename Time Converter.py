import pandas as pd
import numpy as np
x=pd.read_excel("original - Kopya.xlsx",6)

pv_uretimi=x[["A1_PV","A2_PV","A3_PV","A4_PV","A5_PV"]]

pv_uretimi2=pd.DataFrame(columns=["A1_PV","A2_PV","A3_PV","A4_PV","A5_PV"])
m=pv_uretimi[["A1_PV"]].values.tolist()
n=np.ones(8760*60).tolist()
"""
for y in (8760*2):
    for x in range(8760):
        m[x]=n[(60*y):(60*(y+1))]
"""

par2=pd.read_excel("original - Kopya.xlsx",6)
# y = yuk talebi
load=np.array(par2[["A1","A2","A3","A4","A5"]])

y=-1
while y <8759 :
    y += 1
    for x in range((60*y),(60*(y+1))):
        n[x] = m[y][0]
df=pd.DataFrame(n)
df.to_excel("a.xlsx")