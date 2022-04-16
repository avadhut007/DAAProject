
from flask import Flask, flash, render_template, request, redirect
from random import randint
import time

app = Flask(__name__)

# Function to generate random array
def create_random_array(array_len):
    input_array = []
    for i in range(0,array_len):
        input_array.append(randint(10,500))
    print(input_array)
    return input_array

# Function for merge sorting left and right arrays of input array
def merge_sort_algo(left_array,right_array):
    
    sorted_array = []
    left_index = 0
    right_index = 0
    while len(sorted_array) < len(right_array) + len(left_array):
        if left_array[left_index] <= right_array[right_index]:
            sorted_array.append(left_array[left_index])
            left_index = left_index + 1
        else:
            sorted_array.append(right_array[right_index])
            right_index = right_index + 1 

        if len(left_array)  == left_index:
            sorted_array.extend(right_array[right_index:]) 
            break        
        if len(right_array)  == right_index:
            sorted_array.extend(left_array[left_index:]) 
            break

    return sorted_array

# Function for Merge Sorting
def merge_sort_function(input_array):

    if len(input_array) < 2:
        return input_array

    mid_index = len(input_array)//2
    
    right_array = merge_sort_function(input_array[mid_index:])
    left_array = merge_sort_function(input_array[0:mid_index])

    sorted_array = merge_sort_algo(left_array,right_array)

    return sorted_array

# Function for Heapifying the input
def heapify_function(sorted_array, j, i):
    max_node = i
    left_node = 2*i + 1
    right_node = 2*i + 2
    sorted_array

    if left_node < j and sorted_array[max_node] < sorted_array[left_node]:
        max_node = left_node

    if right_node < j and sorted_array[max_node] < sorted_array[right_node]:
        max_node = right_node
    
    if max_node != i:
        sorted_array[max_node], sorted_array[i] =  sorted_array[i], sorted_array[max_node]
        heapify_function(sorted_array, j, max_node)

# Function for Heap Sorting
def heap_sort_function(input_array):
    sorted_array = input_array[:]
    init_time = time.time()
    array_len = len(sorted_array)

    for ind in range(array_len//2 -1, -1, -1):
        heapify_function(sorted_array,array_len, ind )
    
    for ind in range(array_len-1 , 0, -1):
        sorted_array[0], sorted_array[ind] = sorted_array[ind] , sorted_array[0]
        heapify_function(sorted_array,ind, 0 )
    final_time = time.time()
    exec_time = final_time - init_time
    return sorted_array,exec_time

# Function for partition in Quick sorting using last element as pivot
def quick_sort_algo(sorted_array,start,end):
    ind = start-1
    pivot = sorted_array[end]
    for j in range(start,end,1):
        if sorted_array[j] < pivot:
            ind+=1
            sorted_array[j], sorted_array[ind] = sorted_array[ind], sorted_array[j]
    sorted_array[end], sorted_array[ind+1] = sorted_array[ind+1], sorted_array[end]
    return ind+1

# Function for Quick Sorting
def quick_sort_function(sorted_array,start,end):
    
    if len(sorted_array) == 1:
        return sorted_array
    
    if start < end:
        pivot_index = quick_sort_algo(sorted_array,start,end)

        quick_sort_function(sorted_array, start, pivot_index-1)
        quick_sort_function(sorted_array, pivot_index+1, end)

# function to sort and update median values in 3 Median Quicksort
def quick_sort_3med_algo(sorted_array,start,end):
    first_pivot = sorted_array[start]
    middle_pivot = sorted_array[end//2]
    last_pivot = sorted_array[end]
    med_array = [first_pivot,middle_pivot,last_pivot]
    med_array.sort()
    median = med_array[1]
    sorted_array[start] = med_array[0]
    sorted_array[end] = med_array[1]
    sorted_array[end//2] = med_array[2]


# Function for Quick Sorting using 3 median
def quick_sort_3med_function(sorted_array,start,end):
    if start < end:
        quick_sort_3med_algo(sorted_array,start,end)
        quick_sort_function(sorted_array,start,end)

# Function for Insertion Sorting
def insertion_sort_function(input_array):
    sorted_array = input_array[:]
    init_time = time.time()
    for i in range(1,len(sorted_array)):
        key_element = sorted_array[i]
        index = i
        while index > 0 and key_element < sorted_array[index-1]:
            sorted_array[index] = sorted_array[index-1]
            index = index -1
        sorted_array[index] = key_element
    final_time = time.time()
    exec_time = final_time - init_time    
    return sorted_array,exec_time

# Function for Selection Sorting     
def selection_sort_function(input_array):
    sorted_array = input_array[:]
    init_time = time.time()
    for i in range(0,len(sorted_array)-1):
        minimum = i
        for j in range(i+1, len(sorted_array)):
            if  sorted_array[minimum] > sorted_array[j]:
                minimum = j
        sorted_array[minimum], sorted_array[i] = sorted_array[i], sorted_array[minimum]
    final_time = time.time()
    exec_time = final_time - init_time    
    return sorted_array,exec_time

# Function for Bubble Sorting 
def bubble_sort_function(input_array):
    sorted_array = input_array[:]
    init_time = time.time()
    for i in range(len(sorted_array)):
        for j in range(len(sorted_array)-i-1):
            if sorted_array[j+1] < sorted_array[j]:
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]
    final_time = time.time()
    exec_time = final_time - init_time
    return sorted_array,exec_time

# Home Route 
# To sort random input array and print sorted array and execution time
@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home_function():
    if request.method == 'POST':
        try:
            if 'array_len' in request.form:
                array_len = int(request.form["array_len"])
                selected_algo = request.form["selected_algo"]
                input_array = create_random_array(array_len)
                if selected_algo == "Mergesort":
                    init_time = time.time()
                    sorted_array = merge_sort_function(input_array)
                    final_time = time.time()
                    exec_time = final_time - init_time
                    print("Mergesort = ",sorted_array,exec_time)
                
                if selected_algo == "Heapsort":
                    sorted_array,exec_time = heap_sort_function(input_array)
                    print("Heapsort = ",sorted_array,exec_time)

                if selected_algo == "Quicksort":
                    sorted_array = input_array[:]
                    init_time = time.time()
                    quick_sort_function(sorted_array,0,len(sorted_array)-1)
                    final_time = time.time()
                    exec_time = final_time - init_time
                    print("Quicksort = ",sorted_array,exec_time)

                if selected_algo == "Quicksort3":
                    sorted_array = input_array[:]
                    init_time = time.time()
                    quick_sort_3med_function(sorted_array,0,len(sorted_array)-1)
                    final_time = time.time()
                    exec_time = final_time - init_time
                    print("Quicksort 3med = ",sorted_array,exec_time)

                if selected_algo == "Insertionsort":
                    sorted_array,exec_time = insertion_sort_function(input_array)
                    print("Insertionsort = ",sorted_array,exec_time) 

                if selected_algo == "Selectionsort":
                    sorted_array,exec_time = selection_sort_function(input_array)
                    print("Selectionsort = ",sorted_array,exec_time) 

                if selected_algo == "Bubblesort":
                    sorted_array,exec_time = bubble_sort_function(input_array)
                    print("Bubblesort = ",sorted_array,exec_time) 

                result_string =f"""The input array of length {array_len}  is {input_array}. <br><br>
                                   Using {selected_algo} sorted array is {sorted_array}. <br><br>
                                   Time taken to sort is {exec_time} """
                return render_template('home.html',result_string= result_string) 
                 
        except Exception as e:
            print(e,"Error has occured")
    
    return render_template('home.html')

# Compare Route 
# To compare execution time of all sorting alogorithms using Google Charts
@app.route("/compare", methods=['GET','POST'])
def compare_function():
    if request.method == 'POST':
        try:
            if 'array_len' in request.form:  
                array_len = int(request.form["array_len"])
                input_array = create_random_array(array_len)
                list_data=[]

                init_time = time.time()
                sorted_array = merge_sort_function(input_array)
                final_time = time.time()
                exec_time = final_time - init_time
                list_data.append(["Mergesort",exec_time])

                sorted_array,exec_time = heap_sort_function(input_array)
                list_data.append(["Heapsort",exec_time])

                sorted_array = input_array[:]
                init_time = time.time()
                quick_sort_function(sorted_array,0,len(sorted_array)-1)
                final_time = time.time()
                exec_time = final_time - init_time
                list_data.append(["Quicksort",exec_time])

                sorted_array = input_array[:]
                init_time = time.time()
                quick_sort_3med_function(sorted_array,0,len(sorted_array)-1)
                final_time = time.time()
                exec_time = final_time - init_time
                list_data.append(["Quicksort 3median",exec_time])

                sorted_array,exec_time = insertion_sort_function(input_array)
                list_data.append(["Insertionsort",exec_time])

                sorted_array,exec_time = selection_sort_function(input_array)
                list_data.append(["Selectionsort",exec_time])

                sorted_array,exec_time = bubble_sort_function(input_array)
                list_data.append(["Bubblesort",exec_time])
                print(list_data)
                input_size_string = f"Length of Input array is {array_len}."
                return render_template('barchart.html',data_for_chart=list_data,input_size_string=input_size_string)

        except Exception as e:
            print(e,"Error has occured")
    return render_template('compare.html')        

if __name__ == '__main__':
    app.run(debug=True)

