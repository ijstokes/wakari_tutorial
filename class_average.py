#!/usr/bin/env python
""" Example of some basic data processing in Python """

grades    = [] # initialize empty list
altgrades = []

data_fh   = open("classrecord.dat","r")

for student_record in data_fh:
    columns     = student_record.split()
    person      = columns[0]
    grade       = float(columns[3])
    if   grade >= 90.0:
        textgrade = "A+"
    elif grade >= 80.0:
        textgrade = "A"
    elif grade >= 70.0:
        textgrade = "B"
    elif grade >= 60.0:
        textgrade = "C"
    elif grade >= 50.0:
        textgrade = "D"
    else:
        textgrade = "F"
    print "%s\treceived %s [%3.1f]" % (person, textgrade, grade)

    grades.append(grade)
    altgrades.append(textgrade)

data_fh.close()

print grades
print altgrades

average = sum(grades)/len(grades)
print "Overall average is %5.3f" % average
