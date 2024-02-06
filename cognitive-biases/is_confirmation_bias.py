def is_confirmation_bias(hypothesis, all_data, selected_data, vectorize, cosine_similarity, similarity_threshold=0.7):
    hypothesis_vector = vectorize(hypothesis)

    # Vectorize all data and selected data
    all_data_vectors = [vectorize(data) for data in all_data]
    selected_data_vectors = [vectorize(data) for data in selected_data]

    # Calculate average similarity of all data and selected data to the hypothesis
    all_data_similarity = sum(cosine_similarity(hypothesis_vector, data_vec) for data_vec in all_data_vectors) / len(all_data_vectors)
    selected_data_similarity = sum(cosine_similarity(hypothesis_vector, data_vec) for data_vec in selected_data_vectors) / len(selected_data_vectors)

    # Check if selected data is significantly more similar to the hypothesis than all data
    return selected_data_similarity > all_data_similarity + similarity_threshold



# Example usage
hypothesis = "Eating chocolate improves cognitive function."
all_data = ["Study 1: No effect", "Study 2: Negative effect", "Study 3: Positive effect"]
selected_data = ["Study 3: Positive effect"]  # Selectively choosing data that confirms the hypothesis

# The vectorize and cosine_similarity functions would need actual implementations
print(is_confirmation_bias(hypothesis, all_data, selected_data, example_vectorize, example_cosine_similarity, 0.2))
