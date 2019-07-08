# persistry-python

![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

Persistry is a tool for analyzing and visualizing the registry information of autoruns program(sysinternals) and malware frequently uses.

*This tool is a solution to the IR200 issue of Digital Forensic Challenge(a.k.a. DFC) 2019 in Korea.*

## Requirements
```bash
apt-get install python3
pip3 install pyregf
```

## Usage
```bash
python3 runner.py [hives path]
```
'hive path' refers to the folder for the Windows registry hive set. 

For example, the hive path should contain the following files (but all files are not required):

```
SYSTEM
SOFTWARE
SAM
SECURITY
DEFAULT
NTUSER.DAT
USERCLASS.DAT
```

## Security

If you discover any security related issues, please email [`extr3.0@gmail.com`](mailto:extr3.0@gmail.com) instead of using the issue tracker.

## License

The MIT License (MIT). Please see [`LICENSE`](./LICENSE) for more information.

