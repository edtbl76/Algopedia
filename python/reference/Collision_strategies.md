# HashMap Collision Strategies

## Overview

HashMap collision strategies are methods used to handle situations where multiple keys hash to the same index in a hash 
table. Since hash functions can produce the same hash value for different keys (a collision), data structures must
implement strategies to store and retrieve multiple key-value pairs that map to the same bucket.

## Why Collisions Occur

Collisions are inevitable in hash tables due to:
- **Pigeonhole Principle**: With a finite number of buckets and potentially infinite keys, multiple keys must map to the same bucket
- **Hash Function Limitations**: Even well-designed hash functions cannot guarantee unique values for all possible inputs
- **Load Factor**: As the hash table fills up, the probability of collisions increases

## Common Collision Resolution Strategies

### 1. Separate Chaining (Closed Addressing)

In separate chaining, each bucket contains a linked list (or other data structure) of all key-value pairs that hash to that index.

**Characteristics:**
- Each bucket stores multiple entries in a chain
- Simple to implement and understand
- Memory usage grows dynamically
- Good performance when chains are short

**Time Complexity:**
- Average case: O(1) for search, insert, delete
- Worst case: O(n) when all keys hash to the same bucket

**Advantages:**
- Simple implementation
- Handles high load factors well
- Easy deletion of elements
- No clustering issues

**Disadvantages:**
- Extra memory overhead for pointers
- Cache performance may suffer due to pointer chasing
- Performance degrades with long chains

### 2. Open Addressing (Closed Hashing)

Open addressing resolves collisions by finding alternative slots within the hash table itself using a probing sequence.

#### 2.1 Linear Probing

When a collision occurs, linearly search for the next available slot.

**Probe Sequence:** `h(key) + i` where i = 0, 1, 2, ...

**Characteristics:**
- Simple to implement
- Good cache locality
- Suffers from primary clustering

**Primary Clustering:**
- Consecutive occupied slots form clusters
- Larger clusters have higher probability of growing
- Performance degrades as clusters merge

#### 2.2 Quadratic Probing

Uses a quadratic function to determine the next probe position.

**Probe Sequence:** `h(key) + i²` where i = 0, 1, 2, ...

**Characteristics:**
- Reduces primary clustering
- May suffer from secondary clustering
- Not all slots may be reachable

**Secondary Clustering:**
- Keys with the same initial hash value follow the same probe sequence
- Less severe than primary clustering

#### 2.3 Double Hashing

Uses a second hash function to determine the probe step size.

**Probe Sequence:** `h₁(key) + i × h₂(key)` where i = 0, 1, 2, ...

**Characteristics:**
- Eliminates both primary and secondary clustering
- Requires two hash functions
- More complex implementation
- Better distribution of probe sequences

**Requirements for h₂(key):**
- Must never evaluate to 0
- h₂(key) and table size should be relatively prime

### 3. Robin Hood Hashing

A variation of open addressing where elements are moved to minimize the maximum displacement of any element.

**Key Principle:**
- "Rich" elements (close to their ideal position) give way to "poor" elements (far from their ideal position)
- Reduces variance in search times

**Characteristics:**
- Maintains relatively uniform probe distances
- More complex insertion logic
- Better worst-case performance than standard linear probing

### 4. Cuckoo Hashing

Uses two hash tables and two hash functions, guaranteeing O(1) worst-case lookup time.

**Key Principle:**
- Each key can be in one of two possible locations
- If both locations are occupied during insertion, displace existing elements

**Characteristics:**
- Guaranteed O(1) lookup time
- May require rehashing if insertion fails
- Higher memory usage (typically 50% load factor)

## Load Factor and Rehashing

### Load Factor (α)
**Definition:** α = n/m, where n is the number of elements and m is the number of buckets

**Impact:**
- Low load factor: More memory usage, fewer collisions
- High load factor: Better memory utilization, more collisions
- Optimal load factor varies by strategy (typically 0.7-0.8 for chaining, 0.5-0.7 for open addressing)

### Rehashing
When load factor exceeds a threshold:
1. Create a new, larger hash table (typically double the size)
2. Rehash all existing elements into the new table
3. Replace the old table with the new one

**Cost:** O(n) time complexity, but amortized over multiple operations

## Performance Comparison

| Strategy | Average Search | Worst Search | Space Overhead | Cache Performance |
|----------|----------------|--------------|----------------|-------------------|
| Separate Chaining | O(1) | O(n) | High (pointers) | Poor |
| Linear Probing | O(1) | O(n) | Low | Excellent |
| Quadratic Probing | O(1) | O(n) | Low | Good |
| Double Hashing | O(1) | O(n) | Low | Good |
| Robin Hood | O(1) | O(log n) | Low | Excellent |
| Cuckoo Hashing | O(1) | O(1) | High | Good |

## Choosing the Right Strategy

**Use Separate Chaining when:**
- Memory usage is not a primary concern
- High load factors are expected
- Simple implementation is preferred
- Frequent insertions and deletions

**Use Linear Probing when:**
- Cache performance is critical
- Memory usage should be minimized
- Load factors are kept reasonable (< 0.7)

**Use Quadratic Probing when:**
- Moderate improvement over linear probing is needed
- Primary clustering is a concern

**Use Double Hashing when:**
- Best open addressing performance is required
- Both primary and secondary clustering must be avoided

**Use Robin Hood Hashing when:**
- Consistent performance is more important than average performance
- Worst-case scenarios must be minimized

**Use Cuckoo Hashing when:**
- Guaranteed O(1) lookup is required
- Memory usage is not a constraint
- Lookup operations are much more frequent than modifications

## Implementation Considerations

### Hash Function Quality
- A good hash function is crucial regardless of collision strategy
- Poor hash functions can negate the benefits of sophisticated collision resolution
- Consider cryptographic hash functions for security-sensitive applications

### Dynamic Resizing
- Monitor load factor and resize proactively
- Choose appropriate growth factors (common: 2x, prime numbers)
- Consider shrinking when load factor becomes too low

### Deletion Handling
- **Separate Chaining**: Simple removal from chain
- **Open Addressing**: Use tombstones or shifting to maintain probe sequences

### Thread Safety
- Consider concurrent access patterns
- Some strategies are more amenable to concurrent implementations
- Lock-free implementations possible with certain strategies

## Conclusion

The choice of collision resolution strategy significantly impacts hash table performance. While separate chaining offers 
simplicity and handles high load factors well, open addressing strategies can provide better cache performance and memory 
efficiency. Modern implementations often use hybrid approaches or adaptive strategies that change behavior based on runtime 
characteristics.

Understanding these trade-offs allows for informed decisions when implementing or selecting hash table implementations 
for specific use cases.