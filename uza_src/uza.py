from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
from http import HTTPStatus

from parameters.global_parameters import SELLERS
from ebay.ebay import EbayProducts


app = Flask(__name__)
api = Api(app)


class Product(Resource):
    
    def error_handler(self, code, message):
        
        ret = jsonify({
            'message': message,
            })
        
        ret.status_code = code
        
        return ret
        
    def get(self):
        
        productId = request.args.get('productId')        
        seller = request.args.get('seller')
        
        # Query parameters validation
        if productId is None : 
            return self.error_handler(HTTPStatus.EXPECTATION_FAILED, 'productId parameter is missing')
        
        if seller is None : 
            return self.error_handler(HTTPStatus.EXPECTATION_FAILED, 'seller parameter is missing')
        
        if seller.upper() not in SELLERS : 
            return self.error_handler(HTTPStatus.EXPECTATION_FAILED, 'Unknown seller')
        
        #
        
        response = {}
        
        
        if seller.upper() == 'EBAY' :  # EBAY 192138766975
            ebay = EbayProducts()
            response = ebay.getEbayProductFromId(productId)
        
        else : 
            response['productId'] = productId
            response['seller'] = seller

        return jsonify(response)

        
# api.add_resource(Product, '/products/<product_id>') # Route_1
api.add_resource(Product, '/products')  # Route 1

if __name__ == '__main__':
    app.run(port='5002', debug=True)
