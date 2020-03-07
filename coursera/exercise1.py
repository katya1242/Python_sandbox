# Write a function in the cell below that iterates through the words in file_contents,
# removes punctuation, and counts the frequency of each word. Oh, and be sure to make it
# ignore word case, words that do not contain all alphabets and boring words like "and" or "the".
# Then use it in the generate_from_frequencies function to generate your very own word cloud!
# Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud
# via the generate_from_frequencies function.


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    #lowercase_file_contents = file_contents.lower()

    # Removing all punctuation/wild characters from the list elements

    # Create list of words from text
    word_list = file_contents.split()

    for idx in range(0, len(word_list)):
        for p in range(0, len(punctuations)):
            word_list[idx] = word_list[idx].replace(punctuations[p], "")

    # Removing all numbers from the text
    no_numbers_list = []
    for j in word_list:
        if j.isalpha():
            no_numbers_list.append(j)

    # Removing all "uninteresting" words from the list based on existing Uninteresting_words list
    output_list = []
    for item in no_numbers_list:
        if item not in uninteresting_words:
            output_list.append(item)

    return output_list

def generate_from_frequencies(list_with_text):

    res_word_count = {}
    my_list = list_with_text
    print(my_list)

    for word in my_list:
        w = word.lower()
        if word in res_word_count:
            res_word_count[word] += 1
        else:
            res_word_count[word] = 1

    return res_word_count



#print( calculate_frequencies('''!()-[jlnjn  jkjkj kjkjk kj kj kj kj kj k]{};:'\"\,<>./?@#$%^&*_~''') )



print(generate_from_frequencies(calculate_frequencies("""Towardgggg 5 6 8 cab toward ten o’clock that evening my luggage ten ten ten was{5} transferred to a cab,""")))

    # wordcloud
  #  cloud = wordcloud.WordCloud()
  #  cloud.generate_from_frequencies()
  #  return cloud.to_array()
