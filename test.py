import argpare

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--name',"-n",default="abhishek",type=str)
    args.add_argument('--age',"-a",default=25.0,type=str,type=str)
    parse_args=args.parse_args()
    
    print(parse_args.name,parse_args.age)