import hashlib
import json
import random
from Puzzle import transaction_block_target, proposal_block_target
def create_transaction_block(user_id_1, user_id_2, amount):
    transaction_data = {"user_id_1":user_id_1,"user_id_2":user_id_2, "amount":amount}
    json_string = json.dumps(transaction_data, sort_keys=True).encode('utf-8')
    transaction_hash = hashlib.sha256(json_string).hexdigest()
    target_list = transaction_block_target()
    nonce = 0
    for i in range(0, 1000):
        string = str(i)
        data = string.encode('utf-8')
        find_val = hashlib.sha256(data).hexdigest()
        if find_val in target_list:
            nonce = i
            break
        i = i+1
    block_data = {"tranx":transaction_hash, "nonce":nonce}
    json_data = json.dumps(block_data, sort_keys=True).encode('utf-8')
    block_hash = hashlib.sha256(json_data).hexdigest()

    transaction = {"txn":transaction_hash, "b_hash":block_hash}
    return transaction


def get_transaction_block(val):
    transaction_block_list = []
    transaction_block_list.append(create_transaction_block("Kshitiz", "Utkarsh", 35000))
    val = int(val/3000)
    counter = 1
    while counter is not val:
        user_id_1 = f"user_id_{random.randint(1, 100)}"
        user_id_2 = f"user_id_{random.randint(1, 100)}"
        amount = random.randint(1, 10000)
        block = create_transaction_block(user_id_1, user_id_2, amount)
        transaction_block_list.append(block)

        counter = counter + 1

    return transaction_block_list

    
def create_proposal_block(name):
    target_value = proposal_block_target()
    nonce = 0
    for i in range(0, 100000):
        string = str(i)
        data = string.encode('utf-8')
        find_val = hashlib.sha256(data).hexdigest()
        if find_val in target_value:
            nonce = i
            break
        i = i+1
    blocks = get_transaction_block(nonce)
    prop_data = {"name":name, "nonce":nonce}
    json_data = json.dumps(prop_data, sort_keys=True).encode('utf-8')
    prop_hash = hashlib.sha256(json_data).hexdigest()

    proposals = {"p_hash":prop_hash, "payload":blocks}

    return proposals

