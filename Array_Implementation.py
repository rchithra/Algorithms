# Here, we implement our own array with common methods such as access, push, pop, insert,delete


class My_array():

    def __init__(self):
        self.length = 0  # Initializing array length to 0
        self.data = {}  # Initializing array data using empty dictionary.Keys correspond to index and value to data.

    def __str__(self):
        return str(self.__dict__)  # Print attribute of array(length and data) in string format.

    def get(self, index):
        return self.data[index]  # returns element at the given index at O(1) time.

    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item  # Adds given element to the end of array.

    def pop(self):
        last_item = self.data[self.length - 1]  # Collects last element.
        del self.data[self.length - 1]  # Deletes the last element.
        self.length -= 1  # Decrements the length of the array by 1
        return last_item  # Returns the popped element at O(1) time.

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i + 1]  # Shifts every element from index by one place towards right.
        self.data[index] = item  # Adds the element at given index in O(n) time.

    def delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # Shifts every element from index to end by one place to left.
        del self.data[self.length - 1]  # The last element is deleted as it appears twice
        self.length -= 1  # Length of array decremented by 1 in O(n) time


arr = My_array()
arr.push(6)
arr.push(2)
arr.pop()
arr.push(45)
arr.insert(3, 10)
# arr.delete(4)
print(arr.get(1))
