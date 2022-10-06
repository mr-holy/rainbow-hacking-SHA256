import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    sha256_dic=dict()
    list_new = []
    with open(input_file_name,'r') as f:
        reader = csv.reader(f)
        for i in range(1000,10000):
            sha256_dic[hashlib.sha256(str(i).encode()).hexdigest()] = i
        for row in reader :
            list_new.append((row[0],sha256_dic[row[1]]))
    with open(output_file_name,'a') as f:
        for x,y in list_new :
            f.write("%s,%s\n" %(x,y))
