import csv


with open('file1.csv', mode='r') as f1:
    with open('file2.csv', mode='r') as f2:
        #f = open('output.csv', 'w')
        reader1 = list(csv.reader(f1))
        reader2 = list(csv.reader(f2))
        print(len(reader1))
        print(len(reader2))
        count = 0

        for i in reader2:
            if (i[5] != ''):
                for j in reader1:
                    if(i[5] == j[0]):
                        count +=1
                        #data=j[1]+":"+i[1]+":"+i[2]+":"+i[3]+":"+i[4]+":"+i[5]+":"+i[6]+":"+\
                        #    j[7]+","+j[8] + ":" +j[2]+":"+i[9]+":"+i[10]+":"+i[11]+":"+i[12]+"\n"
                        #print(data)
                        #f.write(data)

                    else:
                        pass


            else:
                count += 1
                #data = i[0] + ":" + i[1] + ":" + i[2] + ":" + i[3] + ":" + i[4] + ":" + i[5] + ":" + i[6] + ":" + \
                #       i[7] + ":" + i[8] + ":" + i[9] + ":" + i[10] + ":" + i[11] + ":" + i[12]+"\n"
                #print(data)
                #f.write(data)

        #f.close()
        print(count)
