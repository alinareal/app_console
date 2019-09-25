# while True:
#     text = raw_input('Enter text: ')
#     if text == 'stop':
#         break
#     print(text.upper())
#
# while True:
#     reply = raw_input('Enter text: ')
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!!!')
#     else:
#         print(int(reply) ** 2)
# print('Bye')
#
# while True:
#     reply = raw_input('Enter text: ')
#     if reply == 'stop':
#         break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!!!')
#     else:
#         print(int(reply) ** 2)
# print('Bye')

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)
