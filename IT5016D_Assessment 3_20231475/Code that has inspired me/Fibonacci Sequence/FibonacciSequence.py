def PrintFibonacci(first, second, length):

    #Stop the printing and recursive calling if length reaches
    #the end.
    if(length == 0):
        return

    #Printng the next Fibonacci number.
    print(first + second, end=" ")

    #Recursively calling the function by updating the value and
    #decrementing the length.
    PrintFibonacci(second, first+second, length-1)

if __name__ == "__main__":
    #Print initial 2 values.
    print(0,1,end=" ")

    #Calling the Function to print the remaining length
    #fibonacci series
    PrintFibonacci(0,1,7-2)