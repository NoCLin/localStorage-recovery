# localStorage 数据恢复

适用于Chrome、Chromium、Electron等软件

## 数据文件

LocalStorage 文件存储位置：{APP_DATA_DIR}/Default/Local Storage/leveldb

localStorage 使用 LevelDB 作为底层数据库

```
leveldb
├── 000003.ldb
├── 000014.ldb
├── 000077.ldb
├── 000080.log
├── CURRENT
├── LOCK
├── LOG
├── LOG.old
└── MANIFEST-000079
```

其中 若干`*.ldb`存储了若干版本的数据，可从此处恢复。

请参考：https://antimatter15.com/2015/12/recovering-deleted-data-from-leveldb/

## 示例数据

bytearray：`b'\x00,{\x8cN!k\x84vpenc'` 
Unicode：`\u7b2c\u4e8c\u6b21\u7684\u6570\u636e`
中文：第二次的数据


程序输出：
```
(bytearray(b'_file://\x00\x01message'), bytearray(b'\x00,{\x8cN!k\x84vpenc'))
['0x7b2c', '0x4e8c', '0x6b21', '0x7684', '0x6570', '0x636e']
第二次的数据
```

## 解码处理

1. 去掉第一个\x00 
2. 剩余bytes 两两倒序以hex组合 (`,{` == `\x2c\x7b` => `\u7b2c` => `第`)

## 工具链

- unicode编码解码: http://www.jsons.cn/unicode/ 
- ldbdump : 
    
    用于从ldb文件dump出数据，但是会直接输出内容而不是byte array，需要手工修改源码不输出明文字符。
    > 然后 ldbdump xxxxxx.ldb > raw.file 可以发现 raw.file 里面是明文字符了，但是如果原来的数据含有中文或者二进制内容，那么导出文件不好用php处理

    请参考：https://blog.csdn.net/gold2008/article/details/70837495
    
- leveldb python leveldb库
