from collections import Counter
import random
from datetime import datetime

dt = datetime.now()

frase = "franco gabriel di martino el profe de python".split()

print(Counter(frase))

print(random.randrange(20, 50))

print(dt)
print(dt.month)
