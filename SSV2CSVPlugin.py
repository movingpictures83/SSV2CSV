from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os
import pandas as pd

class SSV2CSVPlugin:
    def input(self, infile):
       self.data_frame = pd.read_csv(infile, sep=";", index_col=0, parse_dates=True, decimal=',')

    def run(self):
       self.data_frame.fillna(0, inplace=True)

    def output(self, outfile):
       self.data_frame.to_csv(outfile)
