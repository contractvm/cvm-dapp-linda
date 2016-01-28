from ast import literal_eval

class Core:
	def _match (self, t, q):
		q = q.replace ('(', '').replace (')', '').replace (', ', ',').split (',')
		# Length check
		if len (q) != len (t):
			return False

		i = -1
		for qt in q:
			i += 1

			# Empty string: field existence
			if len (qt) == 0:
				continue

			# Start with %, typematch
			if qt[0] == '%':
				if qt[1] == 'f' and type (t[i]) == float:
					continue
				elif qt[1] == 'd' and type (t[i]) == int:
					continue
				elif qt[1] == 's' and type (t[i]) == str:
					continue
				else:
					return False

			# Value match
			else:
				if type(eval (qt)) == type (t[i]) and eval (qt) == t[i]:
					continue
				else:
					return False

		return True

a = Core ()

assert (a._match (literal_eval ("('hellotupla', 12.0, 'hola', 12)"), "('hellotupla', %f, %s, 12)") == True)
assert (a._match (literal_eval ("('hellotupla', 12, 34)"), "(%s, %d, %d)") == True)
assert (a._match (('ciao',12), '("ciao",)') == True)
assert (a._match (('ciao',12), '("ciao",%d)') == True)
assert (a._match (('ciao',12), '("ciao",%s)') == False)
assert (a._match ((), '("ciao",%s)') == False)
assert (a._match (('ciao',12), '(,)') == True)
assert (a._match ((15.0,12,1,'ci'), '(%f,%d,%d,%s)') == True)


print ('Test done.')
