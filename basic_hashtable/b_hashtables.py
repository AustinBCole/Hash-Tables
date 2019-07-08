

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 5381
    for x in string:
        hash = ((( hash << 5) + hash) + ord(x)) & 0xFFFFFFFF
    return hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # Get the hash version of key
    key_hash = hash(key)
    # Make a new pair using the key, value pair that was passed into the function
    new_pair = Pair(key, value)
    # Get the index by doing key_hash modulo hash_table.capacity
    index = key_hash % hash_table.capacity
    # If the index already has a pair associated with it, see if the keys match.
    if hash_table.storage[index] != None:
        # If the keys do not match, print a warning and do nothing
        if key == hash_table.storage[index].key:
            print(f"Collision detected for {key} and {hash_table.storage[index].key}")
        # If the keys do match, update the value
        else:
            hash_table.storage[index].value = value
    # Else
    else:
        # insert the pair into the appropriate index
        hash_table.storage[index] = new_pair
# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # Get the hash version of the key
    hash_key = hash(key)
    # Get the index by modulo-ing the key by the ht's capacity
    index = key % hash_table.capacity
    # If there is a value other than None at index
    if hash_table.storage[index] != None:
        # The value is set to None
        hash_table.storage[index] == None
    # Else, print a warning
    else:
        print(f"{key} not found in hash table, cannot be removed.")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass



def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    for pair in ht.storage:
        if pair != None:
            print(pair.key)

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

Testing()
