### 七牛实现上传后定时删除的方法

在生成上传证书的时候，添加`deleteAfterDays`的上传策略

##### 方法一
```
q = Auth(access_key, secret_key)
policy = {'deleteAfterDays': deleteAfterDays）
token = q.upload_token(bucket_name, key, expires, policy, False)
```

##### 方法二

修改源文件，在auth.py的_policy_fields中添加`deleteAfterDays`项，然后使用类似以下代码

```
q = Auth(access_key, secret_key)
policy = {'deleteAfterDays': deleteAfterDays）
token = q.upload_token(bucket_name, key, expires, policy)
```
