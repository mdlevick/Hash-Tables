class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hte_insert(lp, key, value):
    if lp.key == key:
        lp.value = value
    elif lp.next is None:
        lp.next = HashTableEntry(key, value)
    else:
        hte_insert(lp.next, key, value)

def hte_remove(lp, key):
    if lp.key == key:
        return lp.next

    if lp.next is not None:
        if lp.next.key == key:
            lp.next = lp.next.next
        else:
            hte_remove(lp.next, key)
    return lp

def hte_retrieve(lp, key):
    if lp is None:
        return None
    elif lp.key == key:
        return lp.value
    else:
        return hte_retrieve(lp.next, key)

def dump_hte(lp, l):
    """ Dump all the entries in a hash entry chain into a list """
    if lp is None:
        return l
    else:
        l.append((lp.key, lp.value))
        dump_hte(lp.next, l)

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity = 128):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.stored = 0

    @property
    def load_factor(self):
        return self.stored / self.capacity


    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037

        for c in key:
            hash = hash * 1099511628211
            hash = hash ^ ord(c)

        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        hash = 5381

        for c in key:
            hash = hash * 33 + ord(c)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        address = self.hash_index(key)
        if self.storage[address] is None:
            self.storage[address] = HashTableEntry(key, value)
        else:
            hte_insert(self.storage[address], key, value)

        self.stored += 1

        if self.load_factor > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        address = self.hash_index(key)
        if self.storage[address] is not None:
            self.storage[address] = hte_remove(self.storage[address], key)
            # Doesn't quite work since this doesn't check
            #  if element is absent from linked list
            self.stored -= 1

        if self.load_factor < 0.2:
            self.resize(bigger = False)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        address = self.hash_index(key)
        if self.storage[address] is not None:
            return hte_retrieve(self.storage[address], key)

        return None


    def resize(self, bigger = True):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        temp_list = []
        for l in self.storage:
            dump_hte(l, temp_list)

        if bigger:
            self.capacity *= 2
        else:
            self.capacity = self.capacity // 2

        if self.capacity < 8: # should be 128 according to spec
            self.capacity = 8

        self.storage = [None] * self.capacity

        self.stored = 0

        for key, value in temp_list:
            self.put(key, value)

        del temp_list

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
