import inflect

def generate_table_name(class_name):
    words = [[str[0]]]
    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)
    return inflect.engine().plural('_'.join(''.join(word) for word in words).lower())



# Driver code
str = "CallReview"
print(generate_table_name(str))