class reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

word = input("Enter a word: ")
obj = reverse(word)
print("Reversed string:", obj.reverse_string())