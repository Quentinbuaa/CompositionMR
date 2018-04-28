import os
from tinydb import TinyDB, Query, where


class LoggerDB():
    def __init__(self, db_name):
        self.db_name=db_name
        self.db_path = "../DataRepository"
        self.lable_list= []

    def connectDB(self):
        try:
            self.db = TinyDB(self.db_path+self.db_name)
        except Exception as e:
            print("Cannot connect DataBase")

    def setLabelList(self, label_list):
        self.label_list = label_list

    def insert(self, data_list):
        temp_data = dict(zip(self.label_list, data_list))
        self.db.insert(temp_data)

    def purge(self):
        self.db.purge()

    def query(self):
        return self.db.search((Query()["Num"].test(lambda s: s>=1)))

    def getLabels(self):
        if not len(self.db) <= 0:
            self.records = self.db.all()
            return self.records[0].keys()
        else:
            return []

class Logger():
    def __init__(self, file_name):
        self.file_name = os.path.join("C:/Users/ThinkPad/Dropbox/我的坚果云/Composition/ExperimentalData",file_name)
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)

    def LogMutationScore(self, message):
        with open(self.file_name, "a") as fd:
            fd.write(message)


def countCMRNumber():
    j = 0
    count = 0
    count_list = []
    for i in range(200):
        if j >= 10:
            j = 0
            count_list.append(count)
            count = 0
        j += 1
        print(j)
        if query_result[i]["Equality"] == 1:
            count += 1
    count_list.append(count)
    print(count_list)
    print(len(count_list))

if __name__ == "__main__":
    #Logger().LogMutationScore("as")
    test_db = LoggerDB("knn.db")
    test_db.connectDB()
    query_result = test_db.query()
    for item in query_result:
        if item["Equality"] == 0:
            print(item)


