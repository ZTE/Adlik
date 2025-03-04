# Copyright 2019 ZTE corporation. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# pylint: disable=no-member

import enum
from enum import Enum

from onnx import TensorProto as OnnxTensorProto
from tensorflow.core.framework.types_pb2 import DataType as TfDataType  # pylint: disable=no-name-in-module

_ONNX_DATA_TYPE = OnnxTensorProto.DataType  # pylint: disable=no-member


class DataType(Enum):
    # Boolean values.

    BOOL = enum.auto()

    # Integer values.

    INT8 = enum.auto()
    UINT8 = enum.auto()
    INT16 = enum.auto()
    UINT16 = enum.auto()
    INT32 = enum.auto()
    UINT32 = enum.auto()
    INT64 = enum.auto()
    UINT64 = enum.auto()

    # Floating number values.

    FLOAT16 = enum.auto()
    BFLOAT16 = enum.auto()
    FLOAT = enum.auto()
    DOUBLE = enum.auto()

    # Complex values.

    COMPLEX64 = enum.auto()
    COMPLEX128 = enum.auto()

    # String values.

    STRING = enum.auto()

    @staticmethod
    def from_tf_data_type(data_type: int):
        if data_type == TfDataType.DT_HALF:
            return DataType.FLOAT16

        return DataType[TfDataType.Name(data_type)[len('DT_'):]]

    def to_tf_data_type(self) -> int:
        if self == DataType.FLOAT16:
            return TfDataType.DT_HALF

        return TfDataType.Value(f'DT_{self.name}')

    @staticmethod
    def from_onnx_data_type(data_type: int):
        return DataType[_ONNX_DATA_TYPE.Name(data_type)]

    def to_onnx_data_type(self) -> int:
        return _ONNX_DATA_TYPE.Value(self.name)

    @staticmethod
    def from_tensorrt_data_type(data_type):
        import tensorrt  # pylint: disable=import-outside-toplevel

        if data_type == tensorrt.DataType.HALF:
            return DataType.FLOAT16

        return DataType[data_type.name]

    def to_tensorrt_data_type(self):
        import tensorrt  # pylint: disable=import-outside-toplevel

        if self == DataType.FLOAT16:
            return tensorrt.DataType.HALF

        return getattr(tensorrt.DataType, self.name)

    @staticmethod
    def from_openvino_data_type(data_type):
        precision_map = {
            'F32': DataType.FLOAT,
            'F16': DataType.FLOAT16,
            'I64': DataType.INT64,
            'I32': DataType.INT32,
            'I8': DataType.INT8,
            'U8': DataType.UINT8,
            'U32': DataType.UINT32,
            'BOOLEAN': DataType.BOOL
        }
        return precision_map[data_type.upper()]

    @staticmethod
    def from_paddle_data_type(data_type: str):
        precision_map = {
            'paddle.uint8': DataType.UINT8,
            'paddle.int8': DataType.INT8,
            'paddle.int16': DataType.INT16,
            'paddle.int32': DataType.INT32,
            'paddle.int64': DataType.INT64,
            'paddle.float16': DataType.FLOAT16,
            'paddle.float32': DataType.FLOAT,
            'paddle.float64': DataType.DOUBLE,
            'paddle.bfloat16': DataType.BFLOAT16,
            'paddle.bool': DataType.BOOL,
            'paddle.complex64': DataType.COMPLEX64,
            'paddle.complex128': DataType.COMPLEX128,
        }
        return precision_map[data_type]

    @staticmethod
    def to_torch_data_type(type_str):
        import torch  # pylint: disable=import-outside-toplevel

        torch_data_type_map = {
            'FLOAT': torch.float,
            'DOUBLE': torch.double,
            'COMPLEX64': torch.complex64,
            'COMPLEX128': torch.complex128,
            'FLOAT16': torch.float16,
            'BFLOAT16': torch.bfloat16,
            'UINT8': torch.uint8,
            'INT8': torch.int8,
            'INT16': torch.int16,
            'INT32': torch.int32,
            'INT64': torch.int64,
            'BOOL': torch.bool
        }
        return torch_data_type_map[type_str.upper()]

    @staticmethod
    def from_torch_data_type(type_str):
        import torch  # pylint: disable=import-outside-toplevel

        precision_map = {
            torch.float: DataType.FLOAT,
            torch.double: DataType.DOUBLE,
            torch.complex64: DataType.COMPLEX64,
            torch.complex128: DataType.COMPLEX128,
            torch.float16: DataType.FLOAT16,
            torch.bfloat16: DataType.BFLOAT16,
            torch.uint8: DataType.UINT8,
            torch.int8: DataType.INT8,
            torch.int16: DataType.INT16,
            torch.int32: DataType.INT32,
            torch.int64: DataType.INT64,
            torch.bool: DataType.BOOL
        }
        return precision_map[type_str]

    @staticmethod
    def from_oneflow_data_type(type_str):
        import oneflow  # pylint: disable=import-outside-toplevel

        oneflow_data_type_map = {
            'FLOAT': oneflow.float,
            'DOUBLE': oneflow.double,
            'FLOAT16': oneflow.float16,
            'BFLOAT16': oneflow.bfloat16,
            'UINT8': oneflow.uint8,
            'INT8': oneflow.int8,
            'INT32': oneflow.int32,
            'INT64': oneflow.int64,
            'BOOL': oneflow.bool
        }
        return oneflow_data_type_map[type_str.upper()]
