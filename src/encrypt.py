import hashlib 

class hash_sha3_256():
    def __init__(self, word:str) -> None:
        self.word = word
        self.hash = hashlib.sha3_256(word)
    
    @property
    def get_hash_bytes(self):
        return self.hash.digest()

    @property
    def get_hash_hex(self):
        return self.hash.hexdigest()

    @property
    def get_size_block(self):
        return self.hash.block_size
