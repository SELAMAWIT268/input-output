name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is:", num1 + num2)

filename = "sample.txt"
with open(filename, "r") as file:
    words = file.read().split()
print("Number of words in file:", len(words))

sentence = input("Enter a sentence: ")
reversed_sentence = sentence[::-1]

with open("reversed.txt", "w") as f:
    f.write(reversed_sentence)

print("Reversed sentence saved in reversed.txt")


import csv

filename = "data.csv"
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

print(data)


import time

log_file = "log.txt"
keyword = "ERROR"

print(f"Monitoring {log_file} for '{keyword}'...")

with open(log_file, "r") as file:
    file.seek(0, 2)
    while True:
        line = file.readline()
        if line and keyword in line:
            print("ALERT! Keyword found:", line.strip())
        time.sleep(1)
