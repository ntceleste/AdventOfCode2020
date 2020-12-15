import os

day = 15

dir = 'Day{}'.format(day)

try:
    os.mkdir(dir)
except:
    print('{} already exists'.format(dir))

open('{}/challenge.txt'.format(dir), 'w').close()
open('{}/practice.txt'.format(dir), 'w').close()
open('{}/input.txt'.format(dir), 'w').close()
open('{}/day{}-1.py'.format(dir, day), 'w').close()
open('{}/day{}-2.py'.format(dir, day), 'w').close()

