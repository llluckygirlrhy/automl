'''
@Descripttion: 
@version: 
@Author: feliciaren
@Date: 2020-02-02 18:48:48
@LastEditors  : feliciaren
@LastEditTime : 2020-02-10 16:07:56
'''
import json
import uuid
import time

class Study(object):
    
    def __init__(self,
                name,
                configuration,
                algorithm = "BayesianOptimization",
                create_time = None,
                update_time = None):

        self.name = name
        self.configuaration = configuration
        self.algorithm = algorithm
        self.create_time = create_time
        self.update_time = update_time

    def ToJson(self):
        dic = self.ToDict()
        with open(self.name,'w',encoding='utf-8') as f:
            json.dump(f,dic,indent=4)

    def PrintInfo(self):
        print("================{}_Configuration================".format(self.study_name,self.id))
        print("Create Time: {}, Update Time:{}".format(self.create_time,self.update_time))
        print("Feasible Space:")
        for key in self.configuaration:
            print("{}: {}".format(key,self.configuaration[key]))
    
    def ToDict(self):
        dic = {}
        dic['name'] = self.name
        dic['configuaration'] = self.configuaration
        dic['create_time'] = self.create_time
        dic['update_time'] = self.update_time
        return dic

    @classmethod
    def FromJson(self,json_file):
        with open(json_file,'r',encoding='utf-8') as f:
            dic = json.load(f)

        try:
            assert('name' in dic)
            name = dic.pop('name') + uuid.uuid3(uuid.NAMESPACE_DNS,dic['name'])
        except AssertionError:
            name = uuid.uuid3(uuid.NAMESPACE_DNS,dic['name'])

        try:
            assert('algorithm' in dic)
            algorithm = dic.pop('algorithm')
            return Study(name = name,configuration = dic['configuration'],algorithm = algorithm, create_time = time.time(),update_time = time.time())
        except AssertionError:
            return Study(name = name,configuration = dic['configuration'],create_time = time.time(),update_time = time.time())