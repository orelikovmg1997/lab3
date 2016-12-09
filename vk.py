from id import Id
from friends import Friends


name = input('Имя пользователя: ')
client = Id(name)
uid = client.execute()

friends_client = Friends(uid)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))