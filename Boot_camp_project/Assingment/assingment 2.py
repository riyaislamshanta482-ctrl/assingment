#Sort the score list from highest to lowest using a compact inline function approach.
# make a list by using list
Scores=[72, 45, 88, 60, 91, 33, 78, 55]
Scores.sort(reverse=True)
print("Sorted (high --> low):",Scores)
# 2.From the same list, keep only values that are 60 or above and display them.
print("Passing scores (≥60):")
for i in Scores:
  if i>= 60:

     print(i)

#3.Add 5 bonus points to every score and show the updated list
Scores=[72, 45, 88, 60, 91, 33, 78, 55]
#range(len(Scores)) becuase it will run all the number in the list
for i in range(len(Scores)):
   Scores[i]+=5 # for increment value
print(" Scores after +5 bonus:",Scores)
#4 Compute the total sum of all original scores.
Scores=[72, 45, 88, 60, 91, 33, 78, 55]
total=sum(Scores)
print( "Total of all scores:",total)
#5.Extract all unique grade letters from the given list.
Grade_Letters= ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C']
unique_grades = set(Grade_Letters)
print(" Unique grades:",unique_grades)

#6.Save student records into a structured file with two fields: name and score. Then read it back and display each record. Handle any file-related issues safely.
# Student Record
student_records =[
 {"name":"Alice" ,"score": 88},
 {"name":"Bob" ,"score": 72 },# Bob – 72
 {"name":" Charlie" ,"score": 45},
 {"name":" David " ,"score": 91},
{"name":"  Eve" ,"score": 78}

]
# save into file
try:
    file = open("students.txt", "w")

    for student in student_records :
        file.write(f"{student['name']},{student['score']}\n")

    file.close()

    print("Data saved successfully!")

except Exception as e:
    print("Error while writing file:", e)


# read from file
try:
    file = open("students.txt", "r")

    print("\nStudent Records:")

    for line in file:
        name, score = line.strip().split(",")
        print(f"Name: {name}, Score: {score}")

    file.close()

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("Error while reading file:", e)
#7.Create a summary containing:
# make list again
Scores=[72, 45, 88, 60, 91, 33, 78, 55]
print("Total Student:",len(Scores))
print( " Highest Score:",max(Scores))
print( " Lowest Score:",min(Scores))
#for i in range(len(Scores)):
total=sum(Scores)
avarage=total/len(Scores)
print("Avarage:",avarage)
x=round(avarage, 2)
print("Round 2 decimal:",x)