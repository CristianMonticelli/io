diczionary = {
    'title':'la ragazza dei lupi',
    'author':'Rundell Katherine',
    'year_published':'2016'
}
print(diczionary)
diczionary['genre'] = "per ragazzi"
print(diczionary)
diczionary['year_published'] = '2018'
print(diczionary)
diczionary.pop('author')
print(diczionary)
for x in diczionary:
  print(x)
for z in diczionary:
  print(diczionary[z])
for c,v in diczionary.items():
    print(c,v)