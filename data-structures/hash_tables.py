def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table))
    hash_table[index].append((key, value))
    
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table))
    for item in hash_table[index]:
        if item[0] == key:
            return item[1]
    return None
  
  
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table))
    for item in hash_table[index]:
        if item[0] == key:
            hash_table[index].remove(item)
            return
    return None
  
  
def hash_table_resize(hash_table):
    new_hash_table = [[] for _ in range(len(hash_table) * 2)]
    for bucket in hash_table:
        for item in bucket:
            hash_table_insert(new_hash_table, item[0], item[1])
    return new_hash_table
  
  
def hash(string, max):
    hash = 0
    for c in string:
        hash += ord(c)
    return hash % max
  
  
hash_table = [[] for _ in range(8)]
hash_table_insert(hash_table, "key-0", "val-0")
hash_table_insert(hash_table, "key-1", "val-1")
hash_table_insert(hash_table, "key-2", "val-2")
hash_table_insert(hash_table, "key-3", "val-3")
hash_table_insert(hash_table, "key-4", "val-4")
hash_table_insert(hash_table, "key-5", "val-5")
hash_table_insert(hash_table, "key-6", "val-6")
hash_table_insert(hash_table, "key-7", "val-7")
hash_table_insert(hash_table, "key-8", "val-8")
hash_table_insert(hash_table, "key-9", "val-9")
hash_table_insert(hash_table, "key-10", "val-10")
hash_table_insert(hash_table, "key-11", "val-11")

print(hash_table)