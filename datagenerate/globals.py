import typesense, random
from faker import Faker
fake = Faker('en_US')

class GLOBALS :
    
    # Authentication with Typesense    
    def typesenceAuth(self):
        client = typesense.Client({
            'nodes': [{
                'host': 'localhost',  # For Typesense Cloud use xxx.a1.typesense.net
                'port': '8108',       # For Typesense Cloud use port no. 443
                'protocol': 'http'    # For Typesense Cloud use https
            }],
            'api_key': 'xyz',
            'connection_timeout_seconds': 2
        })
        return client
        
    # random gender generator   
    def randomGender(self) :
        return random.choice(['M', 'F'])

    # random moble no generator   
    def randomMobileNo(self) :
        return str(random.randint(1000000000, 9999999999))

    # random address generator   
    def randomAddress(self) :
        return fake.address()[0:10]

    # random name generator   
    def randomName(self) :
        return fake.name()[0:10]
    
    
    # session settings
    def setSession(self, request, options) :
        return request.session[{'user_details': options}]
    
    def sessionDestroy(self, request) :
        request.session.flush()
        request.session.clear()
        request.session.close()
        request.session.clear_expired()
        return True
 
    def test(self) :
        return 'dry rtrn'
 