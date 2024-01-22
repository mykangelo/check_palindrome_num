



#create a function for a palindrome check
def palindrome_check(num):
    print("original number", num)
    orig_num = (str(num)) # equate the orig num from the given num and convert num into string

    reversed_num = (str(num)[ : :-1]) # use a string slicing to reverse the original num by using the start:stop:step

    if orig_num == reversed_num: #start a if condition to check if the orig num is equal to reversed num
        print("The given number is a palindrome")
    else: 
        print("The given number is not palindrome")

#call the function with the given number
palindrome_check(121)
palindrome_check(125)



