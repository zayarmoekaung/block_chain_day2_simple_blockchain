import time
from models.block import Block
from models.blockChain import Blockchain
from utils import *

class Main:
    difficulty = 1
    def __init__(self):
        #initialize Main oblect with new block chain
        print("#### Simple BlockChain ####")
        diffadj = getBooleanInput("Do You want to adjust difficulty ? (default = 1 ) :")
        if diffadj:
            self.difficulty = getNumberInput("set your difficulty :")
        print("Initializing BlockChain....\n")
        printLine()
        self.blockchain = Blockchain(self.difficulty)
    
    def start(self):
        #get user input for options
        printLine()
        print("Select Your Option")
        option = getOption(["AddBlock","ValidateChain","PrintBlockChain","Exit"])
        if option == "AddBlock":
            return self.addBlock()     
        if option == "ValidateChain":
            return self.validateChain()
        if option == "PrintBlockChain":
            return self.printChain()
        if option == "Exit":
            return self.exitApp()
    
    def addBlock(self):
        printLine()
        data = getStringInput("Enter Message : ")
        index = self.blockchain.getIndex()
        previous_hash = self.blockchain.get_latest_block().hash
        timeStamp = time.time()
        self.blockchain.add_block(Block(index,previous_hash,timeStamp,data))
        pause()
        return self.start()
    
    def validateChain(self):
        printLine()
         # Validate the blockchain
        print("Is blockchain valid?", self.blockchain.is_chain_valid() )
        pause()
        return self.start()
    
    def printChain(self):
        printLine()
        for block in self.blockchain.chain:
            print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}, Nonce: {block.nonce}\n")
        pause()
        return self.start()        
    
    def exitApp(self):
         print("Closing")
         self.blockchain = None
         exit()
         
if __name__ == "__main__":
   Main().start()