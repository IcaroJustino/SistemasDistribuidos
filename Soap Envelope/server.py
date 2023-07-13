from spyne import Application, rpc, ServiceBase, Array, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json
import requests

base_url = "https://mhw-db.com"

class Monster(ServiceBase):
    @rpc(_returns=Array(Unicode))
    def get_all_monsters(self):
        response = requests.get(f"{base_url}/monsters")
        monsters = response.json()
        return [json.dumps(monster) for monster in monsters]

    @rpc(Unicode, _returns=Unicode)
    def get_monster(self, monster_id):
        response = requests.get(f"{base_url}/monsters/{monster_id}")
        monster = response.json()
        return json.dumps(monster)

class Item(ServiceBase):
    @rpc(_returns=Array(Unicode))
    def get_all_items(self):
        response = requests.get(f"{base_url}/items")
        items = response.json()
        return [json.dumps(item) for item in items]

    @rpc(Unicode, _returns=Unicode)
    def get_item(self, item_id):
        response = requests.get(f"{base_url}/items/{item_id}")
        item = response.json()
        return json.dumps(item)

soap_app = Application([Monster, Item],
                       tns="soap.server",
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

application = WsgiApplication(soap_app)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)  # porta onde o servidor estara ouvindo 
    server.serve_forever()
