# royman-tools
> collection of tools

## Installation
```
pip install royman-tools
```
or from Github:
```
git clone https://github.com/roymanigley/royman-tools.git
cd royman-tools
python setup.py install
```

## Tools

### TCP

#### Usage
```
from royman_tools import tcp

with tcp.Client('127.0.0.1', 4040) as client:
    client.send_str('Hello World')
    print(client.read())

with tcp.Server(4040) as server:
    server.send_str('Hello World')
    print(server.read())

tcp.scan_range('127.0.0.1', list(range(1, 65535 + 1)))
```

### Project Creator

#### Usage
```
royman-tools:create-project --help

royman-tools:create-project --project_name my-project-name
```
