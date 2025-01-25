# Secure WiFi Password QR Generator

Generates cryptographically secure 64-character WiFi passwords and displays them as scannable QR codes.

## Why

This tool implements cybersecurity best practices for secure password generation and transmission:

### Cryptographic Security
- Uses Python's `secrets` module instead of `random` for cryptographically secure random generation
- Implements multiple randomization passes (7-17 iterations) for enhanced entropy
- Ensures cryptographically secure character selection and shuffling

### Data Security
- Zero persistence - passwords never saved to disk
- Memory-only operation - leaves no traces after execution
- No network connectivity required post-installation
- Air-gapped transfer capability through QR codes
- Minimal attack surface through lightweight codebase

### Password Strength
- 63-character length exceeds standard requirements (the maximum length allowable in both Samsung and iPhone mobile hotspots)
- Enforces character set complexity:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Validates minimum requirements for each character type

### Usability Security
- QR code scanning eliminates manual password entry errors
- Visual confirmation of generated password
- Simple interface reduces user error potential
- Cross-platform compatibility between Windows and mobile devices

## Installation

1. Ensure Python 3.8 or higher is installed
2. Clone this repository:
```bash
git clone https://github.com/Learning-Gen-AI/Cyber_WiFiPasswordGenerator.git
cd Cyber_WiFiPasswordGenerator
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python main.py
```

2. The tool will:
   - Generate a secure 64-character password
   - Display it in the console
   - Show a QR code containing only the password
   - Exit cleanly when window is closed

3. To use the generated password (two options):
   
   Option A - Connecting phone to home WiFi:
   - Copy the password
   - Enter it in your router's settings interface and save
   - Scan the QR code with your mobile device
   - Copy it and use it to connect your phone to your home WiFi

   Option B - Mobile Hotspot:
   - Scan the QR code with your mobile device
   - Copy the password
   - Set it as your mobile hotspot password
   - On the computer, copy the password from the terminal and use it to connect to the mobile hotspot

## Requirements
- Python 3.8+
- Windows 11
- Dependencies listed in requirements.txt

## Security Considerations
- Keep your screen private when displaying the QR code
- Clear your clipboard after copying the password
- Use the tool in a secure environment
- Generate new passwords periodically
- Don't share screenshots of the QR code

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Disclaimer
This tool is provided as-is without any warranties. Users are responsible for their own security practices and should follow their organization's security policies.
