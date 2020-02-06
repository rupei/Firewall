# Firewall

## Testing Procedure

I created unit tests (unit.py) to test subroutines, went through the original suite of tests (in test1.py), and made my own sanity tests (sanity.py) Due to the nature of this project, the main edge cases I considered were invalid inputs to accept_packet (given that there is no guarantee that the inputs are valid). We also ensure that the range of our ports and ip addresses are inclusive. All of these edge cases are written in sanity.py.

Additionally, a random rule and input performance test was conducted to measure the speed of our Firewall. Each call to accept_packet took on average 2.68 microseconds, which is quite good considering that the time it took to randomly generate an integer is also factored into that. Needless to say, our Firewall would not experience that much Latency

## Design Choices

Before beginning to code, I wondered if instead of using an tuple/list, if I could take advantage of a hashset and given a range, simply "flatten" that range down into individual values (i.e. if the port range was from 80-85, I would create 6 entries corresponding to each port number). This way, instead of our accept_packet runtime being O(r) where r := the number of rules, it would be O(1). 

However, in timetest.py, I tried to see what would happen if this was attempted on the entire range of IP addresses (255^4). Not only did my machine run out of memory, but since over a billion points needed to be added, the constructor was very slow. For all practical purposes, I decided to use this iterated tuple/list approach.

I also considered using a class hiearchy for the different "sub-rule sets," but realized that would probably overcomplicate what is otherwise a relatively simple problem.

## Refinements/Optimizations

If I had more time, I would consider using numpy/pandas to potentially speed up my Firewall's performance. Since dealing with vanilla Python iterables can't take advantage of the parallelized methods of those libraries. If I could've done that, I would've used my current solution as a 'reference' for functionality (i.e. I could randomly generate rules and calls to accept_packet and assert that the two outputs are the same).

## Team Preference

1. Data
2. Platform
3. Policy
