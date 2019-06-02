'''
Created on 2 juin 2019

@author: Hugues
'''
import requests
import json
import os

from tpproducts import TPProduct


class EbayProducts(TPProduct):
    
    def response(self,product,shipping_costs):
        
        response  = []
        
        item = product['Item']
            
        product_cost = {}
        shipping_cost = {}
            
        #try :               
        #product cost
        product_cost['currency']    = item['ConvertedCurrentPrice']['CurrencyID']
        product_cost['value']       = item['ConvertedCurrentPrice']['Value']
        
        
        resp = self.constructProductResponse(
            gallery_url=item['PictureURL'], 
            product_name=item['Title'], 
            product_cost=product_cost, 
            shipping_cost=shipping_costs, 
            seller_link=item['ViewItemURLForNaturalSearch'], 
            description=item['ConditionID'],
            seller='EBAY',
            country=item['Country'])
        
        response.append(resp)
        #except:
        #    pass
        
        return response
    
    
    def getProductShippingCost(self,itemId):   
                
        payload={
            'callname'                 : 'GetShippingCosts',
            'responseencoding'         : 'JSON',
            'appid'                    : os.environ['EBAY_APP_NAME'],
            'version'                  : '517',
            'ItemId'                   : str(itemId),
            'siteid'                   : '23',
            'DestinationCountryCode'   : 'BE',
            'DestinationPostalCode'    : '1081',
            'IncludeDetails'           : 'true',
            'QuantitySold'             : '1'
            }
        
        response = requests.get('http://open.api.ebay.com/shopping',params=payload)

        return json.loads(response.text)
    
    
    def getEbayProductFromId(self,itemId):
        
        payload={
            'callname'                 : 'GetSingleItem',
            'responseencoding'         : 'JSON',
            'appid'                    : os.environ['EBAY_APP_NAME'],
            'version'                  : '967',
            'ItemId'                   : str(itemId),
            'siteid'                   : '23'
            }
        
        product = requests.get('http://open.api.ebay.com/shopping',params=payload)
        
        shipping_costs = self.getProductShippingCost(itemId)

        return self.response(json.loads(product.text),shipping_costs['ShippingDetails'])

    
    

if __name__== "__main__":
    
    ebay     = EbayProducts()
    
    product = ebay.getEbayProductFromId(192138766975)

    
    print(json.dumps(product,indent=2))
    


    
    
