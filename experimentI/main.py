import matplotlib.pyplot as plt

# Function to read a text file and return a list of lines
def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Function to find similarities between two lists
def find_similarities(list1, list2):
    # Find items present in both lists
    similarities = [item for item in list1 if item in list2]
    return similarities

# Function to compare two lists
def compare_lists(list1, list2):
    differences = []

    # Find items in list1 not in list2
    differences.extend([item for item in list1 if item not in list2])

    # Find items in list2 not in list1
    differences.extend([item for item in list2 if item not in list1])

    return differences

# Read the text files
GPT_4_data = read_txt('/Users/aiyufan/Study/2023 Fall/DH 285/dh285-Project/data/1/GPT 4.0.txt')
GPT_3_5_data = read_txt('/Users/aiyufan/Study/2023 Fall/DH 285/dh285-Project/data/1/GPT 3.5.txt')

# Find similarities
similarities = find_similarities(GPT_4_data, GPT_3_5_data)

# Compare the files to find differences
differences = compare_lists(GPT_4_data, GPT_3_5_data)

# Visualization
# Plot the count of unique elements and similar elements in the lists
unique_GPT_4 = len([item for item in GPT_4_data if item not in GPT_3_5_data])
unique_GPT_3_5 = len([item for item in GPT_3_5_data if item not in GPT_4_data])
similar_count = len(similarities)

labels = ['Unique in GPT-4.0', 'Unique in GPT-3.5', 'Similar']
values = [unique_GPT_4, unique_GPT_3_5, similar_count]

colors = ['blue', 'orange', 'green']  # Added green for similarities

plt.bar(labels, values, color=colors)
plt.ylabel('Count of Elements')
plt.title('Comparison between GPT-4.0 and GPT-3.5 Text files')

plt.show()
