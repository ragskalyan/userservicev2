from dynamo_db_operations.db_ops.core import DynamoDBOps

db = DynamoDBOps(
    table_name='userData'
)

user_data = db.get_item(
    item_key= {
        'emailId': {'S': 'ragskalyan@gmail.com'},
        'mobileNumber': {'N': '9600234875'}
    }
)

print(type(user_data.get('firstName', {}).values()))

if "kalyan" in user_data.get('firstName', {}).values():
    print(True)
else:
    print(False)
