# inputBam = refBam + outputBam
# help to split the outputBam file

import pysam
import argparse

parser = argparse.ArgumentParser(description="python split_bam.py -in kmb.bam -r estimated_km1_1.bam -out estimated_km2_1.bam")
parser.add_argument("-in", "--input", type=str, metavar="", required=True, help="input the bam file")
parser.add_argument("-r", "--ref", type=str, metavar="", required=True, help="input the ref bam file")
parser.add_argument("-out", "--output", type=str, metavar="", required=True, help="input the output bam file")

args = parser.parse_args()

def loading_db(input_bam):
        db = {}
        ff = pysam.AlignmentFile(input_bam,'rb')
        for read in ff:
                read_id = read.qname
                db[read_id] = "y"
        ff.close()
        return(db)

if __name__=="__main__":
        part = loading_db(args.ref)
        
        ff = pysam.AlignmentFile(args.input,'rb')
        rest = pysam.AlignmentFile(args.output, "wb", template=ff)
        
        for read in ff:
                read_id = read.qname
                if read_id not in part.keys():
                        rest.write(read)
        rest.close()
        ff.close()
