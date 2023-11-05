import json
import hashlib
from block_creation import create_proposal_block
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BlockChains:
    def __init__(self):
        self.head = None
    def add_blocks(self,data):
        new_block = Node(data)
        if self.head is None:
            self.head = new_block
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_block
    def show_blocks(self):
        pointer = self.head
        while pointer.next is not None:
            print(pointer.data, end = "]         --->           [")
            print()
            print()
            pointer = pointer.next
        print(pointer.data)

    def search_transaction(self, target_txn):
        pointer = self.head
        while pointer is not None:
            for block in pointer.data['payload']:
                if block['txn'] == target_txn:
                    return True  
            pointer = pointer.next
        return None 
    
startChain = BlockChains()
startChain.add_blocks(create_proposal_block("Kshitiz"))
startChain.add_blocks(create_proposal_block("Utkarsh"))
startChain.add_blocks(create_proposal_block("Karam"))
startChain.show_blocks()

def check_transaction(u1, u2, amt):
    transaction_data = {"user_id_1":u1,"user_id_2":u2, "amount":amt}
    json_string = json.dumps(transaction_data, sort_keys=True).encode('utf-8')
    transaction_hash = hashlib.sha256(json_string).hexdigest()
    print(startChain.search_transaction(transaction_hash))
    
check_transaction("Kshitiz", "Utkkkkkarsh", 35000)
