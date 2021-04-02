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

import pandas as pd
from sklearn.model_selection import train_test_split


def main():

    # Read data.
    dataset = pd.read_csv("data/iris.csv")

    # Split train-dev-test
    iris_features = dataset[
        ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    ]
    iris_species = dataset["Species"]

    data_train, data_test, labels_train, labels_test = train_test_split(
        iris_features, iris_species, train_size=0.8, random_state=123
    )

    data_train, data_validation, labels_train, labels_validation = train_test_split(
        data_train, labels_train, train_size=0.8, random_state=123
    )

    # Save data splits
    pd.concat([data_train, labels_train], axis=1).to_csv(
        "data/iris_train.csv", index=False
    )
    pd.concat([data_validation, labels_validation], axis=1).to_csv(
        "data/iris_validation.csv", index=False
    )
    pd.concat([data_test, labels_test], axis=1).to_csv(
        "data/iris_test.csv", index=False
    )


if __name__ == "__main__":
    main()
