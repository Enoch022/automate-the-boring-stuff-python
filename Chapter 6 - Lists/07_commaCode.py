# Returns a comma-separated string with "and" before the last item

def comma_code(spam):
    if len(spam) == 0:
        return ''
    if len(spam) == 1:
        return spam[0]

    return ', '.join(spam[:-1]) + ', and ' + spam[-1]


example = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(example))
