print("* each subject of 100 marks")
print('---------------------------------------------------------------')
# taking subject mark input 
stud1=int(input('Enter maths mark: '))
stud2=int(input('Entre physics marks: '))
stud3=int(input('Entre chemistry marks: '))
# finding total mark percentage
total_marks=stud1+stud2+stud3 #must be equal or greater than 120
#each subject percent
if (total_marks>=120 and stud1>33 and stud2>33 and stud3>33):
    print("\n*you have passed the exam")
elif (total_marks<120 and stud1<33 and stud2<33 and stud3<33):
    print('\n*sorry you have failed the exam')
elif (total_marks<120 and stud1<33 or stud2<33 or stud3<33):
        print("\n*'you have faild the exam'")
elif (total_marks>=120 and stud1<33 or stud2<33 or stud3<33):
    print("\n*'sorry you have failed'")




