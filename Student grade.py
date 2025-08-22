names =["Radha ","Siddhi", "Sita"]
grades=[85,90,78]
#add name&grade
names.append("Khushi")
grades.append(88)
print(names)
print(grades)

#update grade 
if"Radha" in names :
     index =names.index("Radha")
     grades[index]=95
     print(grades)
#remove sita name
if"Sita" in names:
     index=names.index("Sita")
     names.pop(index)
     grades.pop(index)
     print (names)

#calculate average grade
total=0
for g in grades:
     total=+g
     average=total/len(grades)
print(f"Average grade: {average:.2f}")


#find highest & lowet marks
highest=grades[0]
lowest=grades[0]
for g in grades:
    if g>highest:
         highest =g
    if g<lowest:
          lowest=g
print(f"Highest grade:{highest}") 
print(f"Lowest grade:{lowest}")    