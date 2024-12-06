user_input = input("Enter a string: ")

# Обратить строку и проверить, равна ли она исходному вводу
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print ("The string is not a palindrome.")
     