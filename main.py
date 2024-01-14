import numpy as np
# Create shortcuts to extenal files
file_path1 = "zadanie1/data_in_overview.txt"
file_path2 = "zadanie1/data_in_learning.txt"
file_path3 = "zadanie1/data_out_learning.txt"
file_path4 = "zadanie1/weights_evolution.txt"


#   Step 1   : Get usable Data 

# Data retrieval  from  data_in_overview.txt  file
with open(file_path1, 'r') as file:
    file.readline()
    file.read(16)
    speed = float(file.readline(10))

    file.read(10)
    precision = float(file.readline(10))

    file.read(8)
    bias = float(file.readline(10))

    file.read(4)
    w14 = float(file.readline(10))

    file.read(4)
    w24 = float(file.readline(10))
    
    file.read(4)
    w34 = float(file.readline(10))

    # Print out input variables (commented out)
    '''print("Speed: ",speed)
    print("Precision: ", precision)
    print("Bias: ", bias)
    print("Waga N1: ", w14)
    print("Waga N2:", w24)
    print("Waga N2:", w34)'''



# Data retrieval  from  data_in_learning.txt  file

with open(file_path2, 'r') as file1:

    # Populating arrays with starter data ( to be changed while retrieving)

    #Variable N or S:
    N_or_S = ["A", "A", "A", "A", "A", "A", "A", "A"]
    #input data for N1:
    q = [0, 0, 0, 0, 0, 0, 0, 0]
    #input data for N2:
    l = [0, 0, 0, 0, 0, 0, 0, 0]


    # Overlooking first line
    file1.readline()

    # Division of lines into individual elements
    # File has 8 lines to iterate through
    for i in range(0, 8):
        f_contents = file1.readline()
        f_contents = f_contents.split()
    
        q[i] = float(f_contents[2])
        l[i] = float(f_contents[3])
        N_or_S[i] = f_contents[1]
    # print out retrieved data (commented out)
    '''print("Assined value N or S ",N_or_S)
    print("Input data for N1: ", q)
    print("Input data for N2: ", l)'''


# Step 2    :  calculation section
# Defining creating and populating  boolean array / whether condition fulfilled/ Initially all switched to false as global variable
# to be deleted later on :
condition_fulfilled = ["False", "False", "False", "False", "False", "False", "False", "False"]



# Defining function for checking the condition ( )    

def check_sum(l, q, N_or_S, w14, w34, w24):
    
    # Juicy part of the function
    i = 0
    while i < 8:
        suma = float(q[i])*w14+float(l[i])*w24+bias*w34
        if N_or_S[i] == 'N'  and suma > 0:
            condition_fulfilled[i] = 'True'
        elif N_or_S[i] == 'S' and suma < 0:
            condition_fulfilled[i] = 'True'
        else:
            condition_fulfilled[i] = 'False'
        i = i+1
    return condition_fulfilled

# Defining function for improving the weights 

def poprawa_wag(speed, w14, w34, w24, N_or_S, bias, condition_fulfilled):
    i=0 
    while i< 8:
      if condition_fulfilled[i] == 'False' and N_or_S[i] == 'N':
        w14 = w14 + (float(q[i])*speed)
        w24 = w24 + (float(l[i])*speed)
        w34 = w34 + (float(bias)*speed)
        return w14, w24, w34
      if     condition_fulfilled[i] == 'False' and N_or_S[i] == 'S':
          w14 = w14 + (-1*float(q[i])*speed)
          w24 = w24 + (-1*float(l[i])*speed)
          w34 = w34 + (-1*float(bias)*speed)
          return w14, w24, w34
      i = i+1


# In this part I'll be calling both functions several times and keeping the results in new variables each time  ( to use in next part )    
# First checking
condition_fulfilled = check_sum(l, q, N_or_S, w14, w34, w24)

#Saving this outcome (first table)
condition_fulfilled_1 = condition_fulfilled.copy()


#Saving first generation weights
w14_1 = w14
w24_1 = w24
w34_1 = w34
# First changing values of weights
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, N_or_S, bias, condition_fulfilled)


# Second checking
condition_fulfilled = check_sum(l, q, N_or_S, w14, w34, w24)


#Saving this outcome (second table)
condition_fulfilled_2 = condition_fulfilled.copy()

#Saving second generation weights
w14_2 = w14
w24_2 = w24
w34_2 = w34

# Second changing values of weights
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, N_or_S, bias, condition_fulfilled)


# Third checking
condition_fulfilled = check_sum(l, q, N_or_S, w14, w34, w24)

#Saving this outcome (third table)
condition_fulfilled_3 = condition_fulfilled.copy()

#Saving third generation weights
w14_3 = w14
w24_3 = w24
w34_3 = w34
# 3. changing values of weights
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, N_or_S, bias, condition_fulfilled)

# 4. checking
condition_fulfilled = check_sum(l, q, N_or_S, w14, w34, w24)

#Saving this outcome (4. table)
condition_fulfilled_4 = condition_fulfilled.copy()

#Saving 4. generation weights
w14_4 = w14
w24_4 = w24
w34_4 = w34
# 4. changing values of weights
w14, w24, w34 = poprawa_wag(speed, w14, w34, w24, N_or_S, bias, condition_fulfilled)


# 5. checking
condition_fulfilled = check_sum(l, q, N_or_S, w14, w34, w24)

#Saving this outcome (5. table)
condition_fulfilled_5 = condition_fulfilled.copy()

#Saving 5. generation weights
w14_5 = w14
w24_5 = w24
w34_5 = w34




# FINAL PART : WRITING DATA OUT TO FILES

# I'll start this part with writing data to weights_evolution.txt
with open(file_path4, 'w') as file4:
    file4.write("Epoch    W14       W24       W34\n")
    file4.write(f"Epoch1  {w14_1}       {w24_1}       {w34_1}\n")
    file4.write(f"Epoch2  {round(w14_2, 1)}        {w24_2}         {w34_2}\n")
    file4.write(f"Epoch3  {round(w14_3)}         {round(w24_3)}          {round(w34_3)}\n")
    file4.write(f"Epoch4  {round(w14_4)}         {round(w24_4)}          {round(w34_4)}\n")
    file4.write(f"Epoch5  {round(w14_5)}         {round(w24_5)}          {round(w34_5)}")


# Now the most difficult part. Write data to data_out_learning.txt

with open(file_path2, 'r') as file2: 
      with open(file_path3, 'w') as file3: 
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}     Epoch1    Epoch2    Epoch3    Epoch4    Epoch5\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[0]}     {condition_fulfilled_2[0]}      {condition_fulfilled_3[0]}     {condition_fulfilled_4[0]}      {condition_fulfilled_5[0]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[1]}     {condition_fulfilled_2[1]}      {condition_fulfilled_3[1]}     {condition_fulfilled_4[1]}      {condition_fulfilled_5[1]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[2]}     {condition_fulfilled_2[2]}      {condition_fulfilled_3[2]}     {condition_fulfilled_4[2]}      {condition_fulfilled_5[2]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[3]}     {condition_fulfilled_2[3]}      {condition_fulfilled_3[3]}     {condition_fulfilled_4[3]}      {condition_fulfilled_5[3]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[4]}     {condition_fulfilled_2[4]}      {condition_fulfilled_3[4]}     {condition_fulfilled_4[4]}      {condition_fulfilled_5[4]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[5]}     {condition_fulfilled_2[5]}      {condition_fulfilled_3[5]}     {condition_fulfilled_4[5]}      {condition_fulfilled_5[5]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[6]}     {condition_fulfilled_2[6]}      {condition_fulfilled_3[6]}     {condition_fulfilled_4[6]}      {condition_fulfilled_5[6]}\n" )
            content_of_file2 = file2.readline()
            file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[7]}     {condition_fulfilled_2[7]}      {condition_fulfilled_3[7]}     {condition_fulfilled_4[7]}      {condition_fulfilled_5[7]}\n" )
            #content_of_file2 = file2.readline()
            #file3.write(f"{content_of_file2[:-1]}       {condition_fulfilled_1[8]}     {condition_fulfilled_2[8]}      {condition_fulfilled_3[8]}     {condition_fulfilled_4[8]}      {condition_fulfilled_5[8]}" )

