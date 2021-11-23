import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database or {'users': []}

    def update(self):
        for user in self.database['users']:
            owed_by = user['owed_by']
            owes = user['owes']
            for debtor in list(owed_by.keys()):
                if debtor in owes:
                    diff = 0
                    if debtor in owes:
                        diff = owes[debtor]
                        del owes[debtor]
                    if debtor in owed_by:
                        diff -= owed_by[debtor]
                        del owed_by[debtor]
                    if diff > 0:
                        owes[debtor] = diff
                    elif diff < 0:
                        owed_by[debtor] = -diff
            user['balance'] = sum(owed_by.values()) - sum(owes.values())

    def get(self, url, payload=None):
        if payload is not None:
            payload = json.loads(payload)
        if url == '/users':
            if payload is None:
                return json.dumps(self.database)
            else:
                return json.dumps({
                    'users': [
                        user for user in self.database['users']
                        if user['name'] in payload['users']
                    ]
                })
        return None

    def post(self, url, payload=None):
        result = None
        if payload is not None:
            payload = json.loads(payload)
        if url == '/add':
            if payload is not None:
                name = payload['user']
                users = self.database['users']
                user = None
                for idx in users:
                    if idx['name'] == name:
                        user = idx
                        break
                if user is None:
                    new_user = {
                        'name': name,
                        'owes': {},
                        'owed_by': {},
                        'balance': 0
                    }
                    users.append(new_user)
                    self.update()
                    result = json.dumps(new_user)
        elif url == '/iou':
            if payload is not None:
                lender_name = payload['lender']
                borrower_name = payload['borrower']
                amount = payload['amount']
                lender = borrower = None
                for user in self.database['users']:
                    if user['name'] == lender_name:
                        lender = user
                    elif user['name'] == borrower_name:
                        borrower = user
                if lender is not None and borrower is not None:
                    lender['owed_by'].setdefault(borrower_name, 0)
                    lender['owed_by'][borrower_name] += amount
                    borrower['owes'].setdefault(lender_name, 0)
                    borrower['owes'][lender_name] += amount
                    self.update()
                    result = self.get(
                        '/users',
                        json.dumps({'users': [lender_name, borrower_name]})
                    )
        return result
