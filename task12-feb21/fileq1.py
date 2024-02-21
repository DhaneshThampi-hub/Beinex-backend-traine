'''1.Write a Python program to read an entire text file.'''

f1=open('file.txt','w')
f1.write('Hello how are you.I am working as Trainee in backend web development @ Beinex\n')
f1.write('Beinex is a multinational firm exploring the endless possibilities of data for Cloud, Analytics, Artificial Intelligence, Machine Learning, and Automation.\n')
f1.write('In effect, Beinex architects, guides, leads, and implements solutions in Analytics, AI, and ML for the spheres of Digital Transformation, GRC, and Risk & Audit Transformation.')
f1.close()
f1=open('file.txt','r')
print("Contents of the file:")
print(f1.read())
f1.close()