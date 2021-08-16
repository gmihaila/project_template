# coding=utf-8
# Copyright 2018 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Code for data manipulation.
"""

import os
import pandas_datareader as web


STOCK_SYMBOL = 'AAPL'
START_DATE = '1990-01-01'
END_DATE = '2021-02-28'
DATA_SOURCE = 'yahoo'
PATH_RAW_DATA = 'data/raw'

def main():

    # Get start year.
    start_year = START_DATE.split("-")[0]
    # Get end year.
    end_year = END_DATE.split("-")[0]
    # Read data.
    stocks_df = web.DataReader(STOCK_SYMBOL, data_source=DATA_SOURCE, start=START_DATE, end=END_DATE)
    # Reset index.
    stocks_df.reset_index(inplace=True)
    # Save data to csv file.
    stocks_df.to_csv(os.path.join(PATH_RAW_DATA, f"{STOCK_SYMBOL}_{START_DATE}_{END_DATE}.csv"), index=False)


if __name__ == "__main__":
    main()
