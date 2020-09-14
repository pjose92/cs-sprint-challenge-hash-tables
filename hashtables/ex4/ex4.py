def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    TODO: "need to find what positive numbers have negative corresponding numbers"
    "results should come back with positive numbers"
    
    index = {}
    result = []
    
    for num in a:
        if num >= 0:
            if num in index:
                result.append(num)
            else:
                index[num] = 1
        else:
            negative = -num
            if negative in index:
                result.append(negative)
            else:
                index[negative] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
