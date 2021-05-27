class Utils:
    @staticmethod
    def removekey(d, key):
        # shallow copy
        r = dict(d)
        r.pop(key, None)
        return r
