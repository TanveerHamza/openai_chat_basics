products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            ...
            "Fast wireless charging"
        ]
    },
    ...
]
# Combine the features for last_product and each product in products
last_product_text = [create_product_text(product) for product in products]
product_texts = create_product_text(last_product)

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
product_embeddings = create_embeddings(product_texts)[0]

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings, n=3)

for hit in hits:
  product = products[hit['index']]
  print(product['title'])

# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(product)  for product in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embeddings = np.mean(history_embeddings, axis = 0)

# Filter products to remove any in user_history
products_filtered = [product for product in products if product not in user_history]
# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
  product = products_filtered[hit['index']]
  print(product['title'])