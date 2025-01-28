# '''  Accedental Modification  '''

# class College:
#     def __init__(self):
#         self.balance=50000
# c=College()
# print(c.balance)
# c.balance=100
# print(c.balance)
# del c.balance
# print(c.balance)


# '''  Preventation of Accedental Modification  '''

# class College:
#     def __init__(self):
#         self._balance=50000
# c=College()
# print(c._balance)


# '''  Encapsulation without authentication  '''

# class College:
#     def __init__(self):
#         self._balance=50000
#     def getbalance(self):
#         return self._balance
# c=College()
# print(c.getbalance())


# '''  Encapsulation with Authentication '''

# class College:
#     def __init__(self):
#         self._balance = 50000
#     def getbalance(self,password):
#         if password == 2025:
#             return self._balance
#         else:
#             return "You are nit autherised user."
# c=College()
# print(c.getbalance(2025))