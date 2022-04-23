import requests
import pandas as pd
from .DATA_USE import load_index

class MarketOverviewSpider:
    """
    获取沪深行情，并提供数据接口
    """
    def __init__(self):
        # 读取指数信息
        self.IndexInfo = pd.DataFrame(load_index(), columns=["name", "index", "abbrev"])

    def getIndexDataByName(self, name, start, end):
        url = "http://quotes.money.163.com/service/chddata.html"
        try:
            code = self.IndexInfo.loc[self.IndexInfo["name"] == name, "index"].values[0]
            query = {
                "code": code,
                "start": start,
                "end": end,
                "fields": 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
            }
            response = requests.get(url, params=query)
            response.encoding = "GBK"
            text_ls = response.text.split(sep='\n')
            new_ls = []
            for i in text_ls:
                new_ls.append(i.split(','))

            columns = new_ls[0]
            columns[-1] = columns[-1][:-1]
            new_ls.pop(-1)
            data = new_ls[:0:-1]
            for i in range(len(data)):
                data[i][-1] = data[i][-1][:-1]
            df = pd.DataFrame(data=data, columns=columns)
            return df
        except:
            return None
