#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a cache for our hash table
    cache = {}
    # Create our list with our length of tickets
    route = [None] * length

    # Cycle through all of our tickets
    for i in tickets:
        # Assign source as key and destination as value
        cache[i.source] = i.destination

    # Make our first index of route the one that has a source of "NONE"
    route[0] = cache["NONE"]

    # Cycle through all the of our length to give us an index value, skipping 0 from earlier
    for i in range(1, length):
        # Find the next ticket based on the previous location and add it to our route
        route[i] = cache[route[i - 1]]

    return route
