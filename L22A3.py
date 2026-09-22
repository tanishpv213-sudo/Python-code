import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:" + str(array_num))

print("Number of occurences of the number 3 in the said array:")
print(str(array_num.count(3)))
array_num.reverse()
print("Reversed array:" + str(array_num))
