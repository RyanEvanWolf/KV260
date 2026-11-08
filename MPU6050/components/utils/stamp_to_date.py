#!/usr/bin/env python3
import sys


def decode_stamp(hex_str):
  # Clean up input and ensure '0x' prefix so base=0 handles it correctly
  s = hex_str.strip()
  if not s.lower().startswith('0x'):
    s = '0x' + s

  try:
    v = int(s, 0)
  except ValueError:
    print(f"Error: '{hex_str}' is not a valid hexadecimal number.", file=sys.stderr)
    sys.exit(1)

  # Extract bitfields
  day = (v >> 27) & 31
  month = (v >> 23) & 15
  year = 2000 + ((v >> 17) & 63)
  hour = (v >> 12) & 31
  minute = (v >> 6) & 63
  second = v & 63

  # Print the raw space-separated format matching your example
  print(f'{day} {month} {year} {hour} {minute} {second}')


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <hex_value>')
    print(f'Example: {sys.argv[0]} 3db4e663  OR  {sys.argv[0]} 0x3db4e663')
    sys.exit(1)

  decode_stamp(sys.argv[1])