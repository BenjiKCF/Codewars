string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
import operator


lineup_students = lambda (s): sorted(s.split(), key=lambda x: (len(x), x), reverse=True)

print lineup_students(string)
