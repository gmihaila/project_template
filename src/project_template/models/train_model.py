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
Code to train model.
"""

import pandas as pd

from sklearn.linear_model import LinearRegression


TRAIN_DATA_PATH = 'data/processed/train_AAPL_1990-01-01-2017-12-31.csv'
VALIDATION_DATA_PATH = 'data/processed/validation_AAPL_2018-01-01_2018-12-31.csv'


def main():
    # Read train data.
    train_stocks_df = pd.read_csv(filepath_or_buffer=TRAIN_DATA_PATH)
    # Read validation data.
    validation_stocks_df = pd.read_csv(filepath_or_buffer=VALIDATION_DATA_PATH)



if __name__ == '__main__':
    main()