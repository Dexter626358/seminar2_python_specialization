number = 1000
hexinary = hex(number)[2::]
def getNumber(number, system):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    result = alphabet[number % system]

    while number >= system:
        number //= system
        result += alphabet[number % system]
    return result[::-1]


for i in range(1, 1000):
    print(f"Число по основанию  10: {i}, Число по основанию 16 функция hex(): {hex(i)[2::]}, моя функция: {getNumber(i, 16)}, {hex(i)[2::] == getNumber(i, 16)}")

