import json
import hashlib

def hash_request(data):
    #first convert data to dictionary:
    #data_dict=data.dict()
    data_dict=data.model_dump()
    #second convert data_dict to consistent json string:
    data_json_string=json.dumps(data_dict,sort_keys=True)
    #hash it:
    data_hashed=hashlib.sha256(data_json_string.encode()).hexdigest()
    return data_hashed
    

