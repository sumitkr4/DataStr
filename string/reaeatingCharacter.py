def findRepeat(string):
    temp=[]*256
    for item in string:
        if item not in temp:
            temp.append(item)
        else:
            return item
    return 'not repeat'
string="sumits"
print(findRepeat(string))