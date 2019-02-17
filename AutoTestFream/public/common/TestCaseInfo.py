
class TestCaseInfo(object):
    '''
    测试用例的信息
    '''
    def __init__(self,id="",name="",owner="",result="Failed",startime="",endtime="",secondsDuration="",errorinfo=""):
        self.id = id
        self.name=name
        self.owner=owner
        self.result=result
        self.startime=startime
        self.endtime=endtime
        self.secondsDuration=secondsDuration
        self.errorinfo=errorinfo



        