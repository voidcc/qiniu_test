#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, BucketManager
import qiniu.config
import time

class Qiniu(object):

	def __init__(self, access_key = None, secret_key = None, bucket_name = None):
		self.access_key = access_key
		self.secret_key = secret_key
		self.bucket_name = bucket_name

		self.q = Auth(self.access_key, self.secret_key)

	def upload(self, key, localfile = None, expires = 3600, deleteAfterDays = 7):
		policy = {'deleteAfterDays': deleteAfterDays}
		print policy
		#token = self.q.upload_token(self.bucket_name, key, expires, policy, False)
		token = self.q.upload_token(self.bucket_name, key, expires, policy)

		ret, info = put_file(token, key, localfile)
		print(info)
		assert ret['key'] == key
		assert ret['hash'] == etag(localfile)

	def delete(self, key):
		bucket = BucketManager(self.q)
		ret, info = bucket.delete(self.bucket_name, key)
		print(info)
		assert ret == {}

	def stat(self, key):
		bucket = BucketManager(self.q)
		ret, info = bucket.stat(self.bucket_name, key)
		print(info)
		assert 'hash' in ret


if __name__ == "__main__":
	access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
	secret_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
	bucket_name = "xxxxxx"
	test = Qiniu(access_key, secret_key, bucket_name)

	#localfile = "./image/jurassic-park-tour-jeep-0.jpg"
	localfile = "./image/test-1-0.jpg"
	key = localfile.split('/')[-1]
	test.upload(key, localfile, 3600, 0)

	#localfile = "./image/jurassic-park-tour-jeep-1.jpg"
	localfile = "./image/test-1-1.jpg"
	key = localfile.split('/')[-1]
	test.upload(key, localfile, 3600, 1)

	localfile = "./image/test-1-2.jpg"
	key = localfile.split('/')[-1]
	test.upload(key, localfile, 3600, 2)

	localfile = "./image/test-1-3.jpg"
	key = localfile.split('/')[-1]
	test.upload(key, localfile, 3600, 3)

	#test.stat(key)
	#test.delete(key)

