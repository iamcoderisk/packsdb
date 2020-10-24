import packsdb as db
# hel =  FlashDb()
# hel.open("hello.db")
# hel.addTable('{"name": "contact","cols": ["address", "state", "country"]}')
# # hel.addTable('{"name": "users","cols": ["name", "age", "gender"]}')
# # hel.addTable("['foo', {"bar":["baz", null, 1.0, 2]}]")

# # print(hel.getName())
# mymodule.greeting("ekemini")

k =  db.PacksDB()

k.create("hello")
# k.addKey('{"name":"country", "cols":["name","continent","population"]}')
# k.add('{"name":"sarafina", "cols":["ddd","email","phone"]}')
# k.remove("sooo")
# k.get("users")
tables =  k.selectKey("country")
# # print(tables)
# k.addValue('{"name":"ecuador","continent":"europe","population":"20m"}')
# contacts =  k.selectKey("contact").getAll()
# print(contacts["email"])

# contacts =  k.selectKey("contact").byKey("_id")
# contacts =  k.selectKey("contact").update({
#     "email":"prince@gmail.com"
# })

# contact =  k.selectKey("contact").query('{"type":"select","group":["email","_id"]}')
# print(contact)
