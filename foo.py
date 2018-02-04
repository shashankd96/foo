#!/usr/bin/python2
import time
x = time.ctime() +" : Script - "+ __file__
print x
f = open(__file__, 'a')
f.write('\n# '+x)
f.close()



# Sat Jun 18 14:26:17 2016 : Script - foo.py
# Sat Jun 18 14:26:21 2016 : Script - foo.py
# Sat Jun 18 14:26:22 2016 : Script - foo.py
# Sat Jun 18 14:26:23 2016 : Script - foo.py

# Sat Jun 18 14:26:34 2016 : Script - foo.py

# Sun Feb  4 18:39:32 2018 : Script - foo.py
