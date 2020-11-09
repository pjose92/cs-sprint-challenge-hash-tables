#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

hashTable = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    #if it is none then that is the head(source)
    #if destination is none than that is the tail
    #need to organize tickets from departure to destaination 
    #build ticket dictionary
    for ticket in tickets:
        hashTable[ticket.source] = ticket.destination
    #initialize router
    curr_ticket = "NONE"
    #while not last flight, append current flight
    route = [hashTable[curr_ticket]]
    curr_ticket = hashTable[curr_ticket]

    while curr_ticket != "NONE":
        route.append(hashTable[curr_ticket]) #add current ticket
        curr_ticket = hashTable[curr_ticket]

    return route