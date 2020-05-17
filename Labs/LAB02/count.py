

def count_char(text):
    count = {}
    for t in text:
        count[t] = text.count(t)

    for t in count:
        print(t, count[t])
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count
    pass

def count_char_insensitive(text):
    text = text.lower()
    count = {}
    for t in text:
        count[t] = text.count(t)
    
    for t in count:
        print(t, count[t])
    # TODO do the same as `count_char` but in a case-insensitive manner
    pass


def count_char_ordered(text):
    text = text.lower()
    count = {}
    for t in text:
        count[t] = text.count(t)
    
    counted = sorted(count, key = count.get, reverse=True)
    for t in counted:
        print (t, count[t])
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)
    pass

count_char_ordered('HelloOo!')
