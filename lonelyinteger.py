def lonelyinteger(a):
    # Write your code here
    for val in a:
        if a.count(val) == 1:
            result = val
            return result
