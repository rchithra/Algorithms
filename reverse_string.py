# A string is given, print the reversed string.

# The first solution is to create a new array and append the characters of original array.

def simple_reverse(string):
    new_string = []
    for i in range(len(string) - 1, -1, -1):  # traversing once through the array - O(n)
        new_string.append(string[i])  # Creating a new array - O(n)
    return ''.join(new_string)


string = " Hi How are you?"
print(simple_reverse(string))

# A better way of reversing a string, by taking a pair of elements from either end of string and swapping it till the
# middle of the string. By this we avoid creating a new array and time complexity will be O(n)

def swap(string, a, b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)


def smarter_reverse(string):
    for i in range(len(string) // 2):
        string = swap(string, i, len(string) - i - 1)
    return string


print(smarter_reverse("What is happening"))

# Reverse string using built-in functions- time complexity will be O(n)
string1 = "This is awesome!"
string2 = reversed(string1)
print(''.join(string2))

string1 = list(string1)
string1.reverse()
print(''.join(string1))