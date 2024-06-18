from pyfzz import pyfzz
import os
from tqdm import tqdm


if __name__ == '__main__':
    fzz = pyfzz()

    directory_path = "/home/robat/Programms/FastZigZag/fzz-main/fzztest/fzzdata"

    if os.path.exists(directory_path):

        filenames = os.listdir(directory_path)

        for filename in tqdm(filenames):
            fullpath = os.path.join(directory_path, filename)
            data = fzz.read_file(fullpath)
            bars = fzz.compute_zigzag(data)

            fzz.write_file(os.path.join(directory_path, (filename.replace(".txt", "_pers.txt"))), bars)


    else:
        print("Directory not found")






    """
    # You can use the following code to test the function directly with a list of insertion and deletion operations.
    bars = fzz.compute_zigzag([('i', [0]), ('i', [1]), ('i', [0, 1]), ('d', [0, 1]), ('d', [1])])
    print(bars)

    # Alternatively you can read the filtration from a file
    # and then write the barcodes into a file.
    data = fzz.read_file('sample_filt')
    bars = fzz.compute_zigzag(data)
    print(f'Bars from file {bars}')
    fzz.write_file('sample_filt_pers', bars)
"""