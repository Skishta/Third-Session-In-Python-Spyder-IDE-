'''بسم الله الرحمن الرحيم'''               
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

 '''THIRD SESSION In How to use Python on Spyder IDE'''
#هنتكلم النهاردة عن مجموعة من الvariables ومهمين جدا فى البايثون
list
set
tuple
dict
#كلهم متغيرات ونقدر نخزن فيهم اكثر من قيمة
#يختلفوا عن بعض فى اكثر من شيئ
#هل يمكن التعديل علية بعد كتابتة
#هل عناصرة فى الram مرتبة
#كيفية تعريفة
#اول نوع
######### list
#وهى عبارة عن صندوق كبير اعرف احط فية مجموعة من العناصر
#عناصرها مرتبة, ,يمكن التعديل علية
#ويمكن طلب عنصر معين من الlist باستعمال الindex
#بمعنى انى اعرف استعمل معاهاالindex 
#كيفية تعريفها
list_name=[5,7,8,9.8,3]
#طبعا الارقام int والكلمات مابين التنصيص str
#to print the list
print(list_name)
#التعديل على الlist
#delete last element from the list
list_name.pop()
#delete specific element from the list using (the name of the element)
#to delete int-number write it without quotation
list_name.remove(7)
#to delete str-value write it with quotation
list_name.remove("A")
#delete specific element from the list using (the index of the element)
del list_name[0]
#كيفية ترتيب الlist
list_name.sort()
#إضافة عنصر بالقايمة
#add new element in last position of the list
list_name.append(5.5)
#add new element in specific index in list
#ولكن هنا انا بكتب فى الدالة دى حاجتين الاول هوة المكان اللى عايز تضيف فية والثانى هوة الelement اللى عايز تضيفة
#list_name.insert(place of the element in the list,element)
list_name.insert(3,7.7)
#to call specific element by index
list_name[3]
#ثانى نوع
###### set
#الset غير مرتبة ولا يمكن التعديل عليها بالindex
#وهى عابرة عن list بردك ولكنها تساعد على ان يكون الelement ذو عناصر مميزة
#بمعنى لو عندى ارقام كثيرة داخل الlist وعايز اعمل توحيد للارقام دى هستعمل الset 
listx=[1,2,3,4,1,2,3,4,0,0,4,1,3,5,6,9]
#to union the numbers we use [set]
set(listx)
#ثالث نوع
###### tuple
#الtuple مرتبة ولا يمكن التعديل عليها نهائيا
tuple=["m","G",7,8,9,"F"]
#ويمكن طلب عنصر معين من الtuple باستعمال الindex
tuple[5]
#رابع نوع
####### dict
#الdict غير مرتبة ويمكن التعديل عليها ويتم تحديد الindex لهابطريق كتابة الkey وهو الindex
#يتم استعمالة لربط key ب value ,بمعنى مثلا ربط كلمة معينة من key بمعناها من value  
dictx={"name":"Ahmed","age":28,"year":2019}
#لو حبيت اجيب عنصر معين من الdict
dictx.get("age")
dicty=["people","human"]
#add items of dicty to dictx
dictx.update(dicty)
dictx.
##############################################
#IF conditition
if 8==9:
    print("equal")
elif 8==9:
    print("Equal also")
else:
    print("Not equal")