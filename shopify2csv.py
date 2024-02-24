import csv
import requests

# Your Shopify API credentials and store URL
API_KEY = 'your_api_key'
PASSWORD = 'your_api_password'
STORE_NAME = 'your_store_name.myshopify.com'

# The endpoint to fetch products from your Shopify store
ENDPOINT = f'https://{API_KEY}:{PASSWORD}@{STORE_NAME}/admin/api/2023-01/products.json'

# Function to fetch products
def fetch_products():
    response = requests.get(ENDPOINT)
    if response.status_code == 200:
        return response.json()['products']
    else:
        print("Failed to fetch products")
        return []

# Function to write products to a CSV file
def write_products_to_csv(products):
    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Title', 'Body (HTML)', 'Vendor', 'Product Type', 'Tags'])
        
        # Write product data
        for product in products:
            writer.writerow([
                product.get('title', ''),
                product.get('body_html', '').replace('\n', '').replace('\r', ''), # Remove newlines
                product.get('vendor', ''),
                product.get('product_type', ''),
                ", ".join(product.get('tags', []))
            ])

def main():
    products = fetch_products()
    if products:
        write_products_to_csv(products)
        print("Products have been written to products.csv")
    else:
        print("No products to write.")

if __name__ == '__main__':
    main()
