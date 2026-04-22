import gc
class User:
   class Collection:
      all_user=[]
      @classmethod
      def add(cls,user):
         cls.all_user.append(user)

      @classmethod
      def remove(cls,user):
         cls.all_user.remove(user)

      @classmethod
      def show(cls):
         for user in cls.all_user:
            print(user.name)

   def __init__(self,name):
      self.name=name
      self.connection=[]
      User.Collection.add(self)

   def connect(self,other_user):
      self.connection.append(other_user)

   def show_connections(self):
      for user in self.connection:
         print(f"{self.name} is connected to {user.name}")

   def __del__(self):
      print(f"\nUser {self.name} removed")

a=User("Ram")
b=User("Janu")
c=User("Hari")

print("\nList of users")
User.Collection.show()
a.connect(c)
b.connect(a)
b.connect(c)

print("\n User connections:")
a.show_connections()
b.show_connections()
c.show_connections()
User.Collection.remove(c)
del c
gc.collect()
print("\nExisting users")
User.Collection.show()
del a
del b
gc.collect()
