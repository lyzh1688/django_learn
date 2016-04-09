class TaxCalc(object):

    FullTimeThrethold = 800
    NoFullTimeThretholdLv1 = 3500
    NoFullTimeThretholdLv2 = 5000
    NoFullTimeThretholdLv3 = 8000
    NoFullTimeThretholdLv4 = 12500
    NoFullTimeThretholdLv5 = 38500
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
                return (cost - TaxCalc.NoFullTimeThretholdLv1)/ 0.9 * 0.1 - 105
            elif TaxCalc.NoFullTimeThretholdLv3 < cost <= TaxCalc.NoFullTimeThretholdLv4:
                return (cost - TaxCalc.NoFullTimeThretholdLv1)/0.8 * 0.2 - 555
            else:
                return (cost - TaxCalc.NoFullTimeThretholdLv1)/0.75 * 0.25 - 1005