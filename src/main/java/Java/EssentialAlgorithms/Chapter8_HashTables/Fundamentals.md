# HashTable vs. Lists
- HashTables provide a way that allows you to 
calculate the location of an element directly
    - no  traversal
    - no worry about sorting
- reads/access are O(1) operations
    - faster even than interpolation search. 
    
## FUNDAMENTALS
HashTable MAPS data to locations in a data structure
- a.k.a associative arrays (i.e. they associate a key w/ a value)
- a.k.a dictionaries 

HASHTABLE REQUIREMENTS
- data structure to store the data
- a hashing function to map keys to locations in the data 
structure
- a collision-resolution policy to determine what to do
when keys collide
- functionality:
    - write new keys
    - read existing keys
    - remove keys (most, but not all, impls allow this.)
    - resizing arrays
        - another "optional" feature.
        - INCREASE:
            - decreases fill percentage so collisions are
            less likely
        - DECREASE
            - reclaim freed space

HASHING
- the process of mapping a key to a value
    - traits of good hashing functions
        - data is spread out throughout table avoiding
        "clustering"
        - minimized collisions
        - similar key values should be mapped to 
        dissimilar locations in the table so that the
        location isn't predictable
        - no duplicate keys!
        
COLLISIONS:
- when two keys hash to the same value.

COLLISION-RESOLUTION POLICY:
- determines how to handle collision scenarios

FILL PERCENTAGE
- this is the ratio of used-to-total locations in a hashtable
- the greater the fill pct, the more likely it is that 
a collision will occur.

## CHAINING
A hash table (usually impl'd as an array) that uses BUCKETS 
to hold key values
- BUCKETS = "a collection of entries" 
    - (each bucket is usually a linked list)
    
PROS
- you don't need to expand/shrink
    

CONS
- if you don't expand/shrink, linked lists can get long
(results in a perf hit for finds/remove)
    - can be remediated by increasing the size of the
    hash table (array) itself which creates MORE buckets
    - this requires rehashing the table though.    
- another downside of rehashing to create more buckets is that
it results in wastage due to more emtpy buckets taking up
resources

## PERF
- hashing a key to find a bucket = O(1)
- adding value to top of a bucket = O(1)
- validating that a key doesn't exist
    - O(N/B) steps, for N items across B buckets
    - this assumes a reasonable distribution of data 
    across buckets
    -  sorting the Buckets also makes this faster
    (if you find a larger key, you can stop searching
    rather than wasting iterations)
- removing keys (same as validating that key doesn't exist)
- rehashing = O(N)

    
## OPEN ADDRESSING
(review pros/cons of Chaining)

values are stored in an array
- a calc serves as a hashing function, mapping values
into the array. 
    - ex: if HashTable uses array w/ M entries, simple func
    could be mapping key K into array position K mod M
- different hashing functions/collision resolution policies,
but
    - but consistent result is a collision resolution policy
    that produces a sequence of locations in the array for
    a value.
- this means that a COLLISION results in the algorithm
    continuing to retry for an empty location in the array
    or concludes that it is full (or can't locate one
    in a reasonable amount of time.)
    
### PROBE SEQUENCE
This is the sequence of locations that an open addressing algorithm 
uses to locate keys. 

- the average length of probe sequences for values
that may/may not be in the hash table give a good 
indication  of how efficient that hash table is. 

SEQUENCE
- probe keeps progressing until it
    - finds the item (Done!)
    - hits an empty entry
        - item is not present!
    - probe visits M entries, where M is the size
    of the data structure 
        - item is not present!
        - NOTE: this doesn't mean that the probe sequence has
        reached every entry in the array. It only means that
        it has mathematically visited the same number of 
        elements that the array can hold. If the 
        sequence repeats before visiting all of the
        elements in the array, then it will leave
        blank entries.

PROS
- can be rehashed faster than chained structures to 
reduce fill pct/collision probability

CONS
- its possible that a probe sequence might be unable to find
an empty location, even if one exists.
    - NOTE: this happens when a probe sequence repeats w/o 
    visting all of the elements (BAD)
    
PERFORMANCE
- fast @ reasonable fill pct
- if average probe is 1-2, adding/locating = O(1)
- degrades if array becomes too full. 
    - worse case O(N) if array has N items and is
    completely full.
- rehashing = O(N)

#### REMOVING ITEMS IN A PROBE SEQUENCE
- it is possible for an item in an array to be part of
another item's probe sequence. 
    - i.e. if an item is removed, but it is part of 
    another probe sequence, it would be impossible to find
    the values in the second probe sequence that come after
    the removed item.
    
POSSIBLE SOLUTIONS
- marking item to be deleted
    - PRO: this solves the case of a value being part of
        multiple probe sequences
    - CON: we are wasting space w/ a bunch of values 
        we can't use/don't need
        - waste of space
        - slow search/traversal
    - potential remediation step is to rehash the
    structure, reseting the deleted locations
    - rehashing O(N)
        - N items w/ reasonable fill pct.
        
## LINEAR PROBING
Collision-Resolution Policy adds a constant number to
each location to generate a probe sequence. 

STRIDE
- the constant number mentioned above (usually set to 1)

- each time the algo adds 1, it takes  the 
(location mod array_size) so that the probe sequence wraps
around to the start of the array if necessary.

PRO
- very simple
- is guaranteed to visit every location in the array
    - (guarantees no dead space)
    
CON
- PRIMARY CLUSTERING
    - this is the effect of having items added to the HashTable
    clump together (i.e. large contiguous blocks of 
    elements strung together that are full!)
    - leads to LONG probe sequences => poor performance
    - larger cluster ==> greater probability that a new
    item will be added to the cluster

    
## QUADRATIC PROBING
an approach to resolving primary clustering that is caused by
linear probes

- instead of using a CONSTANT STRIDE, it adds the square of
the number of locations it has tried to create the probe
sequence.
    
        EX
            LINEAR PROBE = 1 2 3 4...
            QUADRATIC PROBE = 1 4 9 16...
            
            (NOTE: assume that N is > 16, or we're binding it
            to the structure w/ an (N mod size) op.
            
PRO
- solves primary clustering

CON
- SECONDARY CLUSTERING
    - this is when values that map to the same initial position, follow the same probe sequence, resulting
    in a cluster
        - even though it is 'spread out' throughout the array, since it reflects the stepwise progression
        of the probe sequence, it results in extending those probe sequences (resulting in poor performance)
- since the probe sequence "leaps" through the array, it is more likely for it to create a sequence that results 
in dead space.

## PSEUDORANDOM PROBING
Instead of constant or squared STRIDE, it is a pseudorandom function of the initially mapped location. 

    EX
        if value initially maps to X, then sequence is :
            
            X, X + p, X + 2 * p, X + 3 * p
            
            p is determined by pseudorandom function.
            
PRO
- prevents primary clustering

CON
- still subject to secondary clustering
- also subject to dead space (i.e. probe sequence repeats w/o visiting all of the elements)

## DOUBLE HASHING
Attempts to resolve secondary clustering by making values that map to the same location
follow different PROBE SEQUENCES
- similar to PSEUDORANDOM PROBING. Instead of a using a PR function of the initial location, it uses
a second hashing function to map the original value to a stride. 


    EX:
        uses pseudorandom hash function F2 to map original values
        
            A and B to 2 different strides:
            
                pA = F2(A), pB = F2(B)
                
            They both start at same value K (different after that)
        
PRO
- eliminates primary and secondary clustering

CON
- still subject to dead space problem. 

## ORDERED HASHING
NOTE: in some (many) applications, values are hashed once and then retrieved many times. 
- EX (Dictionary, lookup tables, addressbooks etc. )
- more important to find/search than to insert.

NOTE: a Chained Hash Table is more likely to find values quickly if the linked lists are sorted. 
- it stops searching when it finds something larger than what it is searching.

- the values don't have to be in "strict" increasing order... they just have to be ordered in a fashion that
ensures that the probe sequence will visit them in increasing orde.r 
