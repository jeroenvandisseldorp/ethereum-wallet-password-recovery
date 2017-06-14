# ethereum-wallet-password-recovery

I found pyethrecover a mess to run, but figured out a way to do without, using the geth command line tool.
My case required scanning the permutations of possible passwords as supported by pyethrecover.

Two scripts provided:
- generate.py: derived from pyethrecover, this script generates permutations of passwords.
- run.sh checks those passwords using the geth command line tool and stops as soon as the password is found.

Usage:

First, adjust generate.py to contain the permutations you want. Then run
`python generate.py > pass.txt`

After that you can use the other script to test all possible passwords:
`run.sh`

After only 10 minutes I found my own password using a generated list of +- 2000 passwords, so 
I'd thought I'd share the mechanism for others to benefit. Happy password hunting!
