import random
import hashlib
def transaction_block_target():
    target_list = []
    random_number_1 = random.randint(100, 200)
    random_number_2 = random.randint(201, 300)
    for i in range(random_number_1, random_number_2):
        string_number = str(i)
        data = string_number.encode('utf-8')
        hash_value = hashlib.sha256(data).hexdigest()
        target_list.append(hash_value)
    return target_list

def proposal_block_target():
    target_list = []
    random_number_1 = random.randint(10000, 15000)
    string = str(random_number_1)
    data = string.encode('utf-8')
    hash_value = hashlib.sha256(data).hexdigest()
    target_list.append(hash_value)
    return target_list