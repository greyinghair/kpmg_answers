# Rewrite question B8 from session 3 using a while loop ........
# A school has following rules for their grading system:
# a. Above 80 – A
# b. 60 to 80 – B
# c. 50 to 60 – C
# d. 45 to 50 – D
# e. 25 to 45 – E
# f. Below 25 - F
# Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lessonname = []
lessonmark = []
lessongrade = []
loopcount = 0 # for 1st loop
loopcount2 = 0 # new count used for 2nd loop to pull out the info from lists to display

while loopcount != 3: # stop looping after loopcount =3
    loopcount += 1 # increment loopcount var by +1 in each run
    lessonname.append(input("What is lesson name #" + (str(loopcount)) + " ?: "))
    lessonmark.append(input("What mark did you get for lesson #" + (str(loopcount)) + " ?: "))
    if int(lessonmark[loopcount - 1]) < 25: #Index position will be previous loopcount -1 as index start at 0
        lessongrade.append("F")
    elif int(lessonmark[loopcount - 1]) < 46:
        lessongrade.append("E")
    elif int(lessonmark[loopcount - 1]) < 51:
        lessongrade.append("D")
    elif int(lessonmark[loopcount - 1]) < 61:
        lessongrade.append("C")
    elif int(lessonmark[loopcount - 1]) < 81:
        lessongrade.append("B")
    elif int(lessonmark[loopcount - 1]) >= 81:
        lessongrade.append("A")

while loopcount2 != loopcount: # run loop until loopcount2 is equal to value of loopcount, (which should be 3)
    loopcount2 += 1 # increment loopcount2 by 1
    print("For " + lessonname[loopcount2-1] + " your grade = " + lessongrade[loopcount2-1]) # Count -1 for index pos