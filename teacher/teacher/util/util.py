class SearchParamUtil(object):

    @staticmethod
    def getKwargs(data={}):
        kwargs = {}
        for (k , v)  in data.items() :
           if v is not None and v != u'' :
               kwargs[k] = v
        return kwargs