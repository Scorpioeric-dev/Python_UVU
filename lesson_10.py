import pickle
import shelve

db_file = shelve.open('letters.txt', 'c')
db_file['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file['end'] = ['x', 'y', 'z']
db_file.close()

outfile = open('data.txt', 'wb')
letters = ['a', 'b', 'c']
pickled_letters = pickle.dumps(letters)
print('4', pickled_letters)
unpickled_letters = pickle.loads(pickled_letters)
print(unpickled_letters)

out_file = open('mydata.txt', 'w')
out_file.write('Hello\n')
out_file.write('world\n')
#
in_file = open('mydata.txt', 'r')
first = in_file.read(1)
second = in_file.read()

in_file.seek(0)

print(in_file.readline())

# weekends = ['Saturday\n', 'Sunday\n']
# out_file.writelines(weekends)
# out_file.flush()
#
# out_file.close()
#
# print(in_file.readlines())
# ['First line\n', 'Last line']
# in_file.close()

out_file = open('mydata.txt', 'a')
out_file.write('\nGoodbye')
# reveals position of a
print(out_file.tell())
