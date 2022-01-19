now = "2022-01-18_065604"
filenames = []
for n in range(1, 100000):
    filenames.append("http://192.168.25.44:5000/static/%s/output_images/%05d.jpg" % (now, n))
print(filenames)