## word cloud

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

words = []
for i in desc:
    if len(i) > 3:
        words.append(i.lower())
    else:
        pass

ex_list = ['google', 'that', 'more', 'kale', 'have', 'with', 'at', 'on', 'the', 'within', 'and', 'you', 'atleast', 'like', 'mentioned', 'below', 'current', 'location', 'role']

uniques = list(set(words))
words_uniques = []

for i in range(len(uniques)):
    if uniques[i] not in ex_list:
        words_uniques.append(uniques[i])

counts = [0] * len(words_uniques)
for i in range(len(words_uniques)):
    for j in range(len(words)):
        if words_uniques[i] == words[j]:
            counts[i] = counts[i] + 1

keys = words_uniques
values = counts

word_cloud_dict = dict(zip(keys, values))
word_cloud_dict = {k: v for k, v in sorted(word_cloud_dict.items(), key=lambda item: item[1], reverse = True)}

word_cloud = dict(list(word_cloud_dict.items())[0:30])

import matplotlib.pyplot as plt
plt.barh(range(len(word_cloud)), word_cloud.values(), color = 'green')
plt.yticks(range(len(word_cloud)), word_cloud.keys())
plt.show()






