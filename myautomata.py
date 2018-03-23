import automata
import bisect
import random
import json


class Matcher(object):
    def __init__(self, l):
        self.l = l
        self.probes = 0

    def __call__(self, w):
        self.probes += 1
        pos = bisect.bisect_left(self.l, w)
        if pos < len(self.l):
            return self.l[pos]
        else:
            return None


f = open('known.json')
known = json.loads(f.read())

words = [x.strip().lower() for x in open('wordsEn.txt')]
m = Matcher(words)

results = []
for k,v in known.iteritems():
    results.append(list(automata.find_all_matches(k,v,m)))

numresults = len(results)

common_set = set(results[0])
 
for i in range(numresults):
    common_set.intersection_update(set(results[i]))

print sorted(common_set)
print len(common_set)
