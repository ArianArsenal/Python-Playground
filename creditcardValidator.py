import os

os.system("cls")

credit_card = input("Enter Credit Card Number : ")
credit_card = credit_card.replace("-", "")
credit_card = credit_card.replace(" ","")

if len(credit_card) != 16 and len(credit_card) != 19:
    print("Invalid Credit Card Number")
else:
    if credit_card.isdigit() == False:
        print("Invalid Credit Card Number")
    else:
        credit_card = credit_card[::-1]

        sum_odd_digits = 0
        sum_even_digits = 0
        total_sum = 0

        for i in credit_card[::2]:
            sum_odd_digits += int(i)
        for x in credit_card[1::2]:
            x = int(x) * 2
            if x >= 10 :
                sum_even_digits += (1 + (x % 10))
            else:
                sum_even_digits += x
        
        total_sum = sum_odd_digits + sum_even_digits

        if total_sum % 10 == 0:
            print("Valid Credit Card Number")
        else:
            print("Invalid Credit Card Number")


#https://en.wikipedia.org/wiki/Luhn_algorithm



