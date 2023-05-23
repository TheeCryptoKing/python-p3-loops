#!/usr/bin/env python3
# function happyNewYear() {
#   let counter = 10;
#   while (counter > 0) {
#     console.log(counter);
#     counter--;
#   }
#   console.log("Happy New Year!");
# }
def happy_new_year():
    # code goes here!
    counter = 10
    while (counter > 0):
        print(counter)
        counter -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i) 
