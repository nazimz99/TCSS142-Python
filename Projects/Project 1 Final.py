#Nazim Zerrouki
#TCSS 142 Progamming Assignment 1 David Schuessler 
#11/20/17

#This line of code is used to open a file to read and to open a file for writing.
infile = open("train.csv", 'r')
outfile = open("clevelanddiag.csv", 'w')

#These are used to create lists for each specific column.
#The patients list is used to test each patient for coronary heart disease.
#The variables are incremented to help record the lines processed and the number of healthy and ill patients.
patients = [ ]
list0 = [ ]
list1 = [ ]
list2 = [ ]
list3 = [ ]
list4 = [ ]
list5 = [ ]
list6 = [ ]
list7 = [ ]
list8 = [ ]
list9 = [ ]
list10 = [ ]
list11 = [ ]
list12 = [ ]
average_ill = [0] * 13 #counter list for ill averages where each index represents the averages of a column.
average_healthy = [0] * 13 #counter list for healthy averages where each index represents the averages of a column.
separation = [0] * 13 #counter list for separation values where each index represents each column of both the ill and healthy averages.
index = 0
ill_count = 0
healthy_count = 0
ill_train = 0 #Uses new classifier to count the number of ill patients.
healthy_train = 0 #Uses new classifier to count the number of healthy patients.

#Counter lists used to calculate the sum of each column for ill and healthy patients respectively.
sum_ill = [0] * 13
sum_healthy = [0] * 13

#Counter list to calculate the attributes that are at risk by using the cleveland classifier.
risk = [0] * 13 

for lines in infile:
#index is incremented for each line processed to calculate the number of lines within the file. 
    index += 1
    
#In order to create a list for each column of attributes, I had to create an array by using the split function. data[0] represents the 1st column whereas data[len(data) - 1) represents every value in the last column.
    data = lines.split(',')
    data[len(data) - 1] = data[len(data) - 1].rstrip('\n')
    
#Once I split the file into an array that represents each line, I created a list called patients with every value in the last column to test whether the patient was ill or healthy.
    num = float(data[len(data) - 1]) 
    patients.append(num)
    
#Since '?' can't be incremented, I test each value in each column and if that value is equal to '?', then we assign zero to that value.
    if data[0] == '?':
        data[0] = '0'
    if data[1] == '?':
        data[1] = '0'
    if data[2] == '?':
        data[2] = '0'
    if data[3] == '?':
        data[3] = '0'
    if data[4] == '?':
        data[4] = '0'
    if data[5] == '?':
        data[5] = '0'
    if data[6] == '?':
        data[6] = '0'
    if data[7] == '?':
        data[7] = '0'
    if data[8] == '?':
        data[8] = '0'
    if data[9] == '?':
        data[9] = '0'
    if data[10] == '?':
        data[10] = '0'
    if data[11] == '?':
        data[11] = '0'
    if data[12] == '?':
        data[12] = '0'
        
#Afterwards, I created a list where it adds each line of code for its respective column. 
    list0.append(data[0])
    list1.append(data[1])
    list2.append(data[2])
    list3.append(data[3])
    list4.append(data[4])
    list5.append(data[5])
    list6.append(data[6])
    list7.append(data[7])
    list8.append(data[8])
    list9.append(data[9])
    list10.append(data[10])
    list11.append(data[11])
    list12.append(data[12])

#i represents the row number or index for each list where i is incremented by 1.
#To check the condition, we have to go through each value in the patients list with a for loop.
#If statement is used to check the num value, so then we can increment the number of ill and healthy patients by 1 depending on its value.
i = 0
for num in patients:

#By checking the value, if the patient is ill, then we increment the column of values to its respective list.
#Each index of the sum counter listbelongs to a column and we increment the sum of each index to the values found in its column, so then we can calculate the average.
#i is used to locate the specific attributes in each column or list where the patient is ill.

    if num != 0:
        ill_count += 1
        sum_ill[0] += float(list0[i])
        sum_ill[1] += float(list1[i])
        sum_ill[2] += float(list2[i])
        sum_ill[3] += float(list3[i])
        sum_ill[4] += float(list4[i])
        sum_ill[5] += float(list5[i])
        sum_ill[6] += float(list6[i])
        sum_ill[7] += float(list7[i])
        sum_ill[8] += float(list8[i])
        sum_ill[9] += float(list9[i])
        sum_ill[10] += float(list10[i])
        sum_ill[11] += float(list11[i])
        sum_ill[12] += float(list12[i])

    else:

#If the patient is healthy, then the same is done except a separate counter list is used to calculate the sums for healthy patients.
        healthy_count += 1
        sum_healthy[0] += float(list0[i])
        sum_healthy[1] += float(list1[i])
        sum_healthy[2] += float(list2[i])
        sum_healthy[3] += float(list3[i])
        sum_healthy[4] += float(list4[i])
        sum_healthy[5] += float(list5[i])
        sum_healthy[6] += float(list6[i])
        sum_healthy[7] += float(list7[i])
        sum_healthy[8] += float(list8[i])
        sum_healthy[9] += float(list9[i])
        sum_healthy[10] += float(list10[i])
        sum_healthy[11] += float(list11[i])
        sum_healthy[12] += float(list12[i])
    i += 1

#This counter list is used to calculate the average ill attributes in each column separately by referring to the index value of the counter list.
average_ill[0] = round(sum_ill[0] / ill_count, 2)
average_ill[1] = round(sum_ill[1] / ill_count, 2)
average_ill[2] = round(sum_ill[2] / ill_count, 2)
average_ill[3] = round(sum_ill[3] / ill_count, 2)
average_ill[4] = round(sum_ill[4] / ill_count, 2)
average_ill[5] = round(sum_ill[5] / ill_count, 2)
average_ill[6] = round(sum_ill[6] / ill_count, 2)
average_ill[7] = round(sum_ill[7] / ill_count, 2)
average_ill[8] = round(sum_ill[8] / ill_count, 2)
average_ill[9] = round(sum_ill[9] / ill_count, 2)
average_ill[10] = round(sum_ill[10] / ill_count, 2)
average_ill[11] = round(sum_ill[11] / ill_count, 2)
average_ill[12] = round(sum_ill[12] / ill_count, 2)

#This counter list is used to calculate the average healthy attributes in each column separately by referring to the index value of the counter list.
average_healthy[0] = round(sum_healthy[0] / healthy_count, 2)
average_healthy[1] = round(sum_healthy[1] / healthy_count, 2)
average_healthy[2] = round(sum_healthy[2] / healthy_count, 2)
average_healthy[3] = round(sum_healthy[3] / healthy_count, 2)
average_healthy[4] = round(sum_healthy[4] / healthy_count, 2)
average_healthy[5] = round(sum_healthy[5] / healthy_count, 2)
average_healthy[6] = round(sum_healthy[6] / healthy_count, 2)
average_healthy[7] = round(sum_healthy[7] / healthy_count, 2)
average_healthy[8] = round(sum_healthy[8] / healthy_count, 2)
average_healthy[9] = round(sum_healthy[9] / healthy_count, 2)
average_healthy[10] = round(sum_healthy[10] / healthy_count, 2)
average_healthy[11] = round(sum_healthy[11] / healthy_count, 2)
average_healthy[12] = round(sum_healthy[12] / healthy_count, 2)

#This counter list is used to find the averages for both healthy and ill attributes in their respective columns by referring to their indexes..
#Then the midpoint is calculated by finding the mean of those averages at each index.
#Index of both separation and the averages counter lists must remain the same.
separation[0] = round((average_ill[0] + average_healthy[0]) / 2, 2)
separation[1] = round((average_ill[1] + average_healthy[1]) / 2, 2)
separation[2] = round((average_ill[2] + average_healthy[2]) / 2, 2)
separation[3] = round((average_ill[3] + average_healthy[3]) / 2, 2)
separation[4] = round((average_ill[4] + average_healthy[4]) / 2, 2)
separation[5] = round((average_ill[5] + average_healthy[5]) / 2, 2)
separation[6] = round((average_ill[6] + average_healthy[6]) / 2, 2)
separation[7] = round((average_ill[7] + average_healthy[7]) / 2, 2)
separation[8] = round((average_ill[8] + average_healthy[8]) / 2, 2)
separation[9] = round((average_ill[9] + average_healthy[9]) / 2, 2)
separation[10] = round((average_ill[10] + average_healthy[10]) / 2, 2)
separation[11] = round((average_ill[11] + average_healthy[11]) / 2, 2)
separation[12] = round((average_ill[12] + average_healthy[12]) / 2, 2)

#This entire line of code is used to iterate and test the classifier that was used for the cleveland study in the training study and is explained later in the code.

i = 0
#pos = 0
#risk_total = 0
for  num in patients:
    risk = [0] * 13 #This risk counter is a list that only processes one line at a time. It is incremented by 1 at each index depending on how it compares to the separation value in its respective column.
    risk_total = 0
   
    if float(list0[i]) > separation[0]:
        risk[0] += 1
    if float(list1[i]) > separation[1]:
        risk[1] += 1
    if float(list2[i]) > separation[2]:
        risk[2] += 1
    if float(list3[i]) > separation[3]:
        risk[3] += 1
    if float(list4[i]) > separation[4]:
        risk[4] += 1
    if float(list5[i]) > separation[5]:
        risk[5] += 1
    if float(list6[i]) > separation[6]:
        risk[6] += 1
    if float(list7[i]) > separation[7]:
        risk[7] += 1
    if float(list8[i]) > separation[8]:
        risk[8] += 1
    if float(list9[i]) > separation[9]:
        risk[9] += 1
    if float(list10[i]) > separation[10]:
        risk[10] += 1
    if float(list11[i]) > separation[11]:
        risk[11] += 1
    if float(list12[i]) > separation[12]:
        risk[12] += 1
    i += 1
    #risk_total = risk[0] + risk[1] + risk[2] + risk[3] + risk[4] + risk[5] + risk[6] + risk[7] + risk[8] + risk[9] + risk[10] + risk[11] + risk[12]
    
    #Increments by the values "r" in the counter list to calculate the amount of attributes that are at risk.
    
    for r in risk:
       risk_total += r
    
    #Increments by 1 to find the number of ill and healthy patients based on the conditions presented in Part 2 of the project.
    
    if risk_total > (len(data) - 2) / 2:
        ill_train += 1
    else:
        healthy_train += 1
    #print(risk)
    #print(risk_total)
    
infile.close()

#Outputs total lines, number of ill patients, and number of healthy patients using calculations made previously.

outfile.write("Total Lines Processed:")
outfile.write(str(index))
outfile.write("\nTotal Healthy Count:")
outfile.write(str(ill_count))
outfile.write("\nThe number of healthy patients is:")
outfile.write(str(healthy_count))

#While loop ensures that the values in each counter_list at their respective index will be referred to without incrementing beyond the length of the list.

value = 0
outfile.write("\nThe average attributes for ill patients are:\n")
while value < len(data) - 1:
    outfile.write(str(average_ill[value]))
    value += 1
    outfile.write(',')
outfile.write("\n")

value = 0
outfile.write("\nThe average attributes for healthy patients are:\n")
while value < len(data) - 1:
    outfile.write(str(average_healthy[value]))
    value += 1
    outfile.write(',')
outfile.write("\n")

value = 0
outfile.write("\nThe separation values are:\n")
while value < len(data) - 1:
    outfile.write(str(separation[value]))
    value += 1
    outfile.write(',')
outfile.write("\n")

#print(ill_train)
#print(healthy_train)

#Opens the next file in the project to be read.
infile2 = open("cleveland.csv", 'r')
#outfile2 = open("cleveland.csv", 'w')
idx = 0
ill_count2 = 0
healthy_count2 = 0

#These lists are used to refer to each value in a specific column for every column.
#These lists are used to create a "risk counter" to help predict whether a patient is ill or not.
list0_2 = [ ]
list1_2 = [ ]
list2_2 = [ ]
list3_2 = [ ]
list4_2 = [ ]
list5_2 = [ ]
list6_2 = [ ]
list7_2 = [ ]
list8_2 = [ ]
list9_2 = [ ]
list10_2 = [ ]
list11_2 = [ ]
list12_2 = [ ]
list13_2 = [ ]
#risk = [0] * 13 #Another risk counter list for the cleveland study.

#Processes each line in "cleveland" study.
for lines2 in infile2:
    
#Splits each line into a list or an array for each row for the 2nd file.
    data2 = lines2.split(',')
    data2[len(data2) - 1] = data2[len(data2) - 1].rstrip('\n')
    elem = data2[0]
    list0_2.append(elem)
    idx = 0
    
#This looks through each value in the list for every line.
#The idx variable is incremented and refers to the index of every value of the list.
#A for loop is used to check ever value in the file and if said value is equal to a string, then it is assigned a new value 'zero'.    
    while idx < len(data2) - 1 :
        idx += 1
    for val in data2:
        if val == '?':
            data2[idx] = '0'
        if data2[12] == '?':
            data2[12] = '0'
        if data2[13] == '?':
            data2[13] = '0'
                
#Each value within a specific column is appended to a list similar to what was done for the training set.    
    list1_2.append(data2[1])
    list2_2.append(data2[2])
    list3_2.append(data2[3])
    list4_2.append(data2[4])
    list5_2.append(data2[5])
    list6_2.append(data2[6])
    list7_2.append(data2[7])
    list8_2.append(data2[8])
    list9_2.append(data2[9])
    list10_2.append(data2[10])
    list11_2.append(data2[11])
    list12_2.append(data2[12])
    list13_2.append(data2[13])

i = 0
#This goes through each row 'i' and looks through each column or identity of each patient which contains values in the first column.
for elem in list0_2:
    risk = [0] * 13
    risk_total = 0
    
#Risk counters are made to detect if a patient is at risk for a specific attribute.
#Each value within the risk counter list will increment by 1 if the person is at risk and this is done for every attribute.
#Each value in the risk belongs to a specific column and is designed to return to 0 when looking through each row or value in each list.
#Each line can be thought of as an array of binary code to calculate the risk.
    
    if float(list1_2[i]) > separation[0]:
        risk[0] += 1
    if float(list2_2[i]) > separation[1]:
        risk[1] += 1
    if float(list3_2[i]) > separation[2]:
        risk[2] += 1
    if float(list4_2[i]) > separation[3]:
        risk[3] += 1
    if float(list5_2[i]) > separation[4]:
        risk[4] += 1
    if float(list6_2[i]) > separation[5]:
        risk[5] += 1
    if float(list7_2[i]) > separation[6]:
        risk[6] += 1
    if float(list8_2[i]) > separation[7]:
        risk[7] += 1
    if float(list9_2[i]) > separation[8]:
        risk[8] += 1
    if float(list10_2[i]) > separation[9]:
        risk[9] += 1
    if float(list11_2[i]) > separation[10]:
        risk[10] += 1
    if float(list12_2[i]) > separation[11]:
        risk[11] += 1
    if float(list13_2[i]) > separation[12]:
        risk[12] += 1
    i += 1

    for r in risk:
        risk_total += r

    if risk_total > (len(data) - 2) / 2:
        ill_count2 += 1
    else:
        healthy_count2 += 1

#print(ill_count2)
#print(healthy_count2)

infile2.close()

diff_1 = abs(ill_count2 - ill_train)
diff_2 = abs(healthy_count2 - healthy_train)
diag1 = ill_count2 - diff_1
diag2 = healthy_count2 - diff_2
diagnosis = diag1 + diag2
accuracy = round((diagnosis) / index, 2)

outfile.write("\nAccuracy:")
outfile.write(str(accuracy))
#print(accuracy)

outfile.close()
