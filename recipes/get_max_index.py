def get_next_index(a):
	if max(a) == 4:
		return 0
	else:
		return max(a) + 1


a = [0, 1, 2, 3, 4]

print(get_next_index(a))

time1 = "2022-05-10 20:51:23"
time2 = "2022-05-10 21:03:03"

import time

t_time1 = time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S"))
t_time2 = time.mktime(time.strptime(time2, "%Y-%m-%d %H:%M:%S"))
print(t_time1, t_time2)

data = {"000": 123, "001": 1234}
data.pop("000")
print(data)
