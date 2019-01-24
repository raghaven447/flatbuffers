# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import encode
from . import number_types
from . import packer

def GetSizePrefix(buf, offset):
	"""Extract the size prefix from a buffer."""
	return encode.Get(packer.int32, buf, offset)

def GetBufferIdentifier(buf, offset, size_prefixed = False):
        """Extract the file_identifier from a buffer"""
        offset+=(number_types.UOffsetTFlags.bytewidth if size_prefixed else 0) + number_types.UOffsetTFlags.bytewidth # offset sizeof(root table offset) + sizeof(size prefix) if present   
        return buf[offset:offset+encode.FILE_IDENTIFIER_LENGTH]

def BufferHasIdentifier(buf, offset, file_identifier, size_prefixed = False):
        return GetBufferIdentifier(buf, offset, size_prefixed = size_prefixed)==file_identifier

def RemoveSizePrefix(buf, offset):
	"""
	Create a slice of a size-prefixed buffer that has
	its position advanced just past the size prefix.
	"""
	return buf, offset + number_types.Int32Flags.bytewidth
