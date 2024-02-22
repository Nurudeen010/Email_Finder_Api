# function for sorting of emails

def sortingInput(text_input):
    finalList = []
    check = set()
    for input in text_input:
        newList = input.lower()
        if newList not in check:
            finalList.append(newList)
            check.add(newList)
    return finalList

