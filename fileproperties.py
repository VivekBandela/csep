import os
stat=os.stat('r170322.txt')
print(stat.st_size)
import time
print(time.ctime(stat.st_atime))
print(time.ctime(stat.st_mtime))
