# meCpG_region.py

This script can help you to calculate the average methylation of a region.

### Dependent

To apply this script, you will need the **pandas**, a python package, in your environment. The following command can help to install.

```shell
pip install pandas
```

### Usage

```shell
python meCpG_region.py -in <input_file> -ref <region_file> -p <process_number>
```

A description of these arguments are as follows:

1. <input_file> - a bed file with four columns (three columns for position, one for methylation proportion). Please use the tab ("\t") to gap the column instead of the space (" ").

   ```shell
   chr1	81	83	0.8
   ```

2. <region_file> - a bed file with regions.

   ```shell
   # 100k
   chr1,0,100000,1_0_100000
   chr1,100000,200000,1_100000_200000
   
   # promoter
   chr1,12027,17027,ENSDARG00000099104
   chr1,6822,11822,ENSDARG0000010240
   ```



### Note

All the .db file were based on the zebrafish GRCz11 genome.