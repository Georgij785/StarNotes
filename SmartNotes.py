import datetime
import json
import os


class note:
    def __init__(self, body_v, name_v, data_v, id_v):
        self.body = body_v
        self.name = name_v
        self.data = data_v
        self.id = id_v
        self.info = {'Name': self.name, 'Body': self.body, 'Data': self.data}

    def getData(self):
        return self.data

    def getName(self):
        return self.name

    def getbody(self):
        return self.body

    def setData(self, data_v):
        self.data = data_v
        self.info['Data'] = data_v

    def setName(self, name_v):
        self.name = name_v
        self.info['Name'] = name_v

    def setBody(self, body_v):
        self.body = body_v
        self.info['Body'] = body_v

    def __str__(self):
        return self.name + "   (" + str(self.data) + "):" + "\n" + self.body


dic = {}
print("Добро пожаловать в заметки")
count = 0
while True:

    operation = input("Введите операцию {add, redact, remove, read, show_all, stop, save, import} > ")
    if operation == "add":
        print("Добавить новую заметку")
        name = input("введите имя записи > ")
        body = input("введите тело заметки > ")
        note1 = note(body, name, datetime.datetime.today(), count)
        dic[note1.id] = note1
        count += 1
    elif operation == "redact":
        id_n = input("введите id записи > ")
        data = datetime.datetime.today()
        body = input("введите тело заметки, на которое хотите поменять > ")
        dic.get(int(id_n)).setBody(body)
        dic.get(int(id_n)).setData(data)
    elif operation == "remove":
        id_n = input("введите id записи > ")
        c = 0
        a = []
        for (p, k) in dic.items():
            a.append(k)
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if datetime.datetime.strptime(str(a[j].data), '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.strptime(
                        str(a[j + 1].data), '%Y-%m-%d %H:%M:%S.%f'):
                    a[j], a[j + 1] = a[j + 1], a[j]
        dic.clear()
        for i in a:
            dic[c] = i
            dic[c].id_n = c
            c += 1
        dic.pop(int(id_n))
    elif operation == "read":
        id_n = input("введите id записи > ")
        print(dic.get(int(id_n)).getbody())
    elif operation == "stop":
        break
    elif operation == "show_all":
        c = 0
        a = []
        for (p, k) in dic.items():
            a.append(k)
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if datetime.datetime.strptime(str(a[j].data), '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.strptime(
                        str(a[j + 1].data), '%Y-%m-%d %H:%M:%S.%f'):
                    a[j], a[j + 1] = a[j + 1], a[j]
        dic.clear()
        for i in a:
            dic[c] = i
            dic[c].id_n = c
            c += 1
        for (k, n) in dic.items():
            print(str(k) + " : " + str(n.name) + "   (" + str(n.data) + ")")
    elif operation == "save":
        c = 0
        a = []
        for (p, k) in dic.items():
            a.append(k)
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if datetime.datetime.strptime(str(a[j].data), '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.strptime(
                        str(a[j + 1].data), '%Y-%m-%d %H:%M:%S.%f'):
                    a[j], a[j + 1] = a[j + 1], a[j]
        dic.clear()
        for i in a:
            dic[c] = i
            dic[c].id_n = c
            c += 1
        jsonTable = {'Notes': {}}
        for (i, o) in dic.items():
            jsonTable['Notes'][i] = {'Name': o.name, 'Body': o.body, 'Data': str(o.data)}
        with open('data.json', 'w') as outfile:
            json.dump(jsonTable, outfile)
    elif operation == "import":
        name = input("имя файла (с расширением .json)")
        with open(str(name)) as json_file:
            is_empty = os.stat(name).st_size == 0
            if is_empty:
                print("файл пустой")
            else:
                data1 = json.load(json_file)
                for (k, p) in data1['Notes'].items():
                    if k == 0:
                        n = p[k]['Name']
                        b = p[k]['Body']
                        d = datetime.datetime.strptime(p[k]['Data'], '%Y-%m-%d %H:%M:%S.%f')
                    else:
                        n = p['Name']
                        b = p['Body']
                        d = p['Data']
                    noteR = note(b, n, d, count)
                    dic[count] = noteR
                    count += 1
        c = 0
        a = []
        for (p, k) in dic.items():
            a.append(k)
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if datetime.datetime.strptime(str(a[j].data), '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.strptime(
                        str(a[j + 1].data), '%Y-%m-%d %H:%M:%S.%f'):
                    a[j], a[j + 1] = a[j + 1], a[j]
        dic.clear()
        for i in a:
            dic[c] = i
            dic[c].id_n = c
            c += 1
    else:
        print("Incorrect operator")
