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
Code to process data to features.
"""

import os
import pandas as pd


ATTRIBUTES = ['Day', 'Month', 'Year', 'High', 'Open', 'Low']
TARGET = ['Close']
PATH_RAW_DATA = 'data/raw/AAPL_1990-01-01_2021-02-28.csv'
PATH_PROCESSED_DATA = 'data/processed'
TRAIN_YEAR = 2017
VALIDATION_YEAR = 2018
TEST_YEAR = 2019


def main():

    # Get details form file name.
    stock_symbol, start_date, end_date = os.path.basename(PATH_RAW_DATA)[:-4].split('_')
    # Read data.
    stocks_df = pd.read_csv(filepath_or_buffer=PATH_RAW_DATA)
    # Reset index.
    stocks_df.reset_index(inplace=True)
    # Convert to date column.
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    # Get year separately.
    stocks_df['Year'] = stocks_df['Date'].dt.year
    # Get month separately.
    stocks_df['Month'] = stocks_df['Date'].dt.month
    # Get day separately.
    stocks_df['Day'] = stocks_df['Date'].dt.day
    # Rearrange columns.
    stocks_df = stocks_df[ATTRIBUTES + TARGET]
    # Split in train start_year - TRAIN_YEAR.
    train_stocks_df = stocks_df[stocks_df['Year'] <= TRAIN_YEAR]
    # Save train file.
    train_stocks_df.to_csv(os.path.join(PATH_PROCESSED_DATA, f"train_{stock_symbol}_{start_date}-{TRAIN_YEAR}-12-31.csv"), index=False)
    # For validation split use VALIDATION_YEAR.
    validation_stocks_df = stocks_df[stocks_df['Year'].isin([VALIDATION_YEAR])]
    validation_stocks_df.to_csv(os.path.join(PATH_PROCESSED_DATA, f"validation_{stock_symbol}_{VALIDATION_YEAR}-01-01_{VALIDATION_YEAR}-12-31.csv"), index=False)
    # Split in test anything in TEST_YEAR and after until end_year.
    test_stocks_df = stocks_df[stocks_df['Year'] >= TEST_YEAR]
    test_stocks_df.to_csv(os.path.join(PATH_PROCESSED_DATA, f"test_{stock_symbol}_{TEST_YEAR}-01-01_{end_date}.csv"), index=False)


if __name__ == "__main__":
    main()
