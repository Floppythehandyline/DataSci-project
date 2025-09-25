import pandas
sr = pandas.Series([11,11,2,7,9,6,6])
print(sr.unique(),                   #ใช้แสดงค่าที่ไม่ซ้ำ(unique)
      sr.nunique(),                  #จำนวนค่าที่ unique
      sr.is_unique,sep="\n")         #ตรวจสอบว่ามัน unique รึป่าว

print('\n',sr.value_counts())       #นับว่ามีตัวซ้ำกี่ตัว