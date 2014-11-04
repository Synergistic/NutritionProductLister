#!/usr/bin/env python

import urllib2, json, re

baseUrl = 'http://an-api.abbottnutrition.com/'
            
def GetProductBlocks():
    response = urllib2.urlopen(baseUrl + '/productsfilelist')
    json_productBlocks = json.load(response)
    return json_productBlocks

def GetProducts(productBlock):
    response = urllib2.urlopen('http://an-api.abbottnutrition.com/productsfile/' + productBlock)
    print productBlock
    products = json.load(response)
    return products
  
  
    
targetNutrients = ['Calories', 'Protein, g', 'Fat, g', 'Sodium, mg', 'Carbohydrate, g']
myProduct = {}
productBlocks = GetProductBlocks()
products1 = GetProducts(productBlocks[9])
for product in products1:
    print '\n' + "".join([ c if c.isalpha() else "" for c in product['ProductName']])
    for nutrient in product['Flavors'][0]['ServingSizes'][0]['NutritionalInfo']:
        if nutrient['NutritionName'] in targetNutrients:
            print nutrient['NutritionName'], nutrient['NutritionValue']

        
