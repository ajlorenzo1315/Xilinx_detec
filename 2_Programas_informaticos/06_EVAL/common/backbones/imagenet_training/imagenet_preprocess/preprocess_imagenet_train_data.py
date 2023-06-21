# Copyright 2019 Xilinx Inc.
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract sub tarball for Imagenet 2012 train dataset
"""
import os, glob, argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_data_path', type=str, required=True, help='path to Imagenet train data')
    args = parser.parse_args()

    class_tar_files = glob.glob(os.path.join(args.train_data_path, '*.tar'))

    for i, class_tar_file in enumerate(class_tar_files):
        class_label = class_tar_file.split(os.path.sep)[-1].split('.')[-2]
        class_folder = os.path.join(args.train_data_path, class_label)
        os.makedirs(class_folder, exist_ok=True)

        print(class_folder)
        os.system('tar xf ' + class_tar_file + ' -C ' + class_folder)
        os.system('rm -rf ' + class_tar_file)


if __name__ == "__main__":
    main()

