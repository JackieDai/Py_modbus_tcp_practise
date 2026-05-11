# -*- coding: utf-8 -*-
"""
@Project : Py_modbus_tcp_practise
@File    : server.py
@Author  : lingxiao
@Date    : 2026-05-11 11:09
@License : (C) Copyright 2026 Ling Xiao. All Rights Reserved.
"""

# ... existing code ...
from pymodbus.server import StartTcpServer

from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext
)

# Creating data to register in Modbus
"""
[25, 220, 1234, 888]
    address    value
    0           25
    1           220
    2           1234
    3           888
---
也即是 Holding Register 里的数据，
例如
    address    value
    0           温度
    1           电压
    2           电流
    3           功率 
"""
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [25, 220, 1234, 888]),
    zero_mode=True # 这里是pymodbus 最恶名昭著的问题之一，pymodbus 会偷偷做地址+1; 设置该属性则禁止+1
)

context = ModbusServerContext(slaves=store, single=True)

print("Modbus TCP Server Running...")


StartTcpServer(
    context=context,
    address=("0.0.0.0", 5020)
)