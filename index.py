
# import libraries
import csv
import json
import re
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from itertools import zip_longest

result = []
counter = 0

for page in range(1, 3):
    print(page)
    url = f'https://harddiskdirect.com/categories/storage-devices/storage/internal-hard-drives/printer-hard-drive.html?p={page}'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.select('#stores-list-div tr:nth-of-type(1)'))
        #find(attrs={"name": "stainfo"})
    
    
    # selector here
    
    name = soup.select('#stores-list-div .stores-name')  # select all
    post_title = soup.select('.product-item-link')
    #regular_price = soup.select('.price')
    regular_price = soup.select('.old_prices .old-price span:nth-of-type(2)')
    sale_price = soup.select('[data-price-amount] .price')
    product_images = soup.select('.product-image-wrapper img.product-image-photo')
    product_cat = soup.select('.category-description h3')

    for post_title_v, regular_price_v, sale_price_v, product_images_v, product_cat_v in zip_longest(
        post_title, 
        regular_price,
        sale_price,
        product_images,
        product_cat
        ):
        counter += 1
        
        # single hyperlink open action
        post_list = '' if post_title_v == None else post_title_v.get('href'),
        post_content = '',
        post_content_value = ''
        
        #sku
        sku_content = ''
        sku_value = ''
        
        #stock
        stock_content = ''
        stock_value = ''
        
        # product page url
        product_page_url = ''
        
        # meta description
        meta_desc_content = ''
        meta_desc_value = ''
        
        
        # manufacture_1 
        manufacture_content = ''
        manufacture_value = ''
        for post in post_list:
            # condition if not None
            if post != None:
                post_url = post
                post_page = urlopen(post_url)
                post_soup = BeautifulSoup(post_page, 'html.parser')
                post_content = post_soup.select('.product-info-main .product.overview .value')
                sku_content = post_soup.select('.product-info-price .sku .value')
                stock_content = post_soup.select('.product-info-stock-sku .stock span:nth-of-type(2)')
                product_page_url = post_page
                meta_desc_content = post_soup.select('meta[property="og:description"]')
                manufacture_content = post_soup.select('.product-info-stock-sku .attrib-extra span:nth-of-type(2)')
            else:
                post_content = ''
                sku_content = ''
                stock_content = ''
                product_page_url = ''
                meta_desc_content = ''
                manufacture_content = ''
            
            # output below
            for post_content_v, sku_content_v, stock_content_v, meta_desc_content_v, manufacture_content_v in zip_longest(
                post_content, sku_content, stock_content, meta_desc_content, manufacture_content):
                
                post_content_value = post_content_v.text
                sku_value = sku_content_v.text
                stock_value = stock_content_v.text
                meta_desc_value = meta_desc_content_v.get('content')
                manufacture_value = manufacture_content_v.text
                
        
            
        
        
        #print(post_content)
        # #condition
        # print(bool(call_for_price_v))
        #print(post_title_v)
        
        result.append({
            "id": counter,
            "post_title": '' if post_title_v == None else post_title_v.get('title'),
            "post_content": post_content_value,
            "sku": sku_value,
            "stock": stock_value
            
        })

        # result.append({
        #     "post_title": '' if post_title_v == None else post_title_v.get('title'),
        #     "post_name": '' if post_title_v == None else post_title_v.text,
        #     "post_parent": "",
        #     "ID": counter,
        #     "post_content": post_content_value,
        #     "post_excerpt": post_content_value,
        #     "post_status": "publish",
        #     "post_password": "",
        #     "menu_order": 0,
        #     "post_date": "", # in progress
        #     "post_author": 1,
        #     "comment_status": "open",
        #     "sku": sku_value,
        #     "parent_sku": "",
        #     "children": "",
        #     "downloadable": "no",
        #     "virtual": "no",
        #     "stock": stock_value,
        #     "regular_price": '' if regular_price_v == None else regular_price_v.text,
        #     "sale_price": '' if sale_price_v == None else sale_price_v.text,
        #     "weight": "",
        #     "length": "",
        #     "width": "",
        #     "height": "",
        #     "tax_class": "",
        #     "visibility": "",
        #     "stock_status": stock_value,
        #     "backorders": "no",
        #     "sold_individually": "no",
        #     "low_stock_amount": "",
        #     "manage_stock": "yes", #in progress
        #     "tax_status": "taxable",
        #     "upsell_ids": "",
        #     "crosssell_ids": "",
        #     "purchase_note": "",
        #     "sale_price_dates_from": "",
        #     "sale_price_dates_to": "",
        #     "download_limit": "'-1",
        #     "download_expiry": "'-1",
        #     "product_url": '' if post_title_v == None else post_title_v.get('href'), #in progress
        #     "button_text": "",
        #     "images": '' if product_images_v == None else product_images_v.get('src'),
        #     "downloadable_files": "",
        #     "product_page_url": product_page_url,
        #     "meta:total_sales": 0,
        #     "meta:_yoast_wpseo_focuskw": "",
        #     "meta:_yoast_wpseo_canonical": "",
        #     "meta:_yoast_wpseo_bctitle": "",
        #     "meta:_yoast_wpseo_meta-robots-adv": "",
        #     "meta:_yoast_wpseo_is_cornerstone": "",
        #     "meta:_yoast_wpseo_metadesc": meta_desc_value,
        #     "meta:_yoast_wpseo_linkdex": "",
        #     "meta:_yoast_wpseo_estimated-reading-time-minutes": 1,
        #     "meta:_yoast_wpseo_content_score": "90", #in progress
        #     "meta:_yoast_wpseo_title": "",
        #     "meta:_yoast_wpseo_metakeywords": "",
        #     "tax:product_type": "simple",
        #     "tax:product_visibility": "",
        #     "tax:product_cat": "Uncategorized" if product_cat_v == None else product_cat_v.text,
        #     "tax:product_tag": "",
        #     "tax:product_shipping_class": "",
        #     "attribute:pa_manufacture": '' if manufacture_1_v == None else manufacture_1_v.text,
        #     "attribute_data:pa_manufacture": "0|1|0",
        #     "attribute_default:pa_manufacture": ""
        # })

print(json.dumps(result))
file = open('result.json', 'w')
file.write(json.dumps(result))
file.close()
