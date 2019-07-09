

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.original_capacity = capacity
        self.storage = [None] * capacity
        # Add count property to help us know when we should increase capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 5381
    for x in string:
        hash = ((( hash << 5) + hash) + ord(x)) & 0xFFFFFFFF
    return hash


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # Get the hashified key
    hash_key = hash(key)
    # Get the index using the hashified key and ht's capacity
    index = hash_key % hash_table.capacity
    # If hash_table[index] != None
    if hash_table.storage[index] != None:
        # If key is equal to the index's linkedPair key
        if key == hash_table.storage[index].key:
            # replace index's value with new value
            hash_table.storage[index].value = value
        # Else, handle collision
        else:
            # current_linked_pair is equal to pair at index
            current_linked_pair = hash_table.storage[index]
            # While current_linked_pair.next is not equal to None:
            while current_linked_pair.next != None:
                # current_linked_pair is equal to current_linked_pair.next
                current_linked_pair = current_linked_pair.next
            # Check if key matches pair key
            if current_linked_pair.key == key:
                # Replace old value with new value
                current_linked_pair.value = value
            # Else
            else:
                # Create LinkedPair with key, value arguments
                new_linked_pair = LinkedPair(key, value)
                    # current_linked_pair.next is equal to new_linked_pair
                current_linked_pair.next = new_linked_pair
    
    # Else, insert linkedPair at appropriate index
    else:
        # Create LinkedPair with key, value arguments
        new_linked_pair = LinkedPair(key, value)
        hash_table.storage[index] = new_linked_pair
    # Increase hash table's count property
    hash_table.count += 1
    # Double size of hash table when it grows past load factor of 0.7
    # Check to see if it has grown to or past the load factor
    if hash_table.count >= hash_table.capacity * 0.7:
        # Double the hash table's capacity
        # Create new capacity, new storage
        new_capacity = hash_table.capacity * 2
        new_storage = [None] * new_capacity
        # Loop through hash table's storage
        for i in range(0, hash_table.capacity):
            # If the element is not None
            if hash_table.storage[i] is not None:
                # Hash key for new index
                index = hash(hash_table.storage[i].key) % new_capacity
                new_storage[index] = hash_table.storage[i]
        hash_table.storage = new_storage
        hash_table.capacity = new_capacity


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # Get hashified key
    hash_key = hash(key)
    # Get index using hashified key and ht's capacity
    index = hash_key % hash_table.capacity
    # if hash_table[index] is not equal to None
    print(index)
    if hash_table.storage[index] != None:
        # If node key is equal to key
        if hash_table.storage[index].key == key:
            # hash_table[index] is now equal to node.next
            hash_table.storage[index] = hash_table.storage[index].next
            # Return
            return
        # Check to see if the index contains a linked list
        # If linked list
        if hash_table.storage[index].next != None:
            # Iterate over node.next
            current_linked_pair = hash_table.storage[index]
            while current_linked_pair != None:
                # If node key is equal to key
                if current_linked_pair.next.key == key:
                    # Patch up linked list by making node.next = node.next.next
                    current_linked_pair.next = current_linked_pair.next.next
                    # Subtract one from count
                    hash_table.count -= 1
                    # Return
                    return
                current_linked_pair = current_linked_pair.next

    # Else
    else:
        # Print a warning
        print(f"{key} not found in hash table, cannot be removed.")
    # If the hashtable has shrunk past a load factor of 0.2 and has been resized past the original size
    if hash_table.count <= hash_table.capacity * 0.2 and hash_table.capacity > hash_table.original_capacity:
        # Halve the capacity
        # Create new capacity, new storage
        new_capacity = hash_table.capacity / 2
        new_storage = [None] * new_capacity
        # Loop through hash table's storage
        for i in range(0, hash_table.capacity):
            # If the element is not None
            if hash_table.storage[i] is not None:
                # Hash key for new index
                index = hash(hash_table.storage[i].key) % new_capacity
                new_storage[index] = hash_table.storage[i]
        hash_table.storage = new_storage
        hash_table.capacity = new_capacity

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # Get hashified key
    hash_key = hash(key)
    # Get index using hashified key and ht's capacity
    index = hash_key % hash_table.capacity
    # if hash_table[index] is not equal to None
    if hash_table.storage[index] != None:
        # If node key is equal to key
        if hash_table.storage[index].key == key:
            # Return index value
            return hash_table.storage[index].value
        # Check to see if the index contains a linked list
        # If linked list
        if hash_table.storage[index].next != None:
            # Iterate over node.next
            current_linked_pair = hash_table.storage[index].next
            while current_linked_pair != None:
                # If node key is equal to key
                if current_linked_pair.key == key:
                    # Return current_linked_pair value
                    return current_linked_pair.value
                current_linked_pair = current_linked_pair.next
    # Else
    else:
        # Print a warning
        print(f"{key} not found in hash table, cannot be removed.")


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    new_hash_table.storage = [None] * new_hash_table.capacity
    for i in range(len(hash_table.storage)):
        new_hash_table.storage[i] = hash_table.storage[i]
        hash_table.storage[i] = None
    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")

#ht = HashTable(2)
#
#print(hash("key-1") % ht.capacity)
#print(hash("key-2") % ht.capacity)
#print(hash("key-3") % ht.capacity)
#print(hash("key-4") % ht.capacity)
#print(hash("key-5") % ht.capacity)
#print(hash("key-6") % ht.capacity)
#print(hash("key-7") % ht.capacity)
#print(hash("key-8") % ht.capacity)
#print(hash("key-9") % ht.capacity)
