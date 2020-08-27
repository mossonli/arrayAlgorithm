#
# class Mymeta(type):  # 继承默认元类的一堆属性
#     def __init__(self, class_name, class_bases, class_dic):
#         # if '__doc__' not in class_dic or not class_dic.get('__doc__').strip():
#         #     raise TypeError('必须为类指定文档注释')
#         print(class_name)
#         print(class_bases)
#         print(class_dic)
#         if not class_name.istitle():
#             raise TypeError('类名首字母必须大写')
#
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)
#
#
# class people(object, metaclass=Mymeta):
#     country = 'China'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' % self.name)

# from copy import deepcopy
#
# a = ["哈哈","呵呵", "吼吼"]
# b = deepcopy(a)
# ret = dict.fromkeys("abc", b) # fromkeys直接使用类名进行访问
# print(ret)
# ret['a'].append("hello")
# a.append("嘻嘻")     #同样会添加到字典中,因为a的地址没有变
# print(ret)
#{'a': ['哈哈', '呵呵', '吼吼', '嘻嘻'], 'b': ['哈哈', '呵呵', '吼吼', '嘻嘻']}
