import time
from .block import Block

class Blockchain:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        ## Ensures only one instance of Blockchain is created (Singleton Pattern)
        if cls._instance is None:
            cls._instance = super(Blockchain, cls).__new__(cls)
        return cls._instance

    def __init__(self, difficulty=4):
        if not hasattr(self, 'chain'):
            self.chain = [self.create_genesis_block()]
            self.difficulty = difficulty

    def create_genesis_block(self):
        ## Creates the first block in the chain
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]
    
    def getIndex(self):
        return  len(self.chain)
    
    def add_block(self, new_block):
        ## Adds a mined block to the blockchain """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        ## Validates the blockchain by checking hashes and the previous hash linkage
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash at index", i)
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print("Invalid block linkage at index", i)
                return False

        return True
