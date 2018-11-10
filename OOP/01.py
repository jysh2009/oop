class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass
mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = 'python'
    def doHomework(self):
        print('i do home work!')

        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()

