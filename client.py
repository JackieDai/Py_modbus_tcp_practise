# -*- coding: utf-8 -*-
"""
@Project : Py_modbus_tcp_practise
@File    : client
@Author  : lingxiao
@Date    : 2026-05-11 11:24
@License : (C) Copyright 2026 Ling Xiao. All Rights Reserved.
"""

# ... existing code ...
from pymodbus.client import ModbusTcpClient
# binding localhost of port: 5020
client = ModbusTcpClient(
    host="127.0.0.1",
    port=5020
)

# 连接服务器
client.connect()

result = client.read_holding_registers(
    address=0,
    count=4,
    slave=1
)

print("读取结果:")
print(result.registers)

client.close()