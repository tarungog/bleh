import os
import time

flags = []
with open('flags.txt', 'r') as flagsFile:
    for line in flagsFile:
        flags.append(line)

gccCommand = "time gcc "
inputFilename = "toy.c"
outputFilename = "output"


gccCommand += inputFilename + " "
flagSwitches = [1,0,0,1,0]s
for flagSwitchesIndex in range(len(flagSwitches)):
    if flagSwitches[flagSwitchesIndex]:
         gccCommand += flags[flagSwitchesIndex][:-1] + " "


gccCommand += "-o " + outputFilename

start_time = time.time()
os.system(gccCommand)
end_time = time.time()
total_time = end_time - start_time
print(total_time)


start_time = time.time()
os.system("./" + outputFilename)
end_time = time.time()
total_time = end_time - start_time
print(total_time)

print(gccCommand)
