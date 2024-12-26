def format2cyfrowy(v):
  if v <= 9:
    return '0' + str(v)
  return str(v)

def roznicaCzasu(t1: str, t2: str):
  t2_sek = int(t2[0:2]) * 3600 + int(t2[3:5]) * 60 + int(t2[6:8])
  t1_sek = int(t1[0:2]) * 3600 + int(t1[3:5]) * 60 + int(t1[6:8])
  t = abs(t2_sek - t1_sek)
  tg = t // 3600
  tm = (t - tg * 3600) // 60
  ts = t - tg * 3600 - tm * 60
  return format2cyfrowy(tg) + ':' + format2cyfrowy(tm) + ':' + format2cyfrowy(
    ts)

print(roznicaCzasu("09:05:08", "13:10:33"))
print(roznicaCzasu("13:10:33", "09:05:08"))
print(roznicaCzasu("09:35:08", "13:10:33"))
print(roznicaCzasu("24:00:00", "00:00:01"))
print(roznicaCzasu("24:00:00", "00:00:00"))
