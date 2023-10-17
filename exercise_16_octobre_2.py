#fonctions crée (sqrt,average,odd_or_not,compute_sum)
class Math():
    def sqrt(self, number):
        number = number ** (1/2)
        return number

    def average(self, numbers):
        list = 0
        number = 0
        for i in numbers:
            list += i
            number += 1
            average = list/number
        return average

    def odd_or_not(self, number):
        if (number%2!=0):
            print(f"{number} is odd")
        else:
            print(f"{number} is even")


    def compute_sum(self, numbers):
        result = 0
        for number in numbers:
            result += number
        return result

math = Math()  # instance the class to use insides function
print('The square root of 9 is {}\n'.format(math.sqrt(9)))

print("The average of 10, 30, 20 and 10 is {}".format(math.average([10,30,20,10])))
print()
math.odd_or_not(11)
print()
math.odd_or_not(4)
print()
print("The sum of 10, 30, 10, 40 and 20 is {}".format(math.compute_sum([10,30,10,40,20])))