#question 1
try:
    with open("diray.txt","w") as f: #create file
     f.write("\n2024-06-01: Had a great day at the park.")
     f.write("\n2024-06-02: Finished reading a good book.")
     f.write("\n2024-06-03: Cooked dinner for the family.")
     f.write("\n2024-06-04: Went for a long morning walk.")
     f.write("\n2024-06-05: Started learning about Python files.")
     f.close()
    print("Diray entires saved sucessfuly") #if diray is success
except Exception as e:
     print("Error While using file") #Not sucessful
#2.Add more entries to the same file and then display all stored content.
try:
    with open("add_entries.txt","w") as f:
     f.write(""" 2020-05-01:I read in class 8.
2021-01-02:I am playing cricket.
2022-01-22: I got gpa 5
2024-020-02: I took my HSC exam """)
    print("Add entriers sucessfuly")
except Exception as e:
  print("Error While using file") #Not sucessful
with open("diray.txt","r") as f : #read mathod
  print(f.read()) #for show the data
  f.close()
#3.Extract all dates from the entries that match the format YYYY-MM-DD.
import re
with open("diray.txt","r") as f : #read mathod
  date=f.read()
diray=re.findall(r"\d{4}-\d{2}-\d{2}",date)
print("\nDates found:",diray)
# 4.Check whether specific words exist in an entry and report whether each word is found or not.
with open("diray.txt", "r") as f:
    data = f.read().lower()

with open("spec_word.txt", "w") as f:
    words = ["park", "play", "cricket", "book", "family", "python"]

    for word in words:
        if word.lower() in data:
            f.write(f"{word} found\n")
        else:
            f.write(f"{word} not found\n")
# From all entries, collect every unique word longer than 4 characters

with open("diray.txt", "r") as f:
    entries = f.readlines()

unique_words = set()

for entry in entries:
    words = entry.split()

    for word in words:
        clean_word = word.strip(".,:")

        if len(clean_word) > 4:
            unique_words.add(clean_word)

print("Unique words longer than 4 characters:")
print(unique_words)
# 6.From all entries, collect every unique word longer than 4 characters

with open("diray.txt", "w") as f:
    f.write("\n2024-06-01: Had a great day at the park.")
    f.write("\n2024-06-02: Finished reading a good book.")
    f.write("\n2024-06-03: Cooked dinner for the family.")
    f.write("\n2024-06-04: Went for a long morning walk.")
    f.write("\n2024-06-05: Started learning about Python files.")

# Read file
with open("diray.txt", "r") as f:
    diray = f.readlines()

threshold = 40

for entry in diray:
    length = len(entry)

    if length > threshold:
        label = "Long"
    else:
        label = "Short"

    print(f"Entry: {entry.strip()}")
    print(f"Length: {length} characters")
    print(f"Label: {label}")
    print("-" * 40)
#8.
try:
    # Attempt to open a non-existing file
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Program finished cleanly.")

    # Extract dates
with open("diray.txt", "w") as f:
    f.write("\n2024-06-01: Had a great day at the park.")
    f.write("\n2024-06-02: Finished reading a good book.")
    f.write("\n2024-06-03: Cooked dinner for the family.")
    f.write("\n2024-06-04: Went for a long morning walk.")
    f.write("\n2024-06-05: Started learning about Python files.")

dates = []
for entry in diray:
    date = entry.split(":")[0]
    dates.append(date)

# Find the longest entry
longest_entry = max(entries, key=len)

# Build summary
summary = {
    "Total number of entries": len(entries),
    "All extracted dates": dates,
    "Longest entry": longest_entry
}

# Display summary
for key, value in summary.items():
    print(f"{key}: {value}")