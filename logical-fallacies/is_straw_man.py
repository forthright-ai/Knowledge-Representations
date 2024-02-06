def is_straw_man(original_claim, distorted_claim, attack_on_distorted, conclusion, vectorize, cosine_similarity, similarity_threshold=0.7):
    original_vector = vectorize(original_claim)
    distorted_vector = vectorize(distorted_claim)
    attack_vector = vectorize(attack_on_distorted)

    # Calculate semantic similarity
    original_distorted_similarity = cosine_similarity(original_vector, distorted_vector)
    distorted_attack_similarity = cosine_similarity(distorted_vector, attack_vector)

    # Check conditions
    is_distorted = original_distorted_similarity < similarity_threshold
    is_attack_on_distorted = distorted_attack_similarity > similarity_threshold
    is_conclusion_false = conclusion == f"{original_claim} is false"

    return is_distorted and is_attack_on_distorted and is_conclusion_false

 
# Example usage
original = "We should reduce military funding to increase education funding."
distorted = "He wants to leave our country defenseless."
attack = "Leaving the country defenseless is dangerous."
conclusion = "We should reduce military funding to increase education funding. is false"

print(is_straw_man(original, distorted, attack, conclusion, example_vectorize, example_cosine_similarity))
