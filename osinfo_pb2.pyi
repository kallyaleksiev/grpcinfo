from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OSInfo(_message.Message):
    __slots__ = ["osname", "totalRAM"]
    OSNAME_FIELD_NUMBER: _ClassVar[int]
    TOTALRAM_FIELD_NUMBER: _ClassVar[int]
    osname: str
    totalRAM: int
    def __init__(self, osname: _Optional[str] = ..., totalRAM: _Optional[int] = ...) -> None: ...

class OSQuery(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProcessInfo(_message.Message):
    __slots__ = ["children", "creationTime", "pid", "username"]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedScalarFieldContainer[int]
    creationTime: float
    pid: int
    username: str
    def __init__(self, pid: _Optional[int] = ..., username: _Optional[str] = ..., creationTime: _Optional[float] = ..., children: _Optional[_Iterable[int]] = ...) -> None: ...

class ProcessQuery(_message.Message):
    __slots__ = ["pid"]
    PID_FIELD_NUMBER: _ClassVar[int]
    pid: int
    def __init__(self, pid: _Optional[int] = ...) -> None: ...
