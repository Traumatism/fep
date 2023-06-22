import base64

from typing import SupportsBytes, final


class Encoding:
    """Class that contains encoding/decoding utils"""

    @final
    def encode_base85(self, value: SupportsBytes) -> str:
        """Applies b85encode() on `value`"""
        return base64.b85encode(bytes(value)).decode()

    @final
    def decode_base85(self, value: SupportsBytes) -> str:
        """Applies b85decode() on `value`"""
        return base64.b85decode(bytes(value)).decode()

    @final
    def encode_base64(self, value: SupportsBytes) -> str:
        """Applies b64encode() on `value`"""
        return base64.b64encode(bytes(value)).decode()

    @final
    def decode_base64(self, value: SupportsBytes) -> str:
        """Applies b64decode() on `value`"""
        return base64.b64decode(bytes(value)).decode()

    @final
    def encode_base32(self, value: SupportsBytes) -> str:
        """Applies b32encode() on `value`"""
        return base64.b32encode(bytes(value)).decode()

    @final
    def decode_base32(self, value: SupportsBytes) -> str:
        """Applies b32decode() on `value`"""
        return base64.b32decode(bytes(value)).decode()
