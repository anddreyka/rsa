from something import kek

import random

ru = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','щ','ъ','ы','ь','э','ю','я',' ',',','.','-','?']

def encodeMessage(message, e, mod):

    return list(map(lambda num: str(num**e % mod),

               map(lambda char: ru.index(char) if (char in ru) else 228, message)))

def decodeMessage( message, d, mod):

    return list(map(lambda num: ru[num] if (num < len(ru) and ru[num] in ru) else '?',
                     
           map(lambda num: int(num) ** d % mod , message)))







p = simpleNumbs[random.randint(10, 20)]

q = simpleNumbs[random.randint(21, 30)]

mod = p * q
n = mod
simpleNumbs = kek(n)
m = (p-1) * (q-1)

e = d = 1 //объявление переменных


for kek in simpleNumbs:

    if kek >= m:

        break

    if m % kek != 0:

        e = kek

        break




for i in range(m):

    if (i * e) % m == 1:

        d = i


message = input('Алиса говорит:')

encodedMessage = encodeMessage(message,e,mod)

print(f'Алиса зашифровывает сообщение: {"".join(encodedMessage)}')

print(f'Боб расшифровывает сообщение:{"".join(decodeMessage(encodedMessage, d, mod))}')
