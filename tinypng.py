#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
import click
import tinify

ting_keys = ["xxxxxxxxxxxxxxx"]  # API KEYS		
keys_index = 0
keys_len = len(ting_keys)

def compress_image(inputFile, outputFile, img_width):
	source = tinify.from_file(inputFile)
	if not check_api_count():
		return False
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)
	return True

# check couts
def check_api_count():
	compressions_this_month = tinify.compression_count
	if compressions_this_month >= 500:
		global keys_index
		keys_index += 1
		return check_api_key()
	else:
		return True

# check valid api key
def check_api_key():
	global keys_index
	global keys_len
	while keys_index < keys_len:
		valid = True
		try:
			tinify.key = ting_keys[keys_index]
			tinify.validate()
		except tinify.AccountError, e:
			print "Your free API Key %s validate failed!!!\n" % ting_keys[keys_index]
			valid = False
		except Exception, e:
			valid = False
		if not valid:
			keys_index += 1
		else:
			# The first 500 compressions each month are free.
			compressions_this_month = tinify.compression_count
			if compressions_this_month >= 500:
				keys_index += 1
			else:
				break
	if keys_index >= keys_len:
		print "Your free API Key has been used up!!!\n"
		return False
	return True

# Compress images under a folder
def compress_path(path, width, recurse):
	if not os.path.isdir(path):
		print "This is not a folder, please enter the correct path to the folder!"
		return
	else:
		srcPath = path 	# source path
		toPath = path 		# output path, here can change target output path
		print "srcPath = %s" % srcPath
		print "toPath = %s\n" % toPath
		offset = "    "
		space = offset
		lens = 0

		for root, dirs, files in os.walk(srcPath):
			print space + "%s" % root
			pause = False
			if len(dirs) > 0:
				space = space + offset
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
					print space + offset + "%s" % name
					lens += 1
					toFullPath = toPath + root[len(srcPath):]
					toFullName = toFullPath + '/' + name
					if os.path.isdir(toFullPath):
						pass
					else:
						os.mkdir(toFullPath)
					result = compress_image(root + '/' + name, toFullName, width)
					if not result:
						pause = True
						break
			if not recurse:
				break
			if pause:
				break
		if lens == 0:
			print "\nNo picture are processed!!!"
		else:
			print "\n%d picture are processed!!!" % lens

# compress only specified files
def compress_file(inputFile, width):
	if not os.path.isfile(inputFile):
		print "This is not a file, please enter the correct path to the file!"
		return
	print "file = %s" % inputFile
	dirname  = os.path.dirname(inputFile)
	basename = os.path.basename(inputFile)
	fileName, fileSuffix = os.path.splitext(basename)
	outputFile = inputFile  # output path, here can change target output path
	if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
		compress_image(inputFile, outputFile, width)
	else:
		print "This file type is not supported!"

@click.command()
@click.option('-f', "--file",  type=str,  default=None,  help="single file compression")
@click.option('-d', "--dir",   type=str,  default=None,  help="the compressed folder, default current directory")
@click.option('-w', "--width", type=int,  default=-1,    help="image width, unchanged default")
@click.option('-r', "--recurse", is_flag=True, help="recursively subdirectories")
def run(file, dir, width, recurse):
	print "TinyPng Runing!!!\n"

	if not check_api_key():
		return

	if file is not None:
		compress_file(file, width)						# compress only one file
		pass
	elif dir is not None:
		compress_path(dir, width, recurse)				# compress the files in the specified directory
		pass
	else:
		compress_path(os.getcwd(), width, recurse)		# compress the files in the current directory
	print "\nTinyPng Success!!!"

if __name__ == "__main__":
    run()

