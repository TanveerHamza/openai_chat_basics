# Define a function to combine the relevant features into a single string
def create_product_text(product):
  return f"""Title: {products['title']}
Description: {products['short_description']}
Category: {products['category']}
Features: {','.join(products['features'])}"""

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = create_embeddings(product_texts)

exercise_texts = [create_exercise_text(exercise) for exercise in exercises] 
exercise_embeddings = create_embeddings(exercise_texts)

similarity_scores = calculate_similarity(product_embeddings, exercise_embeddings)
best_match = find_best_match(similarity_scores)
print(f"The best match for {exercises[best_match]['name']} is {products[best_match]['title']}")