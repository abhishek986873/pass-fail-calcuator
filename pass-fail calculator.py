print("* EACH SUBJECT OF 100 MARKS")
print('---------------------------------------------------------------')
print("* CRITERIA FOR PASSING:-\n* TOTAL 40% REQUIRED\n* EACH SUBJECT MARKS MUST GREATER THAN 33")
print('---------------------------------------------------------------')
# taking subject mark input 
stud1=int(input('• Enter maths mark: '))
stud2=int(input('• Enter physics marks: '))
stud3=int(input('• Enter chemistry marks: '))
print('---------------------------------------------------------------')
# calculating percentage
add=stud1+stud2+stud3
div=(add/300)
per_nt=int((div*100))
# finding total mark percentage
total_marks=stud1+stud2+stud3 #must be equal or greater than 120
#each subject percent
if (total_marks>=120 and stud1>33 and stud2>33 and stud3>33):
    print("\n* you have passed the exam")
    print("• PERCENTAGE = ",per_nt,'%')
elif (total_marks<120 and stud1<33 and stud2<33 and stud3<33):
    print('\n* sorry you have failed the exam')
    print("• PERCENTAGE = ",per_nt,'%')
elif (total_marks<120 and stud1<33 or stud2<33 or stud3<33):
    print("\n* 'you have faild the exam'")
    print("• PERCENTAGE = ",per_nt,"%")
elif (total_marks>=120 and stud1<33 or stud2<33 or stud3<33):
    print("\n* 'sorry you have failed'")
    print("• PERCENTAGE = ",per_nt,'%')
