import csv


with open('file.csv', mode='r') as f1:


        reader1 = list(csv.reader(f1))

        print("Number of lines : ",len(reader1))
        print("Number of Columns: ",len(reader1[0]))
