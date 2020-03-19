# Tutorial 223 - Work with CSV files using python
from csv import reader
with open('file.csv', 'r') as f:
    csv_reader = reader(f)
    # print(csv_reader)   # iterator
    next(csv_reader)
    for row in csv_reader:
        print(row)


# *****************************************************************************************
# Tutorial 224 - Read CSV files with DictReader
from csv import DictReader
with open('file.csv', 'r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['name'])


# *****************************************************************************************
# Tutorial 225 - Write to CSV File
# writer, DictWriter
from csv import writer
with open('write.csv', 'w', newline="") as f:
    csv_writer = writer(f)
    # methods - writerow, writerows
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['yash', 'india'])
    # csv_writer.writerow(['harsh', 'up'])
    # csv_writer.writerow(['krish', 'aligarh'])
    
    csv_writer.writerows([['name', 'country'], ['yash', 'india'], ['harsh', 'up'], ['krish', 'aligarh']])


# *****************************************************************************************
# Tutorial 226 - Write to CSV using DictWriter
from csv import DictWriter
with open('write2.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname', 'lastname', 'age'])
    csv_writer.writeheader()
    # methods - writerow, writerows
    # csv_writer.writerow({
    #     'firstname' : 'yash',
    #     'lastname' : 'gupta',
    #     'age' : 20
    # })
    # csv_writer.writerow({
    #     'firstname' : 'harsh',
    #     'lastname' : 'gupta',
    #     'age' : 18
    # })
    # csv_writer.writerow({
    #     'firstname' : 'krish',
    #     'lastname' : 'gupta',
    #     'age' : 14
    # })
    # writerows --> [dict, dict, dict]
    csv_writer.writerows([
        {'firstname' : 'yash', 'lastname' : 'gupta', 'age' : 20},
        {'firstname' : 'harsh', 'lastname' : 'gupta', 'age' : 18},
        {'firstname' : 'krish', 'lastname' : 'gupta', 'age' : 14}
    ])


# *****************************************************************************************
# Tutorial 227 - Read and Write CSV files simultaneously
from csv import DictReader, DictWriter
with open('file1.csv', 'r') as rf:
    with open('file2.csv', 'w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['firstname', 'lastname', 'salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname = row['firstname']
            lname = row['lastname']
            slry = row['salary']
            csv_writer.writerow({
                'firstname' : fname.upper(),
                'lastname' : lname.upper(),
                'salary' : slry
            })

