# TinyPngUtil
English | [中文](https://github.com/zhllineme/TinyPngUtil/blob/main/README_zh.md) 

A tool for TinyPng to use free api key. Support multiple api keys. 

- Validate keys in order and self set next valid key.

- Overwrite the original image by default after compression.

- The hierarchical directory for printing compressed files.

- Total number of compressed files to print.

- The operation will be terminated after the free times are used up. 

TinyPng : https://tinypng.com/

Apply for api key ： https://tinypng.com/developers

A key can compress up to 500 images per month for free, so you can apply for multiple keys.

# Install

first install python, then use pip install packages.

```
pip install --upgrade tinify
pip install click
```

# Use case

 After you have applied for the API key, you need to modify tinypng.py to fill in the API key to which you applied.

```
ting_keys = ["xxxxxxxxxxxxxxx"]  # API KEYS
```



- For help

```
python tinypng.py --help
```



- Compress all picture files under the current folder, do not contain subdirectories.

```
python tinypng.py
```



- Compress all picture files under the current folder and subdirectories.

```
python tinypng.py -r
```



- Compress all picture files by target folder, do not contain subdirectories.

```
python tinypng.py -d D:\github_project\TinyPngUtil
```



- Compress target single file.

```
python tinypng.py -f D:\github_project\TinyPngUtil\test.png
```



- Compress  file with target width.

```
python tinypng.py -f D:\github_project\TinyPngUtil\test.png -w 100
```

