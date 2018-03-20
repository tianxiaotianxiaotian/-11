
						
******************************************************************************************
abs()函数    
描述：返回数字的绝对值。    
语法：abs( x )  	参数：x -- 数值表达式，可以是整数，浮点数，复数    
返回值：函数返回 x（数字）的绝对值，如果参数是一个复数，则返回它的大小。
# 案例：
print ("abs(-40) : ", abs(-40))
print ("abs(100.10) : ", abs(100.10))
******************************************************************************************
dict()函数 	 
描述：用于创建一个字典。     
语法：class dict(**kwarg)                    参数：**kwargs -- 关键字。    
	  class dict(mapping, **kwarg)			 参数：mapping -- 元素的容器。
	  class dict(iterable, **kwarg)			 参数：iterable -- 可迭代对象。
返回值：返回一个字典。
# 案例：
dict()                        # 创建空字典
{}
>>> dict(a='a', b='b', t='t')     # 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1} 
>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
******************************************************************************************
help()函数 		
描述：用于查看函数或模块用途的详细说明。  	
语法：help([object])   参数：object -- 对象；
返回值：返回对象帮助信息。
# 案例：
>>>help('sys')             # 查看 sys 模块的帮助
……显示帮助信息……
 
>>>help('str')             # 查看 str 数据类型的帮助
……显示帮助信息……
 
>>>a = [1,2,3]
>>>help(a)                 # 查看列表 list 帮助信息
……显示帮助信息……
 
>>>help(a.append)          # 显示list的append方法的帮助
……显示帮助信息……
***********************************************************************************************
min()函数  	
描述：返回给定参数的最小值，参数可以为序列。   
语法：min( x, y, z, .... )  	参数：x -- 数值表达式    y -- 数值表达式   z -- 数值表达式
返回值：返回给定参数的最小值。
# 案例：
print ("min(80, 100, 1000) : ", min(80, 100, 1000))
print ("min(-20, 100, 400) : ", min(-20, 100, 400))
print ("min(-80, -20, -10) : ", min(-80, -20, -10))
print ("min(0, 100, -400) : ", min(0, 100, -400))
************************************************************************************************
setattr()函数    
描述：setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
语法：setattr(object, name, value)    
参数：object -- 对象   name -- 字符串，对象属性。 value -- 属性值。
返回值：无
# 案例：
class A(object):
    bar = 1

a = A()
getattr(a, 'bar')          # 获取属性 bar 值
1   					   # 结果1
setattr(a, 'bar', 5)       # 设置属性 bar 值
a.bar
5  						   # 结果5
*********************************************************************************************
all()函数
描述：all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
语法：all(iterable)   	参数：iterable -- 元组或列表。
返回值：如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；

		注意：空元组、空列表返回值为True，这里要特别注意。
# 案例：
all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
False
all([0, 1，2, 3])          # 列表list，存在一个为0的元素
False
   
all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
False
all((0, 1，2, 3))          # 元组tuple，存在一个为0的元素
False
   
all([])             # 空列表
True
all(())             # 空元组
True
************************************************************************************************
dir()函数
描述：dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息
语法：dir([object])			参数：object -- 对象、变量、类型
返回值：返回模块的属性列表。
# 案例：
>>>dir()   #  获得当前模块的属性列表
['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
>>> dir([ ])    # 查看列表的方法
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
*************************************************************************************************
hex()函数
描述：用于将10进制整数转换成16进制，以字符串形式表示
语法：hex(x)  参数：x -- 10进制整数
返回值：返回16进制数，以字符串形式表示。
# 案例：
>>>hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
>>> hex(1L)
'0x1L'
>>> hex(12)
'0xc'
>>> type(hex(12))
class 'str'      # 字符串
*************************************************************************************************
next()函数
描述：next() 返回迭代器的下一个项目
语法：next(iterator[, default])  
参数：iterator -- 可迭代对象
	  default -- 可选，用于设置在没有下一个元素时返回该默认值，
	  			 如果不设置，又没有下一个元素则会触发 StopIteration 异常。
返回值：返回对象帮助信息。
# 案例：
'''首先获得Iterator对象:'''
it = iter([1, 2, 3, 4, 5])
'''循环:'''
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
*************************************************************************************************
slice()函数
描述：实现切片对象，主要用在切片操作函数里的参数传递。
语法：class slice(stop)       			
	  class slice(start, stop[, step]) 	
参数：start -- 起始位置     stop -- 结束位置    step -- 间距
返回值：返回一个切片对象。
# 案例：
>>>myslice = slice(5)    # 设置截取5个元素的切片
>>> myslice
slice(None, 5, None)
>>> arr = range(10)
>>> arr
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> arr[myslice]         # 截取 5 个元素
[0, 1, 2, 3, 4]
>>>
***********************************************************************************************88
any()函数    python2.5以上版本可以使用
描述：用于判断给定的可迭代参数 iterable 是否全部为空对象，
	  如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True
语法：any(iterable)     		参数：iterable -- 元组或列表。
返回值：如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
# 案例：
>>>any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
 
>>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
True
 
>>> any([0, '', False])        # 列表list,元素全为0,'',false
False
 
>>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
 
>>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
True
 
>>> any((0, '', False))        # 元组tuple，元素全为0,'',false
False
  
>>> any([]) # 空列表
False
 
>>> any(()) # 空元组
False
***************************************************************************************
divmod()函数   	在 python 2.3 版本之前不允许处理复数。
描述：python divmod() 函数把除数和余数运算结果结合起来，
	  返回一个包含商和余数的元组(a // b, a % b)。
语法：divmod(a, b)   	参数：a: 数字     b: 数字
返回值：无
# 案例：
>>>divmod(7, 2)
(3, 1)
>>> divmod(8, 2)
(4, 0)
>>> divmod(1+2j,1+0.5j)
((1+0j), 1.5j)
***************************************************************************************
id()函数
描述：用于获取对象的内存地址。
语法：id([object])   参数：object -- 对象
返回值：返回对象的内存地址。
# 案例：
>>>a = 'runoob'
>>> id(a)
4531887632
>>> b = 1
>>> id(b)
140588731085608
***************************************************************************************
object()函数 
***************************************************************************************
sorted()函数
描述：对所有可迭代的对象进行排序操作。
sort 与 sorted 区别：
	sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

	list 的 sort 方法返回的是对已经存在的列表进行操作，
	而内建函数 sorted 方法返回的是一个新的 list，
	不是在原来的基础上进行的操作。
语法：sorted(iterable, key=None, reverse=False)
参数：iterable -- 可迭代对象。
	  key -- 主要是用来进行比较的元素，只有一个参数，
	  		 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
	  reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
返回值：返回重新排序的列表。

# 案例：
>>>sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]                    # 默认为升序

你也可以使用 list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些。
>>>a=[5,2,3,1,4]
>>> a.sort()
>>> a
[1,2,3,4,5]

另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。
>>>sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

利用key进行倒序排序
>>>example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> result_list = sorted(example_list, key=lambda x: x*-1)
>>> print(result_list)
[7, 6, 5, 4, 3, 2, 1, 0]
>>>

要进行反向排序，也通过传入第三个参数 reverse=True：
>>>example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> sorted(example_list, reverse=True)
[7, 6, 5, 4, 3, 2, 1, 0]
**************************************************************************************
ascii()函数
描述：ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 
	  但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数
	  使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
语法：ascii(object) 			 参数：object -- 对象。
返回值：返回字符串。
# 案例：
>>> ascii('runoob')
"'runoob'"
****************************************************************************************
enumerate()函数
描述：用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
	  同时列出数据和数据下标，一般用在 for 循环当中。
语法：enumerate(sequence, [start=0])				
参数：sequence -- 一个序列、迭代器或其他支持迭代对象。
	  start -- 下标起始位置。
返回值：返回 enumerate(枚举) 对象。
# 案例：
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>>list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>>list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


普通的 for 循环
>>>i = 0
>>>seq = ['one', 'two', 'three']
>>>for element in seq:
...    print(i, seq[i])
...    i += 1
... 
0 one
1 two
2 three


for 循环使用 enumerate
>>>seq = ['one', 'two', 'three']
>>>for i, element in enumerate(seq):
...    print(i, seq[i])
... 
0 one
1 two
2 three
>>>
************************************************************************************************
input()函数 			python3 里 input() 默认接收到的是 str 类型
描述：Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。

	  Python2.x 中 input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。

	  raw_input() 将所有输入作为字符串看待，返回字符串类型。
	  而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。

	  注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
	  		而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
	 		除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。

语法：input([prompt])   参数：prompt: 提示信息
# 案例：
input() 需要输入 python 表达式
>>>a = input("input:")
input:123                  # 输入整数
>>> type(a)
<type 'int'>               # 整型
>>> a = input("input:")    
input:"runoob"           # 正确，字符串表达式
>>> type(a)
<type 'str'>             # 字符串
>>> a = input("input:")
input:runoob               # 报错，不是表达式
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'runoob' is not defined
<type 'str'>


raw_input() 将所有输入作为字符串看待
>>>a = raw_input("input:")
input:123
>>> type(a)
<type 'str'>              # 字符串
>>> a = raw_input("input:")
input:runoob
>>> type(a)
<type 'str'>              # 字符串
>>>
*********************************************************************************************
oct()函数
描述：将一个整数转换成8进制字符串。
语法：oct(x)   参数：oct(x)
返回值：返回8进制字符串。
# 案例：
>>>oct(10)
'012'
>>> oct(20)
'024'
>>> oct(15)
'017'
>>>
*********************************************************************************************
staticmethod()函数
描述：返回函数的静态方法。
语法：staticmethod(function) 		参数：无
返回值：无
# 案例：
class C(object):
    @staticmethod
    def f():
        print('runoob');
 
C.f();          # 静态方法无需实例化
cobj = C()
cobj.f()        # 也可以实例化后调用
*********************************************************************************************
bin()函数
描述：返回一个整数 int 或者长整数 long int 的二进制表示。
语法：bin(x)   		参数：x -- int 或者 long int 数字
返回值：字符串。
# 案例：
>>>bin(10)
'0b1010'
>>> bin(20)
'0b10100'
*********************************************************************************************
eval()函数
描述：用来执行一个字符串表达式，并返回表达式的值。
语法：eval(expression[, globals[, locals]])   		
参数：expression -- 表达式。
	  globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
	  locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
返回值：返回表达式计算结果。
# 案例：
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> n=81
>>> eval("n + 4")
85
*********************************************************************************************
int()函数
描述：用于将一个字符串或数字转换为整型。
语法：class int(x, base=10)    参数：x -- 字符串或数字。    base -- 进制数，默认十进制。
返回值：返回整型数据
# 案例：
>>>int()               # 不传入参数时，得到结果0
0
>>> int(3)
3
>>> int(3.6)
3
>>> int('12',16)        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
18
>>> int('0xa',16)  
10  
>>> int('10',8)  
8
open() 函数
描述：python open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
语法：open(name[, mode[, buffering]])
参数: name : 一个包含了你要访问的文件名称的字符串值。
	  mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
	  		 这个参数是非强制的，默认文件访问模式为只读(r)。
	  buffering : 如果 buffering 的值被设为 0，就不会有寄存。
	  			  如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，
	  			  表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
不同模式打开的文件列表
	r 		rb 		r+ 		rb+
	w 		wb 		w+ 		wb+
	a 		ab 		a+ 		ab+

file.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)

file.readline() 返回一行

file.readlines([size]) 返回包含size行的列表,size 未指定则返回全部行

for line in f: print line #通过迭代器访问

f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.

f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).

f.seek(偏移量,[起始位置]) 用来移动文件指针.

偏移量:单位:比特,可正可负
起始位置:0-文件头,默认值;1-当前位置;2-文件尾
f.close() 关闭文件

# 案例：
>>>f = open('test.txt')
>>> f.read()
'RUNOOB1\nRUNOOB2\n'
**********************************************************************************************
str() 函数
描述：将对象转化为适于人阅读的形式。
语法：class str(object='')   参数：object -- 对象。
返回值：返回一个对象的string格式
# 案例：
>>>s = 'RUNOOB'
>>> str(s)
'RUNOOB'
>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
>>> str(dict)
"{'google': 'google.com', 'runoob': 'runoob.com'}"
>>>
**********************************************************************************************
bool() 函数     是int的子类
描述：用于将给定参数转换为布尔类型，如果没有参数(0,1)，返回 False。
语法：class bool([x])   参数：x -- 要进行转换的参数。
返回值：返回 Ture 或 False。
# 案例：
>>>bool()
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True
>>> issubclass(bool, int)  # bool 是 int 子类
True
*******************************************************************************************
exec 函数
描述：执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
语法：exec(object[, globals[, locals]])
参数：object：必选参数，表示需要被指定的Python代码。
	  globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
	  locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。
	  		  如果该参数被忽略，那么它将会取与globals相同的值。
返回值：exec 返回值永远为 None
# 案例：
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    
func()
**************************************************************************************************
isinstance() 函数
描述：判断一个对象是否是一个已知的类型，类似 type()。
	isinstance() 与 type() 区别：
		type() 不会认为子类是一种父类类型，不考虑继承关系。
		isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
语法：isinstance(object, classinfo)
参数：object -- 实例对象。
	  classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
返回值：如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
# 案例：
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True

type() 与 isinstance()区别：
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False   不会认为子类是一种父类类型，不考虑继承关系
******************************************************************************************
ord() 函数
描述：是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
	  它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
	  如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
语法：ord(c)   	参数：c -- 字符。
返回值:返回值是对应的十进制整数。
# 案例：
>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99
*****************************************************************************************
sum() 函数 					求和
描述：对系列进行求和计算。
语法：sum(iterable[, start])   
参数：iterable -- 可迭代对象，如列表。
	  start -- 指定相加的参数，如果没有设置这个值，默认为0。
返回值：返回计算结果。
# 案例：
>>>sum([0,1,2])  
3  
>>> sum((2, 3, 4), 1)        # 元组计算总和后再加 1
10
>>> sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
12
****************************************************************************************
bytearray() 函数
描述：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
语法：class bytearray([source[, encoding[, errors]]])
参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
	  如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
	  如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
	  如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
	  如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值：返回新字节数组。
# 案例：
>>>bytearray()
bytearray(b'')
>>> bytearray([1,2,3])
bytearray(b'\x01\x02\x03')
>>> bytearray('runoob', 'utf-8')
bytearray(b'runoob')
>>>
*********************************************************************************************
filter() 函数     过滤
描述：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
	  该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
	  然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
语法：filter(function, iterable)
参数：function -- 判断函数。
	  iterable -- 可迭代对象。
返回值：返回列表。
# 案例：
##过滤出1~100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
 
newlist = filter(is_sqr, range(1, 101))
print(newlist)
*********************************************************************************************
issubclass() 函数      
描述：判断参数 class 是否是类型参数 classinfo 的子类。
语法：issubclass(class, classinfo)
参数：class -- 类。     classinfo -- 类。
返回值：如果 class 是 classinfo 的子类返回 True，否则返回 False。
# 案例：
class A:
    pass
class B(A):
    pass
    
print(issubclass(B,A))    # 返回 True
********************************************************************************************
pow() 函数      	幂
描述：返回 x**y（x的y次方） 的值。
语法：import math  
	  math.pow( x, y )
	  # 内置的 pow() 方法
	  pow(x, y[, z])
参数：x -- 数值表达式。
	  y -- 数值表达式。
	  z -- 数值表达式。
返回值：返回 xy（x的y次方） 的值。
# 案例：
import math   # 导入 math 模块

print ("math.pow(100, 2) : ", math.pow(100, 2))
# 使用内置，查看输出结果区别
print ("pow(100, 2) : ", pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("math.pow(2, 4) : ", math.pow(2, 4))
print ("math.pow(3, 0) : ", math.pow(3, 0))
********************************************************************************************
super() 函数
描述：super() 函数是用于调用父类(超类)的一个方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
	  但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
语法：super(type[, object-or-type])
参数：type -- 类。
	  object-or-type -- 类，一般是 self
Python3.x 和 Python2.x 的一个区别是: 
	Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
# 案例：
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
************************************************************************************************
bytes 函数
描述：返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。
	  它是 bytearray 的不可变版本
语法：class bytes([source[, encoding[, errors]]])
参数：如果 source 为整数，则返回一个长度为 source 的初始化数组；
	  如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
	  如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
	  如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
	  如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值：返回一个新的 bytes 对象。
# 案例：
>>>a = bytes([1,2,3,4])
>>> a
b'\x01\x02\x03\x04'
>>> type(a)
<class 'bytes'>
>>>
>>> a = bytes('hello','ascii')
>>>
>>> a
b'hello'
>>> type(a)
<class 'bytes'>
>>>
************************************************************************************
float() 函数
描述：用于将整数和字符串转换成浮点数。
语法：class float([x])
参数：x -- 整数或字符串
返回值：返回浮点数
案例：>>>float(1)
1.0
>>> float(112)
112.0
>>> float(-123.6)
-123.6
>>> float('123')     # 字符串
123.0
************************************************************************************
iter() 函数      
描述：用来生成迭代器
语法：iter(object[, sentinel])
参数：object -- 支持迭代的集合对象。
	  sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
	  			  此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，
	  			  都会调用 object。
返回值：迭代器对象。
# 案例：
>>>lst = [1, 2, 3]
>>> for i in iter(lst):
...     print(i)
... 
1
2
3
***********************************************************************************
print() 函数
描述：用于打印输出，最常见的一个函数。
语法：print(*objects, sep=' ', end='\n', file=sys.stdout)
参数：objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
	  sep -- 用来间隔多个对象，默认值是一个空格。
	  end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
	  file -- 要写入的文件对象。
返回值：无
# 案例：
Python3 下测试
>>>print(1)  
1  
>>> print("Hello World")  
Hello World  
 
>>> a = 1
>>> b = 'runoob'
>>> print(a,b)
1 runoob
 
>>> print("aaa""bbb")
aaabbb
>>> print("aaa","bbb")
aaa bbb
>>> 
 
>>> print("www","runoob","com",sep=".")  # 设置间隔符
www.runoob.com
*******************************************************************************************
tuple 函数
描述：将列表转换为元组。。
语法：tuple( seq )   		参数：seq -- 要转换为元组的序列。
返回值：返回元组。
# 案例：
>>>list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')
*****************************************************************************************
callable() 函数
描述：用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
	  但如果返回False，调用对象ojbect绝对不会成功。

对于函数, 方法, lambda 函数, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
语法：callable(object)
参数：object -- 对象
返回值：可调用返回 True，否则返回 False
# 案例：
>>>callable(0)
False
>>> callable("runoob")
False
 
>>> def add(a, b):
...     return a + b
... 
>>> callable(add)             # 函数返回 True
True
>>> class A:                  # 类
...     def method(self):
...             return 0
... 
>>> callable(A)               # 类返回 True
True
>>> a = A()
>>> callable(a)               # 没有实现 __call__, 返回 False
False
>>> class B:
...     def __call__(self):
...             return 0
... 
>>> callable(B)
True
>>> b = B()
>>> callable(b)               # 实现 __call__, 返回 True
True
*****************************************************************************************
format 格式化函数
描述：Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

语法：是通过 {} 和 : 来代替以前的 % 。

format 函数可以接受不限个参数，位置可以不按顺序。
*****************************************************************************************
len()方法
描述：返回对象（字符、列表、元组等）长度或项目个数。
语法：len( s )   参数：s -- 对象。
返回值：返回对象长度。
# 案例：
>>>str = "runoob"
>>> len(str)             # 字符串长度
6
>>> l = [1,2,3,4,5]
>>> len(l)               # 列表元素个数
5
*****************************************************************************************
property() 函数
描述：是在新式类中返回属性值。
语法：class property([fget[, fset[, fdel[, doc]]]])
参数：fget -- 获取属性值的函数
	  fset -- 设置属性值的函数
	  fdel -- 删除属性值函数
	  doc -- 属性描述信息
返回值：返回新式类属性。
# 案例：
定义一个可控属性值 x
class C(object):
    def __init__(self):
        self._x = None
 
    def getx(self):
        return self._x
 
    def setx(self, value):
        self._x = value
 
    def delx(self):
        del self._x
 
    x = property(getx, setx, delx, "I'm the 'x' property.")


将 property 函数用作装饰器可以很方便的创建只读属性：

class Parrot(object):
    def __init__(self):
        self._voltage = 100000
 
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


property 的 getter,setter 和 deleter 方法同样可以用作装饰器：

class C(object):
    def __init__(self):
        self._x = None
 
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
 
    @x.setter
    def x(self, value):
        self._x = value
 
    @x.deleter
    def x(self):
        del self._x
*************************************************************************************
type() 函数
描述:如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
语法:class type(name, bases, dict)
参数：name -- 类的名称。
	  bases -- 基类的元组。
	  dict -- 字典，类内定义的命名空间变量。
返回值：一个参数返回对象类型, 三个参数，返回新的类型对象。
# 案例：
# 一个参数实例
>>> type(1)
<type 'int'>
>>> type('runoob')
<type 'str'>
>>> type([2])
<type 'list'>
>>> type({0:'zero'})
<type 'dict'>
>>> x = 1          
>>> type( x ) == int    # 判断类型是否相等
True
 
# 三个参数
>>> class X(object):
...     a = 1
...
>>> X = type('X', (object,), dict(a=1))  # 产生一个新的类型 X
>>> X
<class '__main__.X'>
***************************************************************************************
chr() 函数
描述：用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
语法：chr(i)
参数：i -- 可以是10进制也可以是16进制的形式的数字。
返回值：返回值是当前整数对应的ascii字符。
# 案例：
>>>print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
0 1 a
>>> print chr(48), chr(49), chr(97)         # 十进制
0 1 a
**************************************************************************************
frozenset() 函数
描述：返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
语法：class frozenset([iterable])
参数：iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回值：返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。
# 案例：
>>>a = frozenset(range(10))     # 生成一个新的不可变集合
>>> a
frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = frozenset('runoob') 
>>> b
frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合
>>>
*************************************************************************************
list()方法
描述：用于将元组转换为列表。
语法：list( seq )
参数：list -- 要转换为列表的元组
返回值：返回列表。
# 案例：
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)

str="Hello World"
list2=list(str)
print ("列表元素 : ", list2)
输出结果：
列表元素 :  [123, 'Google', 'Runoob', 'Taobao']
列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
*************************************************************************************
range() 函数用法
描述：Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
	  Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
	  Python2 range() 函数返回的是列表。
语法：range(stop)
	  range(start, stop[, step])
参数：start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
	  stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
	  step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
返回值：无
# 案例：
>>>range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
>>>

>>>range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
>>>
*****************************************************************************************
vars() 函数
描述：返回对象object的属性和属性值的字典对象。
语法：vars([object])
参数：object -- 对象
返回值：返回对象object的属性和属性值的字典对象，
	    如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
# 案例：
>>>print(vars())
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> class Runoob:
...     a = 1
... 
>>> print(vars(Runoob))
{'a': 1, '__module__': '__main__', '__doc__': None}
>>> runoob = Runoob()
>>> print(vars(runoob))
{}
*******************************************************************************************
classmethod 修饰符
描述：classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
	  但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
语法:classmethod
参数：无
返回值：返回函数的类方法。
# 案例：
class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
A.func2()               # 不需要实例化
*************************************************************************************************
getattr() 函数
描述：用于返回一个对象属性值。
语法：getattr(object, name[, default])
参数：object -- 对象。
	  name -- 字符串，对象属性。
	  default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
返回值：返回对象属性值。
# 案例：
>>>class A(object):
...     bar = 1
... 
>>> a = A()
>>> getattr(a, 'bar')        # 获取属性 bar 值
1
>>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
3
>>>
***********************************************************************************************
locals() 函数
描述：locals() 函数会以字典类型返回当前位置的全部局部变量。
	  对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
语法：locals()
参数：无
返回值：返回字典类型的局部变量。
# 案例：
>>>def runoob(arg):    # 两个局部变量：arg、z
...     z = 1
...     print (locals())
... 
>>> runoob(4)
{'z': 1, 'arg': 4}      # 返回一个名字/值对的字典
>>>
**********************************************************************************************
repr() 函数
描述：将对象转化为供解释器读取的形式。
语法：repr(object)
参数：object -- 对象。
返回值：返回一个对象的 string 格式。
# 案例：
>>>s = 'RUNOOB'
>>> repr(s)
"'RUNOOB'"
>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
>>> repr(dict)
"{'google': 'google.com', 'runoob': 'runoob.com'}"
>>>
**********************************************************************************************
zip() 函数
描述：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

	 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
语法：zip([iterable, ...])
参数：iterabl -- 一个或多个迭代器;
返回值：返回元组列表
# 案例：
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
***********************************************************************************************
compile() 函数
描述：将一个字符串编译为字节代码。
语法：compile(source, filename, mode[, flags[, dont_inherit]])
参数：source -- 字符串或者AST（Abstract Syntax Trees）对象。。
	  filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
	  mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
	  flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
	  flags和dont_inherit是用来控制编译源码时的标志
返回值：返回表达式执行结果。
# 案例：
>>>str = "for i in range(0,10): print(i)" 
>>> c = compile(str,'','exec')   # 编译为字节代码对象 
>>> c
<code object <module> at 0x10141e0b0, file "", line 1>
>>> exec(c)
0
1
2
3
4
5
6
7
8
9
>>> str = "3 * 4 + 5"
>>> a = compile(str,'','eval')
>>> eval(a)
17
*****************************************************************************************
globals() 函数
描述：会以字典类型返回当前位置的全部全局变量。
语法：globals()
参数：无
返回值：返回全局变量的字典。
# 案例：
>>>a='runoob'
>>> print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__',
 '__doc__': None, 'a': 'runoob', '__package__': None}
 ****************************************************************************************
map() 函数
描述：map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，
返回包含每次 function 函数返回值的新列表。
语法：map(function, iterable, ...)
参数：unction -- 函数，有两个参数
	  iterable -- 一个或多个序列
返回值：Python 2.x 返回列表。
	    Python 3.x 返回迭代器
# 案例：
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
**************************************************************************************
reversed 函数
描述：返回一个反转的迭代器。
语法：reversed(seq)
参数：seq -- 要转换的序列，可以是 tuple, string, list 或 range。
返回值：返回一个反转的迭代器。
# 案例：
# 字符串
seqString = 'Runoob'
print(list(reversed(seqString)))
 
# 元组
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(list(reversed(seqTuple)))
 
# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))
 
# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))

以上实例输出结果为：

['b', 'o', 'o', 'n', 'u', 'R']
['b', 'o', 'o', 'n', 'u', 'R']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]
**************************************************************************************
__import__() 函数
描述：__import__() 函数用于动态加载类和函数 。

	  如果一个模块经常变化就可以使用 __import__() 来动态载入。
语法：__import__(name[, globals[, locals[, fromlist[, level]]]])
参数：name -- 模块名
返回值：返回元组列表。
# 案例：
##3a.py 文件代码：
 
import os  
 
print ('在 a.py 文件中 %s' % id(os))
###test.py 文件代码：
 
import sys  
__import__('a')        # 导入 a.py 模块
执行 test.py 文件，输出结果为：

在 a.py 文件中 4394716136
***************************************************************************************
complex() 函数
描述：用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
	  如果第一个参数为字符串，则不需要指定第二个参数。。
语法：class complex([real[, imag]])
参数：real -- int, long, float或字符串；
	  imag -- int, long, float；
返回值：返回一个复数。
# 案例：
>>>complex(1, 2)
(1 + 2j)
 
>>> complex(1)    # 数字
(1 + 0j)
 
>>> complex("1")  # 当做字符串处理
(1 + 0j)
 
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
*****************************************************************************************
hasattr() 函数
描述：用于判断对象是否包含对应的属性。
语法：hasattr(object, name)
参数：object -- 对象。 			name -- 字符串，属性名。
返回值：如果对象有该属性返回 True，否则返回 False
# 案例：
class Coordinate:
    x = 10
    y = -5
    z = 0
 
point1 = Coordinate() 
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性
输出结果：

True
True
True
False
****************************************************************************************
max() 函数
描述：返回给定参数的最大值，参数可以为序列。
语法：max( x, y, z, .... )
参数：x -- 数值表达式。			y -- 数值表达式。		z -- 数值表达式。
返回值：返回给定参数的最大值。
# 案例：
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400))
print ("max(-80, -20, -10) : ", max(-80, -20, -10))
print ("max(0, 100, -400) : ", max(0, 100, -400))
以上实例运行后输出结果为：

max(80, 100, 1000) :  1000
max(-20, 100, 400) :  400
max(-80, -20, -10) :  -10
max(0, 100, -400) :  100
****************************************************************************************
round() 函数
描述：返回浮点数x的四舍五入值。
语法：round( x [, n]  )
参数：x -- 数值表达式。			n -- 数值表达式。
返回值：返回浮点数x的四舍五入值。
# 案例：
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))
以上实例运行后输出结果为：

round(70.23456) :  70
round(56.659,1) :  56.7
round(80.264, 2) :  80.26
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
**************************************************************************************
delattr() 函数
描述：delattr 函数用于删除属性。
	  delattr(x, 'foobar') 相等于 del x.foobar。
语法：delattr(object, name)
参数：object -- 对象。		name -- 必须是对象的属性。
返回值：无
# 案例：
class Coordinate:
    x = 10
    y = -5
    z = 0
 
point1 = Coordinate() 
 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
 
delattr(Coordinate, 'z')
 
print('--删除 z 属性后--')
print('x = ',point1.x)
print('y = ',point1.y)
 
# 触发错误
print('z = ',point1.z)
*************************************************************************************
hash() 函数
描述：用于获取取一个对象（字符串或者数值等）的哈希值。
语法：hash(object)
参数：object -- 对象；
返回值：返回对象的哈希值。
# 案例：
>>>hash('test')            # 字符串
2314058222102390712
>>> hash(1)                 # 数字
1
>>> hash(str([1,2,3]))      # 集合
1335416675971793195
>>> hash(str(sorted({'1':1}))) # 字典
7666464346782421378
>>>
*************************************************************************************
memoryview() 函数
描述：返回给定参数的内存查看对象(Momory view)。
	  所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，
	  在不需要复制对象基础上允许Python代码访问。
语法：memoryview(obj)
参数：obj -- 对象
返回值：返回元组列表。
# 案例：
Python2.x 应用：
>>>v = memoryview('abcefg')
>>> v[1]
'b'
>>> v[-1]
'g'
>>> v[1:4]
<memory at 0x77ab28>
>>> v[1:4].tobytes()
'bce'
Python3.x 应用：
>>>v = memoryview(bytearray("abcefg", 'utf-8'))
>>> print(v[1])
98
>>> print(v[-1])
103
>>> print(v[1:4])
<memory at 0x10f543a08>
>>> print(v[1:4].tobytes())
b'bce'
>>>
***************************************************************************************
set() 函数
描述：创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
语法：class set([iterable])
参数：iterable -- 可迭代对象对象；
返回值：返回新的集合对象
# 案例：
>>>x = set('runoob')
>>> y = set('google')
>>> x, y
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
>>> x & y         # 交集
set(['o'])
>>> x | y         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y         # 差集
set(['r', 'b', 'u', 'n'])
>>>