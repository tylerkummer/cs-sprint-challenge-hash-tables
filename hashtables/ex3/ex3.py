def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create hash table
    cache = {}

    # Create an empty array for our intersected list
    result = []

    # Cycle through our array with arrays
    for i in arrays:
        # Cycle through each individual array within our array of arrays
        for j in i:
            # Check if the individual number j is located in our hash table cache then
            if j in cache:
                # Increment the counter of cache by 1
                cache[j] += 1
                # Check if the the number in j is also in the rest of the arrays
                if cache[j] == len(arrays):
                    # If so then append our result array by j
                    result.append(j)
            else:
                # If not then just assign the cache of j to 1
                cache[j] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
