############
#author:FuYuyang
#info:This is a programe for test
############
names = ['FYY','LK','WST','PYY']
message = names[-1].title() +  ' said, " I am a little boy"' + "."
print(message)
names.insert(0,'WYZ')
message = names[0].title() + ' is not my roommate' + '.'
print(message)
print('So we decide to delete Wyz from the list.')
temp = names.pop(0)
stranger = [temp]
print('roommates:')
print(names)
print('not roommates:')
print(stranger)
print('Oh! Pyy is not my roommate as well.')
print('deleting...')
temp = names.pop(-1)
stranger.append(temp)
print('roommates:')
print(names)
print('not roommates:')
print(stranger)
