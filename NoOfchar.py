def NoOfChar(text,s):
    count = 0
    for letter in text:
        if letter == s:
            count =  count + 1
    return count
