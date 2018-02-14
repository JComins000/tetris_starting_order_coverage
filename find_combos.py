"""
<playfield>
  gg
   g
gg g
g  gg
g   g
gg gg
gg gg  z
s jjllzzt
ssjoolzttt
 sjooliiii
----------
  gg
   g
gg g
g  gg
g   g
gg gg
gg ggi   t
s jjgil tt
ssjooilzzt
 sjooillzz
----------
  gg
   g
gg g
g  gg
g   g
gg gg
gg gg   ti
s jjgl tti
ssjoolzzti
 sjoollzzi
----------
  gg
   g
gg g
g  gg
g   g
gg gg
gg gg    l
s jjz tlll
ssjzztttoo
 sjziiiioo
----------
  gg
   g
gg g
g  gg
g   g
gg gg
gg gg    z
s jjt oozz
ssjtttoozl
 sjiiiilll
----------
  gg
   g
gg g
g  gg
g   g
gg gg i
gg gg i  t
s oo  i tt
ssooljizzt
 sllljjjzz
</playfield>
  gg
   g
gg g
g  gg
g   g
gg ggl
gg ggl   t
s ggjll tt
ssoojjjzzt
 sooiiiizz
----------
</playfield>

1. i must come before z

2a. l must come before z or i
2b. o must come before either j or i

3a. o must come before j
3b. l must come before either o or j

4a. o must come before l
4b. z must come before either j or i
4c. i must come before either z or l

5a. i must come before o
5b. j must come before z

6a. j must come before i
6b. o must come before l 

7a. i must come before j
7b. j must come before l
7c. i must come before either z or o
"""

from itertools import permutations

def check(bag):
	flip = ''
	can_form_t_single = set()

	i_pos = bag.index('i')
	s_pos = bag.index('s')
	z_pos = bag.index('z')
	j_pos = bag.index('j')
	l_pos = bag.index('l')
	o_pos = bag.index('o')
	def c1():
		if i_pos < z_pos:
			can_form_t_single.add('1'+flip)
	def c2():
		if l_pos < max(z_pos, i_pos):
			if o_pos < max(j_pos, i_pos):
				can_form_t_single.add('2'+flip)
	def c3():
		if o_pos < j_pos:
			if l_pos < max(o_pos, z_pos):
				can_form_t_single.add('3'+flip)
	def c4():
		if o_pos < l_pos:
			if z_pos < max(j_pos, i_pos):
				if i_pos < max(z_pos, l_pos):
					can_form_t_single.add('4'+flip)
	def c5():
		if i_pos < o_pos:
			if j_pos < z_pos:
				can_form_t_single.add('5'+flip)
	def c6():
		if j_pos < i_pos:
			if l_pos < o_pos:
				can_form_t_single.add('6'+flip)
	def c7():
		if i_pos < j_pos:
			if j_pos < l_pos:
				if i_pos < max(z_pos, o_pos):
					can_form_t_single.add('7'+flip)
	
	check_fns = c1, c2, c3, c4, c5, c6, c7
	[fn() for fn in check_fns]
	flip = 'f'
	z_pos, s_pos = s_pos, z_pos
	j_pos, l_pos = l_pos, j_pos
	[fn() for fn in check_fns]
	for i in range(1,len(check_fns)+1):
		if str(i) in can_form_t_single:
			if str(i)+'f' in can_form_t_single:
				can_form_t_single.remove(str(i))
				can_form_t_single.remove(str(i)+'f')
				can_form_t_single.add(str(i)+'e')
	if len(can_form_t_single) == 0:
		print(bag)
	return can_form_t_single

f = open('t_spin_single_options.txt', 'w')
bags = ['t'+''.join(p) for p in permutations('iojlsz')]
for bag in bags:
	scenes = check(bag)
	sorted_scenes = sorted(scenes)
	out_str = (bag+' '+', '.join(sorted_scenes)+'\n')
	f.write(out_str)

f.close()