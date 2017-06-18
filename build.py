def solution(list_of_nums):
    """Enter Code Here"""
    result = {'ODD': 0, 'EVEN': 0}
    for num in list_of_nums:
        if num % 2 == 0:
            result['EVEN']+=1
        else:
            result['ODD']+=1
    return result
