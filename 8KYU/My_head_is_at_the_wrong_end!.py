# First method
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]

# Second method
def fix_the_meerkat(arr):
    return arr[::-1]

# Third method
def fix_the_meerkat(arr):
    arr.reverse()
    return arr
