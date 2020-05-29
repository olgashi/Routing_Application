class HashTable:
    def __init__(self, size=40):
        self.table = []
        for i in range(size):
            self.table.append([])

    def insert(self, key, package):
        bucket = hash(key) % len(self.table)
        print('Insert Bucket', bucket)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    def search(self, key):
        bucket = hash(key) % len(self.table)
        print('Search bucket', bucket)
        bucket_list = self.table[bucket]
        print('Bucket list', bucket_list[0].package_id)

        if bucket_list[0].package_id == key:
            return bucket_list[0]
        else:
            return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
