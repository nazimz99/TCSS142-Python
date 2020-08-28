#Nazim Zerrouki
import math
infile = open("grades.csv", 'r')
outfile = open("examScores.csv", 'w')
first_names = [ ]
last_names = [ ]
midterms = [ ]
finals = [ ]
averages = [ ]
lineCount = 0
maxAverage = 0
count = 0
index = 0
for lines in infile:
    lineCount += 1
    if lineCount > 1:
        data = lines.split(',')
        last_names.append(data[0])
        first_names.append(data[1])
        midterms.append(data[2])
        data[3] = data[3].rstrip('\n')
        finals.append(data[3])
        total = 0
        idx = 2
        while idx < len(data):
            total += float(data[idx])
            idx += 1
            average = math.ceil(total / (idx - 2))
        averages.append(average)
        index = averages.index(average)
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
        if average > maxAverage:
            maxAverage = average             
infile.close()
outfile.write('\n')
outfile.write('\n')
for average in averages:
    if average >= maxAverage - 5 and average <= maxAverage:
        index = averages.index(average)
        count += 1
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
        
outfile.write('\n{:>2}'.format(count))
outfile.write(" students have scored 5 points within the maximum average.\n")
outfile.write('\n')

count = 0
for average in averages:
    if average in range(90, maxAverage + 1):
        index = averages.index(average)
        count += 1
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
outfile.write('\n{:>2}'.format(count))
outfile.write(" students have an average score above 90 points.\n")
outfile.write('\n')
count = 0
for average in averages:
    if average in range(70, 80):
        index = averages.index(average)
        count += 1
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
outfile.write('\n{:>2}'.format(count))
outfile.write(" students have an average score between 70 and 79 points.\n")
outfile.write('\n')
count = 0
for average in averages:
    if average in range(60, 70):
        index = averages.index(average)
        count += 1
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
outfile.write('\n{:>2}'.format(count))
outfile.write(" students have an average score between 60 and 69 points.\n")
outfile.write('\n')
count = 0
for average in averages:
    if average < 60:
        index = averages.index(average)
        count += 1
        student_list = str(first_names[index]) + ' ' + str(last_names[index]) + ' ' + str(averages[index])
        outfile.write(student_list)
        outfile.write('\n')
outfile.write('\n{:>2}'.format(count))
outfile.write(" students have an average score below 60 points.")




outfile.close()
