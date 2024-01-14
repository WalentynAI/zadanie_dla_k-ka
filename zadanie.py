import numpy as np
# Create shortcuts to extenal files
file_path1 = "zadanie/data_in_overview.inf"
file_path2 = "zadanie/data_in_learning.txt"
file_path3 = "zadanie/data_out_learning.txt"




file_path3 = "zadanie/data_out_learning.txt"
with open(file_path2, 'r') as file:
     with open(file_path3, 'w') as file1:
        for line in file: 
            file1.write(line)

with open(file_path3, 'r') as file1:
    modified_lines = [line.strip() + "                                                             " for line in file1]
with open(file_path3, 'w') as file1:
       file1.write('\n'.join(modified_lines))  
       file1.seek(15)
       file1.write("Epoka1")
       file1.seek(25)
       file1.write("Epoka2")
       file1.seek(35)
       file1.write("Epoka3")         
       file1.seek(45)
       file1.write("Epoka4")
       file1.seek(55)
       file1.write("Epoka5")



with open(file_path2, 'r') as file:
     with open(file_path3, 'w') as file1:
        for line in file: 
            file1.write(line )

with open(file_path3, 'r') as file1:
    modified_lines = [line.strip() + "                                                             " for line in file1]
with open(file_path3, 'w') as file1:
       file1.write('\n'.join(modified_lines))  
       file1.seek(15)
       file1.write("Epoka1")
       file1.seek(25)
       file1.write("Epoka2")
       file1.seek(35)
       file1.write("Epoka3")         
       file1.seek(45)
       file1.write("Epoka4")
       file1.seek(55)
       file1.write("Epoka5")
       file1.seek(80+5)
       

with open(file_path1, 'r') as file:
    
    con = file.readline()

    con = file.read(16)
    speed = file.readline(10)
    speed = float(speed)
    #print("\n")
    con = file.read(10)
    precision = file.readline(10)
    precision = float(precision)
    #print("\n")
    con = file.read(8)
    bias = file.readline(10)
    bias = float(bias)
    #print("\n")
    con = file.read(4)
    w14 = file.readline(10)
    w14 = float(w14)
    #print("\n")
    con = file.read(4)
    w24 = file.readline(10)
    w24 = float(w24)
    #print("\n")
    con = file.read(4)
    w34 = file.readline(10)
    w34 = float(w34)
   



    #print(con)
    print("Speed: ",speed)
    print("Precision: ", precision)
    print("Bias: ", bias)
    print("Waga N1: ", w14)
    print("Waga N2:", w24)
    print("Waga N2:", w34)

    #print(float(speed[:0]))
    

    #print(file.tell())
    print("\n***************\n")

with open(file_path2, 'r') as file1:
    NlubS = ["A", "A", "A", "A", "A", "A", "A", "A"]
    q = [0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0, 0, 0]
    #print(NlubS)
    con = file1.readline()
    elements = con.split()
    #print(con)
    #print(elements[2])
   # print("\n***************\n")



    con = file1.readline()
    elements = con.split()
    #print(con, "\n")
    l[0]  = elements[3]
    q[0]  = elements[2]
    NlubS[0] = elements[1]
    #print(NlubS)
    #print(elements[1], "\n")


    con = file1.readline()
    #print(con)
    elements = con.split()
    l[1]  = elements[3]
    NlubS[1] = elements[1]
    q[1]  = elements[2]
    #print(NlubS)


    con = file1.readline()
    #print(con)
    elements = con.split()
    l[2]  = elements[3]
    NlubS[2] = elements[1]
    q[2]  = elements[2]


    con = file1.readline()
    #print(con)
    elements = con.split()
    l[3]  = elements[3]
    NlubS[3] = elements[1]
    q[3]  = elements[2]


    con = file1.readline()
   # print(con)
    elements = con.split()
    l[4]  = elements[3]
    NlubS[4] = elements[1]
    q[4]  = elements[2]


    con = file1.readline()
   # print(con)
    elements = con.split()
    l[5]  = elements[3]
    NlubS[5] = elements[1]
    q[5]  = elements[2]


    con = file1.readline()
   # print(con)
    elements = con.split()
    l[6]  = elements[3]
    NlubS[6] = elements[1]
    q[6]  = elements[2]


    con = file1.readline()
   # print(con)
    elements = con.split()
    l[7]  = elements[3]
    NlubS[7] = elements[1]
    q[7]  = elements[2]
    print("Przypisana wartość N lub S ",NlubS)
    print("Dane wejściowe do neuronu 1: ", q)
    print("Dane wejściowe do neuronu 2: ", l)


'''print("\n**********\n")
with open(file_path2, 'r') as file1:
    i=1
    file1.seek(0)
    for line in file1:
        con = file1.readline()
        elements = con.split()
        print(f"Elementy z linii: {i}")
        print(elements) 
        i = i+1   
print("\n**********\n")
'''
'''with open(file_path2, 'r') as file1:
    bob = file1.readlines()
    rows = 9
    cols = 4
    matrix = np.zeros((rows, cols))
    print(matrix)
   
    print(matrix)
    mat[1]= [7,5]
    mat[0] = bob[0][0]
    print(mat)

    
import sys

print(sys.version)
'''
bib = ["False", "A", "A", "A", "A", "A", "A", "A"]
print("\n\n\n\n")
#print(bib)

def sprawdzenie(l, q, NlubS, w14, w34, w24, bib):
    #bib = ["False", "A", "A", "A", "A", "A", "A", "A"]
    #print(bib) 
    #print(bib) 
    i = 0
    while i < 8:
        suma = float(q[i])*w14+float(l[i])*w24+bias*w34
        if NlubS[i] == 'N'  and suma > 0:
            bib[i] = 'True'
        elif NlubS[i] == 'S' and suma < 0:
            bib[i] = 'True'
        else:
            bib[i] = 'False'
        i = i+1
    return bib
       
    
    
#def zapis_do_data_out_learning(bib):
   # if 'False' 



def poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib):
    i=0 
    while i< 8:
      if bib[i] == 'False' and NlubS[i] == 'N':
        w14 = w14 + (float(q[i])*speed)
        w24 = w24 + (float(l[i])*speed)
        w34 = w34 + (float(bias)*speed)
        return w14, w24, w34
      if     bib[i] == 'False' and NlubS[i] == 'S':
          w14 = w14 + (-1*float(q[i])*speed)
          w24 = w24 + (-1*float(l[i])*speed)
          w34 = w34 + (-1*float(bias)*speed)
          return w14, w24, w34
      i = i+1
             

print("Wyniki dla epoka 1: ")
# tutaj wykorzystano jeszcze wagi 1 epoki
w14_1 = w14
w24_1 = w24
w34_1 = w34
print(sprawdzenie(l, q, NlubS, w14, w34, w24, bib))
print("table1: ")
with open(file_path3, 'w') as file1:
    print('')

TABLE = sprawdzenie(l, q, NlubS, w14, w34, w24, bib)
print(TABLE)






poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib)
#wagi drugiej epoki 
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib)
w14_2 = w14
w24_2 = w24
w34_2 = w34
print("Wyniki dla epoka 2: ")
print(sprawdzenie(l, q, NlubS, w14, w34, w24, bib))
print("table1: ")

print(TABLE)
table2= bib
#wagi 3 epoki
w14_3 = w14
w24_3 = w24
w34_3 = w34
print("Wyniki dla epoka 3: ")
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib)
print(sprawdzenie(l, q, NlubS, w14, w34, w24, bib))
table3= bib
#wagi 4 epoki
w14_4 = w14
w24_4 = w24
w34_4 = w34
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib)
print("Wyniki dla epoka 4: ")
print(sprawdzenie(l, q, NlubS, w14, w34, w24, bib))
table4= bib
#wagi 5 epoki
w14_5 = w14
w24_5 = w24
w34_5 = w34




w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, NlubS, bias, bib)
print("Wyniki dla epoka 5: ")
print(sprawdzenie(l, q, NlubS, w14, w34, w24, bib))
table5= bib
print("table1: ")




       


            
           
       
     
         






