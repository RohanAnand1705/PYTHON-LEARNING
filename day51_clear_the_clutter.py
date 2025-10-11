import os



apple= os.listdir("clutterfolder")
i=1
for file in apple:
    if file.endswith(".png"):
        print(file)

        os.rename(f"clutterfolder/{file}",f"clutterfolder/{i}.png")
        i=i+1