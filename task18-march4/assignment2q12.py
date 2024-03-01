"""12.Write a function that takes a sentence as input and returns a new sentence 
with the words reversed, while keeping the order of the words in the 
sentence.
"""


def reverse_words_in_sentence(sentence):
    """
    Reverse the order of words in a sentence.

    Parameters:
    - sentence (str): The input sentence.

    Returns:
    - str: The new sentence with reversed words.
    """
    return " ".join(sentence.split()[::-1])


# Example usage:
input_sentence = input("enter a string: ")
result_sentence = reverse_words_in_sentence(input_sentence)
print(f"Original Sentence: {input_sentence}")
print(f"Reversed Sentence: {result_sentence}")
