import numpy as np
import pickle


class CBOW:
    def __init__(self, vocab_size, embedding_dim):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        # Initialize weights with small random values
        self.W1 = np.random.randn(vocab_size, embedding_dim) * 0.01
        self.W2 = np.random.randn(embedding_dim, vocab_size) * 0.01

    def forward(self, context_indices):
        # context_indices shape: (context_size,)
        # Compute the average of the input embeddings
        avg_embedding = np.mean(self.W1[context_indices], axis=0)
        # Compute the output layer
        output = np.dot(avg_embedding, self.W2)
        return output

    def train(self, context_indices, target_index, learning_rate=0.01):
        # Forward pass
        output = self.forward(context_indices)
        # Compute softmax probabilities
        exp_output = np.exp(output - np.max(output))
        probs = exp_output / np.sum(exp_output)
        # Compute loss (cross-entropy)
        loss = -np.log(probs[target_index])
        # Compute gradients
        d_output = probs.copy()
        d_output[target_index] -= 1
        d_W2 = np.outer(np.mean(self.W1[context_indices], axis=0), d_output)
        d_embedding = np.dot(d_output, self.W2.T)
        d_W1 = np.zeros_like(self.W1)
        for idx in context_indices:
            d_W1[idx] += d_embedding / len(context_indices)
        # Update weights
        self.W1 -= learning_rate * d_W1
        self.W2 -= learning_rate * d_W2
        return loss

    def save_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_model(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)


# Example usage
if __name__ == '__main__':
    # Sample data: context words and target word indices
    context_indices = np.array([0, 1, 2])  # Example context indices
    target_index = 3  # Example target index
    vocab_size = 10
    embedding_dim = 5
    model = CBOW(vocab_size, embedding_dim)
    loss = model.train(context_indices, target_index)
    print(f"Training loss: {loss}")
    # Save the model
    model.save_model('cbow_model.pkl')
    # Load the model
    loaded_model = CBOW.load_model('cbow_model.pkl')
    print("Model loaded successfully.")
