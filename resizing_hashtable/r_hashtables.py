

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
        self.storage = [None] * capacity


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
    if hash_table[index] != None:
        # If key is equal to the index's linkedPair key
        if key == hash_table[index].key:
            # replace index's value with new value
            hash_table[index].value = value
        # Else, handle collision
        else:
            # current_linked_pair is equal to pair at index
            current_linked_pair = hash_table[index]
            # While current_linked_pair.next is not equal to None:
            while current_linked_pair.next != None:
                # current_linked_pair is equal to current_linked_pair.next
                current_linked_pair = current_linked_pair.next
            # Create LinkedPair with key, value arguments
            new_linked_pair = LinkedPair(key, value)
            # current_linked_pair.next is equal to new_linked_pair
            current_linked_pair.next = new_linked_pair
    
    # Else, insert linkedPair at appropriate index
    else:
        # Create LinkedPair with key, value arguments
        new_linked_pair = LinkedPair(key, value)
        hash_table[index] = new_linked_pair


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
    if hash_table[index] != None
        # If node key is equal to key
        if hash_table[index].key == key:
            # hash_table[index] is now equal to node.next
            hash_table[index] = hash_table[index].next
            # Return
            return
        # Check to see if the index contains a linked list
        # If linked list
        if hash_table[index].next != None:
            # Iterate over node.next
            current_linked_pair = hash_table[index]
            while current_linked_pair != None:
                # If node key is equal to key
                if current_linked_pair.next.key == key:
                    # Patch up linked list by making node.next = node.next.next
                    current_linked_pair.next = current_linked_pair.next.next
                    # Return
                    return
    # Else
    else:
        # Print a warning
        print(f"{key} not found in hash table, cannot be removed.")

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


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


Testing()
