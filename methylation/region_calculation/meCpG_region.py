import argparse
import pandas as pd
import os
from tqdm import tqdm
from multiprocessing import Process, Queue, current_process

parser = argparse.ArgumentParser(description="A script help you to calculate the average methylation of a region.")
parser.add_argument("-in", "--input", type=str, metavar="", required=True, help="input the bed file")
parser.add_argument("-ref", "--ref", type=str, metavar="", required=True, help="input the ref bed file")
parser.add_argument("-p", "--process", type=int, metavar="", required=True, help="number of process")
args = parser.parse_args()

def bin_methylation(input_str):
        input_str = input_str.split(",")
        tmp = []
        tmp_db = Mydate.copy()
        chr_tmp = tmp_db[tmp_db["ref_ID"] == str(input_str[0])]
        mes = chr_tmp[(int(input_str[1]) <= chr_tmp["start"] ) & (chr_tmp["end"] <= int(input_str[2]))]
        ave = mes['modified_percentage'].mean()
        tmp.append(input_str[3])
        tmp.append(ave)
        return (tmp)

def worker(inqueue, outqueue):
        for frame in iter(inqueue.get, "STOP"):
                outqueue.put(bin_methylation(frame))
        outqueue.put(f"{current_process().name}: BYE!")

def manager():
        PROCESSES = args.process
        inqueue = Queue()
        outqueue = Queue()

        for i in range(PROCESSES):
                Process(target=worker, args=(inqueue, outqueue)).start()

        with open(args.ref) as ff:
                for l in ff:
                        inqueue.put(l.replace("\n", ""))

        for i in range(PROCESSES):
                inqueue.put("STOP")

        stop_count = 0  
        pbar = tqdm(total=total, desc=args.input)
        while stop_count < PROCESSES:
                pbar.update()
                result = outqueue.get()
                
                if len(result) == 2:
                        of.write(str(result[0]) + "\t" + str(result[1]) + "\n")
                
                # print(str(result[0]) + "\t" + str(result[1]))
                elif result[-4:] == "BYE!":
                        stop_count += 1

        pbar.close()
        inqueue.close()
        outqueue.close()
        
if __name__=="__main__":
  
        # loading the site bed file
        Index = ["ref_ID", "start", "end", "modified_percentage"]
        Mydate = pd.read_csv(args.input, header=None, names=Index, sep= "\t")

        # loading the output
        of = open(args.input.replace(".bed", "") + "_" + args.ref.replace(".db", "") + ".bed", "w")

        # loading the promoter database bed file
        DB_index = ["chr", "start", "end", "target_id"]
        DB = pd.read_csv(args.ref,header=None, names=DB_index)
        total = len(DB)

        manager()
