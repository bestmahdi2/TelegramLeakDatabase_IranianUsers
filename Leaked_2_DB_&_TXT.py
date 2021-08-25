from json import loads, dumps
from sys import stdout
from os import listdir

class databaseTel:
    def __init__(self):
        self.excepts = []
        address = './databases/'

        files = [f'{address}{i}' for i in listdir(address) if i.endswith(".txt") and not i.endswith(".LDB.txt")]
        for file in files:
            self.myLines = []
            self.data = []
            self.counter = 0
            print(f'Start for: {file}')
            self.separate_lines(file)
            self.exec_str()
            self.dict_data()
            self.writeTXT(file.replace(".txt", ".LDB.txt"))
            self.writeSqlite(file.replace(".txt", ".LDB.txt"), f"{address}LightDB.db")
            print()
        self.find_dup(f"{address}LightDB.db", f"{address}LightDB.no_dup.db")
        print("\a")

        print(f"excepts:\n{self.excepts}")
        print(f'counter: {self.counter}')

    def separate_lines(self, datebase):
        x = 0
        with open(datebase, "r", encoding="utf-8") as file:
            for line in file:
                stdout.write(f'\rReading Line Count: {x + 1}')
                if '{"settings":' in line:
                    continue
                if "\"message\"" in line:
                    try:
                        exe = {}
                        exec("thisLine = " + f"{line.replace('true', 'True').replace('false', 'False')}", exe)
                        self.myLines.append(exe['thisLine'])
                    except SyntaxError:
                        self.excepts.append(line)
                x += 1
            print(f'\rReading Line Count: {x}')

    def exec_str(self):
        x = 0
        counter = len(self.myLines)
        while x < counter:
            stdout.write(f'\rExec "message" Count: {x + 1}/{counter}')
            exec(f"self.myLines[x]['message'] = {self.myLines[x]['message']}")
            x += 1
        print(f'\rExec "message" Count: {x}/{counter}')

    def dict_data(self):
        x = 0
        counter = len(self.myLines)
        while x < counter:
            stdout.write(f'\rCollect Data Count: {x+1}/{counter}')
            id = self.myLines[x]['id']

            info = {}
            info["id"] = id
            info["phone"] = int(self.myLines[x]['phone'])
            if "username" in self.myLines[x]['message']: info["username"] = f"@{self.myLines[x]['message']['username']}"

            self.data.append(info)

            self.counter += 1
            x += 1

        self.data = [dict(tupl) for tupl in {tuple(dic.items()) for dic in self.data}]
        print(f'\rCollect Data Count: {x}/{counter}')

    def writeTXT(self, file):
        with open(file, "w", encoding="utf-8") as f:
            stdout.write(f'\rWriting down to LightDB:')
            f.write(dumps(self.data, ensure_ascii=False, indent=1))
            stdout.write("")
            print(f'\rDone!')

    def writeSqlite(self, file, database):
        with open(file, "r") as file:
            loader = loads(file.read())

        import sqlite3
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute(
            "CREATE TABLE  IF NOT EXISTS People (UID integer PRIMARY KEY, id integer NOT NULL, phone integer NOT NULL, username text)")

        for load in loader:
            if len(load) == 2:
                sql = ''' INSERT INTO People(id,phone)
                              VALUES(?,?) '''
                cur = conn.cursor()
                cur.execute(sql, (load['id'], load['phone']))
            else:
                sql = ''' INSERT INTO People(id,phone,username)
                              VALUES(?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, (load['id'], load['phone'], load['username']))

        conn.commit()


if __name__ == '__main__':
    databaseTel()



