import sys
import os


import os
import argparse

# for deep learning
Cnn_train_mpp="./GTSRB/Final_Training/images/"
Cnn_test_mpp="./GTSRB/Online-Test-sort"


Cnn_train_Path = "./GTSRB/Final_Training/images/JPEGImages"
Cnn_test_Path = "./GTSRB/Online-Test-sort/JPEGImages"

def main(args):

    cmd=""

    if args.operation == 'demo':
        print('demo')
        os.system('python ./demo_cnn.py')

    elif args.operation =="train_cnn_convert":
        cmd = "python ./ppm_convert_jpeg.py " + Cnn_train_mpp
        print(cmd)
        os.system(cmd)

    elif args.operation == "test_cnn_convert":
        cmd = "python ./ppm_convert_jpeg.py " + Cnn_test_mpp
        print(cmd)
        os.system(cmd)

    elif args.operation == "train_cnn":
        cmd = "python ./train_cnn.py " + Cnn_train_Path
        print(cmd)
        os.system(cmd)

    elif args.operation =="test_cnn":
        cmd = "python ./test_cnn.py " + Cnn_test_Path
        print(cmd)
        os.system(cmd)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation',  type=str, default='')
    args = parser.parse_args()

    main(args)
