import os
import string
import nltk
import pyphen
import re 
import pandas as pd
from urls import urls
#nltk.download('punkt')  # Download the punkt tokenizer data
#nltk.download('words')  # Download the words corpus
# Function to process a single file
def process_file(text_file_path):
    stop_words_folder_path = 'StopWords-20231230T095444Z-001/StopWords/'
    master_dictionary_folder_path = 'MasterDictionary-20231230T095444Z-001/MasterDictionary'
    
    # Read the main text file
    with open(text_file_path, encoding='utf-8') as text_file:
        text = text_file.read()
    
    # Convert to lowercase and remove punctuation
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text into words
    tokenized_words = nltk.word_tokenize(cleaned_text)
    
    # Initialize counters
    positive_count = 0
    negative_count = 0
    
    # Initialize sets to store positive and negative words
    positive_words_set = set()
    negative_words_set = set()
    
    # Read positive words from file
    positive_file_path = os.path.join(master_dictionary_folder_path, 'positive-words.txt')
    with open(positive_file_path, encoding='latin-1') as positive_file:
        positive_words_set.update(positive_file.read().split())
    
    # Read negative words from file
    negative_file_path = os.path.join(master_dictionary_folder_path, 'negative-words.txt')
    with open(negative_file_path, encoding='latin-1') as negative_file:
        negative_words_set.update(negative_file.read().split())
    
    # Initialize an empty set to store all stop words
    all_stop_words = set()
    
    # Iterate over each stop words file in the folder
    for stop_words_file_name in os.listdir(stop_words_folder_path):
        stop_words_file_path = os.path.join(stop_words_folder_path, stop_words_file_name)
    
        # Read stop words from the current file with a different encoding
        with open(stop_words_file_path, encoding='latin-1') as stop_words_file:
            stop_words = stop_words_file.read().split()
    
        # Add the stop words to the set
        all_stop_words.update(stop_words)
    
    # Filter out stop words using a list comprehension
    filtered_words = [word.strip() for word in tokenized_words if word.strip() not in all_stop_words]
    
    # Increment counts based on presence in positive or negative sets
    for word in filtered_words:
        if word in positive_words_set:
            positive_count += 1
        elif word in negative_words_set:
            negative_count += 1
    
    # Calculate total words after cleaning
    total_words_after_cleaning = len(filtered_words)
    #polarity score
    polarity_score = (positive_count - negative_count)/ (( positive_count + negative_count) + 0.000001)
    #subjectivity score
    subjectivity_score = (positive_count + negative_count)/ ((total_words_after_cleaning) + 0.000001)
    
    # Calculate total words after cleaning
    total_words_after_cleaning = len(filtered_words)
    
    # Calculate average sentence length
    sentences = nltk.sent_tokenize(text)
    average_sentence_length = len(tokenized_words) / len(sentences) if len(sentences) > 0 else 0
    
    # Find complex words (words with more than 2 syllables)
    complex_word_count = 0
    
    # Initialize the Pyphen dictionary
    dic = pyphen.Pyphen(lang='en')
    # Check each word for complexity (more than 2 syllables)
    for word in tokenized_words:
        syllable_count = len(dic.positions(word))
        if syllable_count > 2:
            complex_word_count += 1
    
    # Percentage of Complex words 
    percentage_of_complex_words = complex_word_count/len(tokenized_words)
    
    #Fog Index 
    fog_index = 0.4 * ( average_sentence_length+ percentage_of_complex_words)
    
    # Variables for total syllables and total words
    total_syllables = 0
    # Count syllables for each word and update totals
    for word in tokenized_words:
        syllable_count = len(dic.positions(word))
        total_syllables += syllable_count
    
    # Calculate average syllables per word
    average_syllables_per_word = total_syllables / len(tokenized_words)
    
    # Define a regular expression pattern for personal pronouns
    personal_pronoun_pattern = re.compile(r'\b(?:I|we|my|ours|us)\b', flags=re.IGNORECASE)
    # Find matches in the cleaned text
    personal_pronoun_matches = personal_pronoun_pattern.findall(text)
    # Count the occurrences of personal pronouns
    personal_pronoun_count = len(personal_pronoun_matches)
    
    # Calculate the sum of the total number of characters in each word
    total_characters = sum(len(word) for word in tokenized_words)
    average_word_length = total_characters / len(tokenized_words) if len(tokenized_words) > 0 else 0
    
    base_filename = os.path.splitext(os.path.basename(file_path))[0]

    # Find the corresponding URL in the urls.py file based on the base filename
    for index, u in enumerate(urls):
        # Assuming base_filename is in the format 'blackassignXXXX'
        base_filename_suffix = base_filename[-4:]  # Extract the last four characters
        if base_filename_suffix.isdigit():
            file_number = int(base_filename_suffix)
            if 1 <= file_number <= 100:
                url_index = file_number - 1  # Subtract 1 to convert to 0-based index
                url = urls[url_index]
                break
        else:
            # Handle the case where the base_filename does not match the expected format
            url = "Invalid URL"
            break


    return {
        "URL_ID": base_filename,
        "URL": url,
        "Positive Count": positive_count,
        "Negative Count": negative_count,
        "Polarity": polarity_score,
        "Subjectivity Score": subjectivity_score,
        "Average Sentence Length": average_sentence_length,
        "Percentage of Complex Words": percentage_of_complex_words,
        "Fog Index": fog_index,
        "Average Number of Words Per Sentence": average_sentence_length,
        "Complex Words": complex_word_count,
        "Word Count": len(tokenized_words),
        "Average syllables per word": average_syllables_per_word,
        "Personal Pronoun Count": personal_pronoun_count,
        "Average Word Length": average_word_length
    }

# Path to the folder containing text files
folder_path = 'dataset/'

# List to store results for all files
results = []

# Iterate over files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        result = process_file(file_path)
        results.append(result)

# Convert the list of dictionaries to a DataFrame
output_df = pd.DataFrame(results)

# Specify the output file path
output_file_path = 'Excel/output.xlsx'

# Save the DataFrame to an Excel file with automatic column width adjustment
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    output_df.to_excel(writer, index=False, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    for i, col in enumerate(output_df.columns):
        max_len = max(output_df[col].astype(str).apply(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)

# Print a message indicating the file has been saved
print("Output saved to:", output_file_path)
