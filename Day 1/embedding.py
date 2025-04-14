from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "The Statue of Unity is a monumental statue located in Gujarat, India, dedicated to Sardar Vallabhbhai Patel, Standing at 182 meters (597 feet), it is the world's tallest statue and is situated on Sadhu Bet island, facing the Sardar Sarovar Dam. "

embeddings = model.encode(text)
print(embeddings.shape)
print(embeddings)

