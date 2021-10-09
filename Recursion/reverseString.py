def reverse(string):
    # # 1st Approach
    # if len(string) == 0:
    #     return
    # temp = string[0]
    # reverse(string[1:])
    # print(temp,end="")
    if len(string)<=1:
        return string
    return reverse(string[1:]) + string[0]
print(reverse('I m a fan of fan'))