import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("/Users/kshitizsinha/Desktop/Desktop - Kshitiz’s MacBook Pro/WorkingDirectory/Projects/Blockchain-Based-Transactions/BlockChainServer/Server/blockchain-transaction-firebase-adminsdk-3ovuq-ae4fb8dc33.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_users():
    user_list = []
    collection_ref = db.collection("users")
    documents = collection_ref.stream()
    for document in documents:
        user_list.append({"document_id":document.id, "data":document.to_dict()})
    print(user_list)

#get_users()

def get_sercet_key(key):
    message = []
    accounts = []
    collection_ref = db.collection("cred")
    document_ref = collection_ref.document(key)
    documents = collection_ref.stream()
    for document in documents:
        accounts.append(document.id)
    if key not in accounts:
        message.append({"message": "account not there"})
    else:
        document_data =  document_ref.get().to_dict()
        account_value = document_data.get("account")
        message.append({"account": account_value})     
    return message

def get_account_details(account_number):
    info = []
    collection_ref = db.collection("users")
    document_ref = collection_ref.document(account_number)
    document_data = document_ref.get().to_dict()
    name = document_data.get("Name")
    balance = document_data.get("Balance")
    info.append({"name":name, "balance":balance})
    return info
