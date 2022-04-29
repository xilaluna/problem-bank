# Given a sorted array of strings, write a recursive function to find the index of the first
# and last occurrence of a target string.
# If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)

instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_indexes(arr, name):
    output = []

    def recursive_find(index):

        if index >= len(arr):
            return

        elif arr[index] == name and len(output) == 0:
            output.append(index)

        elif arr[index] != name and len(output) == 1:
            output.append(index - 1)

        index += 1
        recursive_find(index)

    recursive_find(0)
    return output


print(find_indexes(instructors, 'Braus'))
