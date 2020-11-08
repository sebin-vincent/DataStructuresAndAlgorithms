def in_place_string_reversal(text):
    length = len(text)
    str = []
    str[:0] = text
    i = 0
    j = length - 1
    a = ""
    while i != j:
        a = str[j]
        str[j] = str[i]
        str[i] = a
        i += 1
        j -= 1
    return str


txt = "sebin"
print(in_place_string_reversal(txt))
