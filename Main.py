import random
import string


def get_random_string():
    length=int(input("Kaç karakterli Olsun ? "))
    letters = string.hexdigits
    yenilikler=string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Oluşturulan", length, "Haneli Şifreniz = \t", result_str)



