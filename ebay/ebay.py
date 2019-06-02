import requests
import json
import os


class EbayProducts(TPProduct):
    
    def constructProductResponse(self,product):
        
        
        response  = []
        
        #print(json.dumps(resp,indent=2))
        
        search_result = product['findItemsByKeywordsResponse'][0]['searchResult'][0]
        
        for item in search_result['item']:
            
            resp         = {}
            product_cost = {}
            selling_cost = {}
              
            resp['gallery_url']         = item['galleryPlusPictureURL']
            resp['product_name']        = item['title'][0]
            
            #product cost
            product_cost['currency']    = item['sellingStatus'][0]['currentPrice'][0]["@currencyId"]
            product_cost['value']       = item['sellingStatus'][0]['currentPrice'][0]["__value__"]
            
            resp['product_cost']        = product_cost
            
            #shipping cost
            selling_cost['currency']    = item['shippingInfo'][0]['shippingServiceCost'][0]["@currencyId"]
            selling_cost['value']       = item['shippingInfo'][0]['shippingServiceCost'][0]["__value__"]
            
            resp['shipping_cost']       = selling_cost
            
            #seller link   
            resp['seller_link']         = item['viewItemURL'][0]
            
            #product description
            resp['description']         = item['condition'][0]['conditionDisplayName']
            
            response.append(resp)
        
        return response
        
    
    
    def getEbayProductFromId(self,productId):
        
        payload={
            'OPERATION-NAME'                 : 'findItemsByKeywords',
            'SERVICE-VERSION'                : '1.0.0',
            'SECURITY-APPNAME'               : os.environ['EBAY_APP_NAME'],
            'RESPONSE-DATA-FORMAT'           : 'JSON',
            'paginationInput.entriesPerPage' : '2',
            'REST-PAYLOAD'                   :'',
            'GLOBAL-ID'                      :'EBAY-FRBE',
            'keywords'                       : str(productId),
            'paginationInput.entriesPerPage' :'2'
            }
        
        response = requests.get('http://svcs.ebay.com/services/search/FindingService/v1',params=payload)

        return json.loads(response.text)

    
    

if __name__== "__main__":
    
    ebay     = TPProducts()
    
    products = ebay.getEbayProduct(192138766975)
    
   
    response = ebay.constructProductResponse(products)
    
    print(json.dumps(response,indent=2))
    


    
    
