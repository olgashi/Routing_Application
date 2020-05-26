class HashTable:
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    def insert(self, item):
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(item)

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
