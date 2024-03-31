## Take a body_of_text.docx as input, and create a histogram of top N words ##

# create a variable to store a list of words in the body of text
import docx
def get_text(filename):
    doc = docx.Document(filename)
    lines = []
    for i in doc.paragraphs:
        lines.append(i.text)
    output = '\n'.join(lines)
    output = output.replace(",", "")
    output = output.replace(".", "")
    return output
desc = get_text('job_desc.docx').split()

# ignore obviously non-significant words, and convert the rest to lower case
words = []
for i in desc:
    if len(i) > 3:
        words.append(i.lower())
    else:
        pass

# create a list of uniques words
uniques = list(set(words))

# create a list of words to exclude from the analysis
ex_list = ['overall', 'this', 'will', 'sure', 'just', 'both', 'gender', 'also', 'while', 'your', "you're", 'google', 'that', 'more', 'kale', 'have', 'with', 'at', 'on', 'the', 'within', 'and', 'you', 'atleast', 'like', 'mentioned', 'below', 'current', 'location', 'role']

# create a blank list to populate later with only significant words
words_uniques = []
for i in range(len(uniques)):
    if uniques[i] not in ex_list:
        words_uniques.append(uniques[i])

# create a loop to count the frequency of each word
counts = [0] * len(words_uniques)
for i in range(len(words_uniques)):
    for j in range(len(words)):
        if words_uniques[i] == words[j]:
            counts[i] = counts[i] + 1

# create a dictionary and sort it so that the most frequent word is at position 1
keys = words_uniques
values = counts
word_cloud_dict = dict(zip(keys, values))
word_cloud_dict = {k: v for k, v in sorted(word_cloud_dict.items(), key=lambda item: item[1], reverse = True)}

# choose the top N keys to include in the histogram
#word_cloud = dict(list(word_cloud_dict.items())[0:50])
word_cloud = dict( (key, value) for (key, value) in word_cloud_dict.items() if value > 1)
print(word_cloud)

# create the histogram
import matplotlib.pyplot as plt
plt.barh(range(len(word_cloud)), word_cloud.values(), color = 'green')
plt.yticks(range(len(word_cloud)), word_cloud.keys())
plt.show()