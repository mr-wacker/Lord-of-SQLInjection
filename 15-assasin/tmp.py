common = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
passwd = ''

ans = 'ab'

k = 'ac'

for i in range(len(ans)):
    for guess in common:

        if guess == ans[i]:
            passwd += guess
            print(passwd) # ab

        