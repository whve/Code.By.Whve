from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

import os
# 路径设置,读取或保存的的修改路径.
os.chdir(r'D:\L. 临时文件\Z. 张珺')

from Bio import SeqIO
for seq_record in SeqIO.parse("whve.BAV-S1.fasta", "fasta"):
    print (seq_record.id)
    print (repr(seq_record.seq))
    print (len(seq_record))

# to do
"""
no.1 seq use
"""

messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
print(messenger_rna)
print(messenger_rna.translate())
