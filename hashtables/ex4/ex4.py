def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Didn't use hash table

    # # Create empty array for our results, positive and negative numbers
    # result = []
    # positive = []
    # negative = []

    # # Cycle through our array
    # for i in a:
    #     # Check if it is a positive number
    #     if i > 0:
    #         # Append it to our positive array
    #         positive.append(i)
    #     else:
    #         # Else append the absolute value to our negative array
    #         negative.append(abs(i))

    # # Loop through our positive array
    # for i in positive:
    #     # Check if i exists in negative
    #     if i in negative:
    #         # Check if i does not exist in the result
    #         if i not in result:
    #             # Append i to the result
    #             result.append(i)

    # Uses hash table

    # Create a hash table
    cache = {}
    # Create a result array
    result = []

    # Cycle through a
    for i in a:
        # Check if the absolute value is in the cache
        if abs(i) in cache:
            # If it is then we have a match for both positive and negative numbers, so append it to the result array
            result.append(abs(i))
            # Set the cache of the abs of i to increment by 1
            cache[abs(i)] += 1
        # If the absolute value is not in cache then just asign it to 1
        else:
            cache[abs(i)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
