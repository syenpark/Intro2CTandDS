###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip = []
    trips = []
    trip_weight = 0
    
    # refer: def __getitem__(self, key): return self.data[key]
    # heaviest_cows = sorted(cows, key=cows.__getitem__, reverse=True)
    heaviest_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    heaviest_cows = [name for (name, weight)in heaviest_cows]    
 
    while heaviest_cows:
        # To prevent unexpected result caused by the altered list,
        # use copy of the list
        for name in heaviest_cows[:]: 
            weight = cows[name]
            
            if weight + trip_weight <= limit:
                # Checks still here (the cow is not loaded yet);
                # Already gone, just skip;
                # Still here, load the cow
                try:
                    heaviest_cows.index(name)
                except:
                    pass
                else:
                    trip.append(name)
                    trip_weight += weight
                    heaviest_cows.remove(name)
            elif weight > limit:
                heaviest_cows.remove(name)
            
        trips.append(trip)
        trip = []
        trip_weight = 0
        
    return trips
    
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Generates all the possible partitions of cows for the brute force method;
    possible_trips = get_partitions(cows)
    
    # Sorts all partitions by ascending # of trips order
    sorted_trips = sorted(possible_trips, key=lambda x: len(x))
    
    # Checks each trip's validity from the trip that has the minimum # of trips 
    for trip in sorted_trips:
        spaceship = []
        cargo_weight = 0
        
        for riders in trip:
            # Total weight of cows in a cargo
            cargo_weight = sum([cows[cow] for cow in riders])
            
            # If overweighted, this partition is impossible to travel
            if cargo_weight > limit:
                break
            else:
                spaceship.append(riders)
        
        # If every partition in a trip is valid, this go on a trip! 
        else:
            return spaceship
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print('greedy_cow_transport:', end - start)
    
    print('')
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print('brute_force_cow_transport:', end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
cows = load_cows("ps1_cow_data.txt")
#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
limit=10
print(cows, '\n')
compare_cow_transport_algorithms()

