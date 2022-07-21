def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Sample Demo Exercises\n")
        txt = open(fname)
        print(txt.read())
file_read('SampleText.txt')

