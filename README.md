# Passio Password Generator

A Python implementation of the popular Crunch password list generation tool. This tool generates all possible password combinations based on specified character sets and length ranges.

## Features

- Generate password combinations with customizable character sets
- Support for predefined character sets (numeric, lowercase, uppercase, alphanumeric, etc.)
- Output to console or file
- Progress tracking and performance metrics
- Interruptible generation (Ctrl+C)
- Limit number of generated passwords
- Memory-efficient generation using iterators

## Installation

No additional dependencies required. Works with Python 3.6+.

## Usage

### Basic Syntax
```bash
python passio.py <min_length> <max_length> <charset> [options]
```

### Examples

1. **Generate 4-6 character lowercase passwords:**
   ```bash
   python passio.py 4 6 @lower
   ```

2. **Generate 1-3 digit numbers:**
   ```bash
   python passio.py 1 3 0123456789
   ```

3. **Generate 5-character alphanumeric passwords to file:**
   ```bash
   python passio.py 5 5 @alphanumeric -o wordlist.txt
   ```

4. **Generate first 1000 combinations only:**
   ```bash
   python passio.py 3 4 @alpha -c 1000
   ```

5. **Custom character set:**
   ```bash
   python passio.py 3 3 abc123
   ```

### Predefined Character Sets

- `@numeric` - 0123456789
- `@lower` - abcdefghijklmnopqrstuvwxyz
- `@upper` - ABCDEFGHIJKLMNOPQRSTUVWXYZ
- `@alpha` - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
- `@alphanumeric` - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
- `@symbols` - !@#$%^&*()_+-=[]{}|;:,.<>?
- `@all` - All characters combined

### Command Line Options

- `-o, --output` - Save output to file instead of console
- `-c, --count` - Maximum number of passwords to generate
- `-b, --buffer-size` - Buffer size for file writing (default: 100000)

## Performance

The tool is optimized for performance:
- Uses Python's `itertools.product` for efficient combination generation
- Streams output to avoid memory issues with large wordlists
- Shows progress indicators for long-running operations
- Supports graceful interruption

## Example Output

```
Charset: abcdef
Length range: 3-4
Total combinations: 252
Saving to: wordlist.txt
Generated: 100,000 passwords (50000/sec)
Completed! Generated 252 passwords in 0.01 seconds
Average speed: 25200 passwords/second
```

## Security Considerations

- Be aware that generating large wordlists can consume significant disk space
- Some character sets and length combinations can generate billions of passwords
- Use the `-c` option to limit generation when testing
- Consider the time and storage requirements before generating large wordlists

## License

This tool is for educational and authorized security testing purposes only.
