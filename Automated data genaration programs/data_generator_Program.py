import csv 
import faker
import random

fields = ['Application ID', 'Vehicle ID', 'Application Status', 'Coverage', 'Cust ID'] 

rows = []

for i in range(0,100):
    mylist = []
    mylist.append(f'40BIS{(i+1)}')
    mylist.append(40+i)
    mylist.append(random.choice(['ACCEPTED','PENDING','REJECTED']))
    mylist.append(str(random.randint(0,10))+ ' SHEETS ATTACHED')
    mylist.append(400+i)
    rows.append(mylist)
    

filename = "applications.csv"
    
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(rows)