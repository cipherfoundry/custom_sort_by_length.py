# This script demonstrates the difference between a sorted list 
# and the original unsorted data.

def by_length(word):
    return len(word)

words = ["apple", "fig", "banana"]

sorted_by_length = sorted(words, key=by_length)

print(words)
print(sorted_by_length)
