版本：protobuf3
环境：python3
安装：
    下载：https://github.com/protocolbuffers/protobuf/releases
    protoc-3.9.1.linux-x86_64.zip
    解压到/usr/local/proto文件夹并添加软连接
    ln -s /usr/local/protoc/bin/protoc /usr/bin/protoc
    pip install python3-protobuf


实例：
    编译生成类
    protoc -I=./ --python_out=./ addressbook.proto
    生成数据
    python createdate.py date.pr
    读取数据
    python readdate.py date.pr

