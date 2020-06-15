import re
import matplotlib.pyplot as plt
import matplotlib.widgets as widg

book = open('journal-1900.txt', encoding='utf-8')
book_string = book.read()
book.close()

# some wired punctuation characters that you cannot type, you have to copy them
book_string_nopunc = re.sub('[.!?“”,‘’:;]', '', book_string)

# two types of dashes (oh god)
book_string_nopunc = re.sub('[—-]', ' ', book_string_nopunc)

# seems to work
# print(book_string_nopunc)

# now we need to remove all uppercase characters
book_string_nofrills = book_string_nopunc.lower()
# print(book_string_nofrills)

# now we need a list of words from a paragraph
words = book_string_nofrills.split()
words.sort()
# print(words)

words_and_count = {}

for word in words:
    if word in words_and_count:
        words_and_count[word] += 1
    else:
        words_and_count[word] = 1

# graph words with more than threshold
words_and_count_hicount = {}

thresh = 25
for word in words_and_count:
    if words_and_count[word] > 25:
        words_and_count_hicount[word] = words_and_count[word]

print(words_and_count_hicount)

# getting words_x and count_y from words_and_count_hicount
words_x = [word for word in words_and_count_hicount]
count_y = [words_and_count_hicount[word] for word in words_and_count_hicount]

# bar graph time!

# number of words
words_number = len(words_x)
indexes = list(range(words_number))

fig, ax = plt.subplots()

plt.bar(indexes, count_y)
plt.xticks(indexes, words_x)

# make a bar graph that shows 20 words at a time 
# and has a slider which allows horizontal navigation

# [left, bottom, width, height]
slider_ax = plt.axes([0.15, 0.9, 0.5, 0.1])
slider = widg.Slider(slider_ax, 'sector', 0, 1, valinit=0)

ax.set_xlim(-0.5, 20.5)

def sector(val):
    left_edge = (words_number - 21) * slider.val - 0.5
    ax.set_xlim(left_edge, left_edge + 21)

slider.on_changed(sector)

plt.show()