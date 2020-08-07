def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    # Create empty array for our results, positive and negative numbers
    result = []
    positive = []
    negative = []

    # Cycle through our array
    for i in a:
        # Check if it exists in the cache
        if i not in cache:
            # Check if it is a positive number
            if i > 0:
                # Append it to our positive array
                positive.append(i)
            else:
                # Else append the absolute value to our negative array
                negative.append(abs(i))
        else:
            # If it doesn't exist in cache asign the cache of i to i
            cache[i] = i

    # Loop through our positive array
    for i in positive:
        # Check if i exists in negative
        if i in negative:
            # Check if i does not exist in the result
            if i not in result:
                # Append i to the result
                result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
