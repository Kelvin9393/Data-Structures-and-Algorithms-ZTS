import time

nemos = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
large = ["nemo"] * 100000

def find_nemo(array):
    t0 = time.time()
    for item in array:
        if item == "nemo":
            print("Found NEMO!")
            break

    t1 = time.time()
    print(f'Call to find Nemo took { t1 - t0 } seconds.')

find_nemo(nemos)
find_nemo(everyone)
find_nemo(large)

    