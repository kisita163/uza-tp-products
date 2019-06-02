'''
Created on 2 juin 2019

@author: Hugues
'''


class TPProduct():
    
    def constructProductResponse(self,
                                 gallery_url   = '',
                                 product_name  = '' ,
                                 product_cost  = {},
                                 shipping_cost = {},
                                 seller_link   = '',
                                 description   = [],
                                 seller        = '',
                                 country       = '' 
                                    ):
        
        #check input
        
        if not isinstance(product_cost, dict):
            print('Ooups product_cost')
            return None
        
        if not isinstance(shipping_cost, dict):
            print('Ooups shipping_cost')
            return None
        
        if not isinstance(gallery_url,list):
            print('Ooups gallery_url')
            return None
        #
        
        resp         = {}
          
        resp['gallery_url']         = gallery_url
        resp['product_name']        = product_name
        
        #product cost
        resp['product_cost']        = product_cost
        
        #shipping cost
        resp['shipping_cost']       = shipping_cost
        
        #seller link   
        resp['seller_link']         = seller_link
        
        #product description
        resp['description']         = description
        
        #seller
        resp['seller']              = seller
        
        #country
        resp['country']             = country
        
        
        return resp
    
    