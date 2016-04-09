class TaxCalc(object):

    FullTimeThrethold = 800
    NoFullTimeThretholdLv1 = 3500
    NoFullTimeThretholdLv2 = 4800
    NoFullTimeThretholdLv3 = 6600
    def __init__(self):
        pass

    @staticmethod
    def taxCalc(isFullTime,cost):
        if isFullTime == 1:
            if cost <= TaxCalc.FullTimeThrethold:
                return 0
            else:
                return (cost - TaxCalc.FullTimeThrethold)/0.8 * 0.2
        else:
            if cost <= TaxCalc.NoFullTimeThretholdLv1:
                return 0
            elif TaxCalc.NoFullTimeThretholdLv1 < cost <= TaxCalc.NoFullTimeThretholdLv2:
                return (cost - TaxCalc.NoFullTimeThretholdLv1) / 0.97 * 0.03
            elif TaxCalc.NoFullTimeThretholdLv2 < cost <= TaxCalc.NoFullTimeThretholdLv3:
                return (cost - TaxCalc.NoFullTimeThretholdLv2)/ 0.9 * 0.1 - 105
            else:
                return (cost - TaxCalc.NoFullTimeThretholdLv3)/0.8 * 0.2 - 555
