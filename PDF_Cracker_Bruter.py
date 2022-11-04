#!/usr/bin/env python3
from datetime import datetime
import pikepdf
from itertools import product
import string
from tqdm import tqdm


ranger = 5
numbers = string.digits
pdffile = 'white_rabbit.pdf'
options = numbers.__len__() ** ranger


def brute(ranger, numbers, pdffile, options):
	y = 0
	x = 0
	start_time = datetime.now()
	for passwd in tqdm((product(numbers, repeat=ranger)), total=options, desc='Passwords tested'):

		try:
			with pikepdf.open(pdffile, password=str(''.join(passwd))) as pdfile:
				pdfile.save('output.pdf')
				with open('found.txt', 'w') as file_out:
					end_time = datetime.now()

					file_out.write(f'Found Password: -->  {("".join(passwd))} \nDuration: {format(end_time - start_time)}')

				exit()


		except pikepdf._qpdf.PasswordError:
			x += 1
			if x == 1000:
				y += 1

				with open('massage.txt', 'w') as file_out:
					end_time = datetime.now()
					file_out.write(f"{str('{0:.2g}'.format((y * x)*100/options))} % done: {str('{0:.2g}'.format(y * x))} of {str('{0:.2g}'.format(options))} cycles! \nDuration: {format(end_time - start_time)} {str(((end_time - start_time) / (y * x)) * options)} \nLast Password = {''.join(passwd)}")
				x = 0

if __name__ == '__main__':
	brute(ranger, numbers, pdffile, options)

