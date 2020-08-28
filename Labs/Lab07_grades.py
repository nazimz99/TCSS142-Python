#Nazim Zerrouki
#11/20/17

import math

def main():
    ifilevar = open('grades.csv', 'r')
    ofilevar = open('examScores.csv', 'w')
    lnameList = []
    fnameList = []
    gradeAve = []
    gradeRanges = [0] * 5
    readFile(ifilevar,fnameList,lnameList,gradeAve,gradeRanges)
    topScorers(lnameList,fnameList,gradeAve)
    print()
    ranges(gradeRanges)
    writeFile(ofilevar,lnameList,fnameList,gradeAve)
    ifilevar.close()
    ofilevar.close()
    
    
def readFile(ifilevar,lnameList,fnameList,gradeAve,gradeRanges):
    ifilevar.readline()
    for line in ifilevar:
        lineList = line.split(',')
        lnameList.append(lineList[0])
        fnameList.append(lineList[1])
        tot = 0
        idx = 2
        while idx < len(lineList):
            tot += int(lineList[idx])
            idx += 1
        average = (math.ceil(tot / (idx-2)))
        gradeAve.append(average)
        if average >= 90:
            gradeRanges[4] += 1
        elif average >= 80:
            gradeRanges[3] += 1
        elif average >= 70:
            gradeRanges[2] += 1
        elif average >= 60:
            gradeRanges[1] += 1
        elif average >= 0:
            gradeRanges[0] += 1
    return lnameList, fnameList, gradeAve, gradeRanges

def writeFile(ofilevar,fnameList,lnameList,gradeAve):
    pos = 0
    for el in lnameList:
        ofilevar.write(el + ',')
        ofilevar.write(fnameList[pos] + ',') 
        ofilevar.write(str(gradeAve[pos]) + '\n')
        pos += 1
    return ofilevar
    

def topScorers(lnameList,fnameList,gradeAve):
    print("Top scorers:")
    hi = max(gradeAve) - 5
    c = 0
    for el in gradeAve:
        if el >= hi:
            print(lnameList[c], fnameList[c], el, sep = ', ')
        c += 1

def ranges(gradeRanges):
    print("Grade ranges: ")
    lowBound = 0
    for el in gradeRanges:   
        print(el, "students with grades >= ", lowBound)
        if lowBound == 0:
            lowBound += 60
        else:
            lowBound += 10


 

main()
