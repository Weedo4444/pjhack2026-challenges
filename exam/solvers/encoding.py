"""Kodowania i reprezentacja danych."""
import base64


def decode_base64(encoded: str) -> bytes:
    return base64.b64decode(encoded.strip(), validate=True)


def decode_hex(encoded: str) -> bytes:
    return bytes.fromhex(encoded.removeprefix('0x'))


def as_text(data: bytes) -> str:
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return 'hex:' + data.hex()


def int_bytes(value: int, length: int | None = None) -> bytes:
    if value < 0:
        raise ValueError('Liczba musi być nieujemna')
    return value.to_bytes(length if length is not None else max(1, (value.bit_length() + 7) // 8), 'big')
