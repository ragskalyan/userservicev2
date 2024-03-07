from dynamo_db_operations.db_ops.core import DynamoDBOps
from user_management.users import UserCreation


def main():
    user = UserCreation(
        first_name="Banumathi",
        second_name="Chandramohan",
        email_id="banumathichandramohan1974@gmail.com",
        password="Banu@1974_oo7",
        mobile_number="9543830466"

    )

    user_output = user.to_user()

    print(user_output)

    db = DynamoDBOps(table_name='userData')

    update = db.update_item(item_key={
        'emailId': {'S': user_output['email_id']},
        'mobileNumber': {'N': user_output['mobile_number']}
    },
        attributes_to_update={
            'firstName': user_output['first_name'],
            'secondName': user_output['second_name'],
            'password': user_output['password']
        })

    print(update)


if __name__ == "__main__":
    main()
