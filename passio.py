#!/usr/bin/env python3

import argparse
import itertools
import sys
import time
from typing import Iterator

def banner():
    print("""
+==============================================================+
|                    Passio PASSWORD GENERATOR                |
|                        Codded by : HackNest                 |
+==============================================================+
""")


class CrunchGenerator:
    def __init__(self, min_len: int, max_len: int, charset: str):
        self.min_len = min_len
        self.max_len = max_len
        self.charset = charset
        self.charset_list = list(charset)
        
    def generate_passwords(self) -> Iterator[str]:
        for length in range(self.min_len, self.max_len + 1):
            for combination in itertools.product(self.charset_list, repeat=length):
                yield ''.join(combination)
    
    def count_combinations(self) -> int:
        total = 0
        charset_size = len(self.charset_list)
        for length in range(self.min_len, self.max_len + 1):
            total += charset_size ** length
        return total


def get_default_charsets() -> dict:
    return {
        'numeric': '0123456789',
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'alpha': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'alphanumeric': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
        'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?',
        'all': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
    }


def parse_charset(charset_str: str) -> str:
    charsets = get_default_charsets()
    
    if charset_str.startswith('@'):
        charset_name = charset_str[1:]
        if charset_name in charsets:
            return charsets[charset_name]
        else:
            print(f"Error: Unknown charset '{charset_name}'")
            print(f"Available charsets: {list(charsets.keys())}")
            sys.exit(1)
    else:
        return charset_str


def save_to_file(passwords: Iterator[str], filename: str, max_count: int = None):
    count = 0
    start_time = time.time()
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for password in passwords:
                f.write(password + '\n')
                count += 1
                
                if max_count and count >= max_count:
                    break
                
                if count % 100000 == 0:
                    elapsed = time.time() - start_time
                    rate = count / elapsed if elapsed > 0 else 0
                    print(f"\rGenerated: {count:,} passwords ({rate:.0f}/sec)", end='', flush=True)
        
        elapsed = time.time() - start_time
        print(f"\nCompleted! Generated {count:,} passwords in {elapsed:.2f} seconds")
        if elapsed > 0:
            print(f"Average speed: {count/elapsed:.0f} passwords/second")
            
    except KeyboardInterrupt:
        print(f"\nInterrupted! Generated {count:,} passwords")
        sys.exit(1)
    except Exception as e:
        print(f"\nError writing to file: {e}")
        sys.exit(1)


def print_to_console(passwords: Iterator[str], max_count: int = None):
    count = 0
    
    try:
        for password in passwords:
            print(password)
            count += 1
            
            if max_count and count >= max_count:
                break
                
    except KeyboardInterrupt:
        print(f"\nInterrupted! Generated {count:,} passwords")
        sys.exit(1)


def main():
    banner()
    parser = argparse.ArgumentParser(
        description='Crunch-like password list generator',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('min_len', type=int, help='Minimum password length')
    parser.add_argument('max_len', type=int, help='Maximum password length')
    parser.add_argument('charset', help='Character set or predefined charset (@name)')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument('-c', '--count', type=int, help='Maximum number of passwords to generate')
    parser.add_argument('-b', '--buffer-size', type=int, default=100000, 
                       help='Buffer size for file writing (default: 100000)')
    
    args = parser.parse_args()
    
    if args.min_len < 1 or args.max_len < 1:
        print("Error: Length must be positive")
        sys.exit(1)
    
    if args.min_len > args.max_len:
        print("Error: Minimum length cannot be greater than maximum length")
        sys.exit(1)
    
    charset = parse_charset(args.charset)
    if not charset:
        print("Error: Charset cannot be empty")
        sys.exit(1)
    
    generator = CrunchGenerator(args.min_len, args.max_len, charset)
    
    total_combinations = generator.count_combinations()
    print(f"Charset: {charset}")
    print(f"Length range: {args.min_len}-{args.max_len}")
    print(f"Total combinations: {total_combinations:,}")
    
    if args.count and args.count < total_combinations:
        print(f"Will generate: {args.count:,} combinations")
    
    passwords = generator.generate_passwords()
    
    if args.output:
        print(f"Saving to: {args.output}")
        save_to_file(passwords, args.output, args.count)
    else:
        print_to_console(passwords, args.count)


if __name__ == '__main__':
    main()
