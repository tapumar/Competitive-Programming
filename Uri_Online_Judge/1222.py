from sys import stdin
from math import ceil


def minimum_number_pages(story, max_lines, max_char):
	max_char_counter = 0
	pages = 0
	lines = 1
	for s in story.split():
		if len(s) + max_char_counter <= max_char:
			max_char_counter += len(s) + 1
		else:
			max_char_counter = 0
			max_char_counter += len(s) + 1
			lines += 1
	return ceil(lines/max_lines)

while True:
	ln = stdin.readline().split()
	if not ln:
		break 
	n, max_lines, max_char = map(int, ln)
	story = stdin.readline()
	print(minimum_number_pages(story, max_lines, max_char))
