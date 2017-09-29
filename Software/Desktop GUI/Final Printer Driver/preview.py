from braille_paper import *

to_be_printed_file = 'text.txt'
output_file = '.output.txt'
char_to_cell_map_file = 'char_to_cell_mapping.txt'

def to_dict(file):
	d = {}
	with open(file) as f:
		for line in f:
			(key, val) = line.split()
			d[key] = val
	return d

def is_in_dict(dict, char):
	if dict.has_key(char): return True
	else: return False

def test(file):
	new = to_dict(char_to_cell_map_file)
	with open(file) as f:
		with open(output_file, 'w') as opf:
			while True:
				ch = f.read(1)
				if ch.islower():
					if is_in_dict(new, ch):
						opf.write(ch + ' ' + str(new[ch]) + '\n')
				elif ch.isupper():
					if is_in_dict(new, ch.lower()):
						opf.write('~' + ' ' + str(new['~']) + '\n')
						opf.write(ch + ' ' + str(new[ch.lower()]) + '\n')
				elif ch.isdigit():
					if is_in_dict(new, ch):
						opf.write('^' + ' ' + str(new['^']) + '\n')
						opf.write(ch + ' ' + str(new[ch]) + '\n')
				elif ch.isspace():
					pass
				else:
					if is_in_dict(new, ch):
						opf.write(ch + ' ' + str(new[ch]) + '\n')
				if not ch: break
	main(output_file)
# test(to_be_printed_file)
# main(output_file)
