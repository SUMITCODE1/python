color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('SampleText.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('SampleText.txt')
print(content.read())
