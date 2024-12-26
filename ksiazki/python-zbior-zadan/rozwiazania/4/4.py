znak = input('Podaj właściwy znak:')[0]
# [0] za instrukcją input() sprawi,
# że jeżeli będzie to dłuższy napis, to i tak przypiszę tylko pierwszy znak

# sposób 1
if znak in '0987654321':
  print('CYFRA!')
elif znak in 'aeyuio':
  print('SAMOGŁOSKA!')
else:
  print('SPÓŁGŁOSKA!')

# Uwaga! Zakładamy oczywiście poprawność wprowadzonego znaku. Jeżeli to nie cyfra
# i nie samogłoska, to pozostaje spółgłoska. Podobne założenie jest w sposobie 2.

# sposób 2 (z wykorzystaniem wyrażeń regularnych)
import re

if re.search('[0-9]+', znak):
  print('CYFRA!')
elif re.search('[aeyuio]+', znak):
  print('SAMOGŁOSKA!')
else:
  print('SPÓŁGŁOSKA!')
