import pickle

colors = ['red','green']
f=open('ch8_2.txt', 'wb')
pickle.dump(colors,f)
f.close()

del colors

f=open('ch8_2.txt', 'rb')
colors=pickle.load(f)
f.close()

print(colors)