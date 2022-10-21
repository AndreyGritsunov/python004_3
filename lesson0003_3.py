def result_print(sum_result):

    print("Ответ: " + str(sum_result))

def sum_number():
    max = 0
    min = 0
    
    for i in range(0, len(n)):
        
        m =  str(n[i]).split(".")

        if len(m) == 2:
            number = n[i] - int(m[0])

            if number > max:

                max = number

            elif number < min:

                min = number

    result_print(max - min) 
       
        
 
n = [1.1, 1.2, 3.1, 5, 10.01]
sum_number()