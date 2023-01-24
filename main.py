# " hello wordl"
print(" hello world")
print(" hello hamza")
print(" I WILL study proramming in UIT ")
# first prog FIND THE PASSWORD
secret_code= 10
guess_count = 0
while guess_count < 3:
    guess_number = int(input(" insert your code :"))
    if guess_number == secret_code :
        print(" you won ")
        break
    else:
       print( " try a gain")
       guess_count  +=1
