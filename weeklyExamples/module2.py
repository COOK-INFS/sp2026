import module1

print('This is the main script.')

# Call the helper function from module 1.
module1.helper_function()

# Call the main function from module 1.
module1.main()

print("-------------------------")
print(f"Module 2's name is: {__name__}")
print(f"Module 1's name is: {__name__}")