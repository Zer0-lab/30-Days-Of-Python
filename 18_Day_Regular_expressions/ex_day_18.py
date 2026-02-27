import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

#What is the most frequent word in the following paragraph?

words = re.findall(r'\w+', paragraph)
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

sorted_counts = sorted(((count, word) for word, count in counts.items()), reverse=True)

print(sorted_counts)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."""

numbers = [int(n) for n in re.findall(r'-?\d+', text)]
print("Nombre =", numbers)

maximum = max(numbers)
minimum = min(numbers)
print("Maximum =", maximum, "\nMinimum =", minimum)
distance = max(numbers) - min(numbers)
print("Distance =", distance)

def is_valid_variable(var):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var)

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

sentence = '''%I $am@% a %tea@cher%, &and& 
I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting 
&and& @emp%o@wering peo@ple. ;
I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(re.sub(r'[!$;@#%&,.?]', '', sentence))

#count three most frequent words in the string.

def most_frequent_words(text):
    words = re.findall(r'\w+', text)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    sorted_counts = sorted(((count, word) for word, count in counts.items()), reverse=True)
    return sorted_counts[:3]

print(most_frequent_words(sentence))



