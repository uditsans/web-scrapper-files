import json

site = input('Enter sitename: ')

a = {}
a['username'] = input('Enter Username: ')
a['password'] = input('Enter Password: ')

f = open(site+'_pass.json', 'w')
f.write(json.dumps(a))
f.close()
