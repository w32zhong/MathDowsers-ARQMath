def extract_keywords(file):
    keywords = set()
    with open(file, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            fields = line.split()
            if fields[0] == '#':
                continue
            kw = fields[1]
            keywords.add(kw)
    return keywords
 
math_keywords = set()
math_keywords = math_keywords.union(extract_keywords('ARQMath/prepro_2021/MSE_tag_keywords.txt'))
math_keywords = math_keywords.union(extract_keywords('ARQMath/prepro_2021/wiki_keywords.txt'))
print(math_keywords)

import pickle
with open('math_keywords.pkl', 'wb') as fh:
	pickle.dump(math_keywords, fh)
