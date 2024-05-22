class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for i, kv in enumerate(self.table[index]):
            k, v = kv
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, kv in enumerate(self.table[index]):
            k, v = kv
            if k == key:
                del self.table[index][i]
                return True
        return False


hash_table = HashTable(10)

hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

print("Valor asociado a 'apple':", hash_table.search("apple"))  
print("Valor asociado a 'banana':", hash_table.search("banana"))  

hash_table.delete("apple")
print("Valor asociado a 'apple' después de eliminar:", hash_table.search("apple"))  

