class Student(object):
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores

    def get_average(self):
        values=list(self.scores.values())
        avg=sum(values)/len(values)
        return round(avg,2)

    def get_score(self, subject):
        return self.scores.get(subject, None)

    def show_info(self):
        print('姓名',self.name)
        print('各科成绩',self.scores)
        print('平均分',self.get_average())


if __name__=='__main__':
    s1=Student("bob",{"数学": 85, "英语": 78, "Python": 92})
    s1.show_info()