Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> print(time.localtime())
time.struct_time(tm_year=2019, tm_mon=5, tm_mday=10, tm_hour=7, tm_min=40, tm_sec=47, tm_wday=4, tm_yday=130, tm_isdst=0)
>>> t=time.localtime()
>>> t[0]
2019
>>> print(month)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(month)
NameError: name 'month' is not defined
>>> for x in range(1,61):
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
>>> for x in range(1,61):
	print(x)
	time.sleep(1)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
>>> print(time.localtime())
time.struct_time(tm_year=2019, tm_mon=5, tm_mday=10, tm_hour=7, tm_min=47, tm_sec=7, tm_wday=4, tm_yday=130, tm_isdst=0)
>>> hora=t[3]
>>> hora
7
>>> minuto=t[4]
>>> segundos=t[5]
>>> import time, os
>>> while true:
	t=time.localtime()
	os.system("cls")
	print(str(t[3]+":"+str(t[4])+":"+str(t[5])
	time.sleep(1)
		  
SyntaxError: invalid syntax
>>> while true:
	t=time.localtime()
	os.system("cls")
	print(str(t[3]+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)
	      
SyntaxError: invalid syntax
>>> while True:
	t=time.localtime()
	os.system("cls")
	print(str(t[3]+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)
	      
SyntaxError: invalid syntax
>>> while True:
	t=time.localtime()
	os.system("cls")
	print(str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)

	      
0
7:57:1
0
7:57:2
0
7:57:3
0
7:57:4
0
7:57:5
0
7:57:6
0
7:57:7
0
7:57:8
0
7:57:9
0
7:57:10
Traceback (most recent call last):
  File "<pyshell#29>", line 5, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> while True:
	t=time.localtime()
	os.system("clear")
	print(str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)

	      
1
7:58:22
1
7:58:23
1
7:58:24
1
7:58:25
1
7:58:26
1
7:58:27
1
7:58:28
1
7:58:29
1
7:58:30
1
7:58:31
Traceback (most recent call last):
  File "<pyshell#31>", line 5, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> 
