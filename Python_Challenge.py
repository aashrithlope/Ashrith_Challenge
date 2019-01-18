import re

for _ in range(int(input())):
    credit_card = input().strip()
    try:
        assert re.match(r'[456]', credit_card)
        assert re.match(r'(\d{4}-){3}\d{4}$', credit_card) or re.match(r'\d{16}$', credit_card)
        credit_card = re.sub(r'-', '', credit_card)    
        assert not re.search(r'(\d)\1{3,}', credit_card)
    except:
        print('Invalid')
    else:
        print('Valid')