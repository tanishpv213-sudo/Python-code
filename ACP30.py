
class Roman:
    def convert(self, num):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"),
            (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value

        return result


n = int(input("Enter an integer: "))

if 1 <= n <= 3999:
    obj = Roman()
    print("Roman numeral:", obj.convert(n))
else:
    print("Enter a number between 1 and 3999.")


class Roman:
    def convert(self, num):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"),
            (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value

        return result


n = int(input("Enter an integer: "))

if 1 <= n <= 3999:
    obj = Roman()
    print("Roman numeral:", obj.convert(n))
else:
    print("Enter a number between 1 and 3999.")
