""" Wylicz zyski z lokaty lub na koncie oszczędnościowym """

# print('Witaj w programie Lokatka !')


class Zysk():
    def __init__(self, kwota:float, procent:float, miesiac:float) -> float:
        self.kwota = kwota
        self.procent = procent
        self.miesiac = miesiac
        
        self.netto = 0
        self.one_netto = 0
        
    def wylicz(self):
        """Liczymy zyski """
        brutto = self.kwota * (self.procent / 100 ) * self.miesiac / 12
        belka = brutto * 0.18
        self.netto = brutto - belka
        if self.miesiac >=2:
            self.one_netto = self.netto / self.miesiac
        print('Na ile miesięcy: {}'.format(self.miesiac))
        print('-' * 50)
        print('Wyliczony zysk brutto to: %.2f zł ' % brutto)
        print('Podatek belki to: %.2f zł' % belka)
        print('A kwota netto na czysto to: %.2f zł' % self.netto)
        print('-' * 50)
        
    def symulacja(self):
        """ Funkcja wyliczy symulację zysków w kolejnych miesiącach  """
        if self.miesiac >= 2:
            for x in range(1, self.miesiac+1):
                print('Miesiąc %i - kwota %.2f zł' % (x, self.one_netto * x))

        
        
if __name__ == '__main__':
    michal = Zysk(5000,2.7,9)
    michal.wylicz()
    print('-' * 50)
    michal.symulacja()


    
