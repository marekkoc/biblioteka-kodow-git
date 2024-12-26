dane = ['172.10.10.10 /24', '108.2.2.240 /28', '11.12.13.14 /20',
        '200.100.150.0 /17', '245.11.12.188 /30']

class Siec:
  def __init__(self, adres_maska: str):
    poz = adres_maska.find(' ')  # zakładam że zawsze po IP jest spacja i maska
    self.bazowyIP = adres_maska[0:poz]
    self.maska = int(adres_maska[poz + 2:])

  def strIP_bit(self):
    '''
    :return: IP jako liczbę 32-bitową (int)
    '''
    ip = self.bazowyIP
    poz = 0
    oktety = ''
    while True:
      poz = ip.find('.')
      if poz < 0: break
      oktety += '{0:08b}'.format(int(ip[0:poz]))
      ip = ip[poz + 1:]
    oktety += '{0:08b}'.format(int(ip))
    return oktety

  def adres_broadcast(self):
    '''
    :return: adres sieci i broadcast jako (32-bit, 32-bit)
    '''
    prefix = self.strIP_bit()[0:self.maska]
    return (prefix + '0' * (32 - self.maska), prefix + '1' * (32 - self.maska))

  def ileHostow(self):
    adres, broadcast = self.adres_broadcast()
    return int(broadcast, 2) - int(adres, 2) - 1

  @staticmethod
  def toString(bit32: str):
    return (str(int(bit32[0:8], 2)) + '.' + str(int(bit32[8:16], 2))
            + '.' + str(int(bit32[16:24], 2))) + '.' + str(int(bit32[24:32], 2))

  def info(self):
    print(f'{self.bazowyIP} = {self.strIP_bit()} / {self.maska}')
    adres, broadcast = self.adres_broadcast()
    print(
      f'Adres sieci: {Siec.toString(adres)} '
      f'Adres rozgłoszeniowy: {Siec.toString(broadcast)}')
    print(f'Hostów: {self.ileHostow()}')
    adresPlus = '{0:032b}'.format(int(adres, 2) + 1)
    broadcastMinus = '{0:032b}'.format(int(broadcast, 2) - 1)
    print(
      f'Adresy hostów od: {Siec.toString(adresPlus)} '
      f'do {Siec.toString(broadcastMinus)}')

for d in dane:
  s = Siec(d)
  s.info()
  print()
