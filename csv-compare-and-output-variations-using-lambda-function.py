import csv


with open('file1.csv', mode='r') as csvFile1:
    with open('file2.csv', mode='r') as csvFile2:
        
        '''
        Read all items in csv file and convert into list format. 
        List will be a nested list -> [[Item1,Value1],[Item2,Value2]...]
        '''
        csvFile1_data = list(csv.reader(csvFile1)) 
        csvFile2_data = list(csv.reader(csvFile2))
        
        '''
        If you want to take a column and compare values in it to the values in the other list use the method below.
        If you JUST want to compare both lists as is then ignore line 18-26 and change list2 and list 1 in non_match to non_match(csvFile1,csvFile2)
        '''
        list1 =[]
        list2 =[]

        for i in reader1:
            if i[5] != '':
                list1.append(i[5])
        for i in reader2:
            if i[5] != '':
                list2.append(i[5])

        l_func = lambda x,y: list((set(x)-set(y))) + list((set(y)-set(x)))
        non_match = l_func(list2,list1)
        
        
        '''
        Output is list of all differences
        '''
        print(non_match)
        
        
        '''
        Clean the output a bit by printing line by line.
        '''
        for i in non_match:
            print(i)
            
            
