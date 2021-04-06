import csv 
import pandas as pd
from collections import Counter
with open('height.csv') as f:
    data = csv.reader(f)
    data1 = list(data)
data1.pop(0)
newData=[]
for i in range(len(data1)):
    weight1=data1[i][0]
    newData.append(float(weight1))
n = len(data1)

finalData = Counter(newData)
modeDataForRange = {
    '70-100':0,
    '100-130':0,
    '130-160':0
}
for weight,occurence in finalData.items():
    print(weight)
    print(occurence)
    if 70<float(weight)<100:
        modeDataForRange['70-100']+=occurence
    elif 100<float(weight)<130:
        modeDataForRange['100-130']+=occurence
    elif 130<float(weight)<160:
        modeDataForRange['130-160']+=occurence
modeRange,modeOccurence=0,0
for range,occurence in modeDataForRange.items():
    print(occurence)
    if occurence>modeOccurence:
        modeRange,modeOccurence=[int(range.split('-')[0]),int(range.split('-')[1])],occurence
print(modeRange)

mode = float((modeRange[0]+modeRange[1])//2)

print(f'Mode is: {mode:2f}')   