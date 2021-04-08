#!/usr/bin/env python

from pathlib import Path
import sys
import os

if len(sys.argv) < 2:
    print("Pool name argument is required.")
    print("Example: `python generate.py usd`")
    exit(1)

poolName = sys.argv[1]

templatePath = Path('./contracts/pool-templates/base/SwapTemplateBase.vy')
sourceCode = open(templatePath).read()

poolDir = Path('./contracts/pools').joinpath(poolName)
if not os.path.exists(poolDir):
    print("Pool directory not exist: ", poolDir)
    exit(1)

targetContractPath = poolDir.joinpath('StableSwap' + poolName.upper() + ".vy")

exec(open("brownie_hooks.py").read())

poolFile = open(targetContractPath, 'w')
poolFile.write(brownie_load_source(templatePath, sourceCode))
poolFile.close()

print("Success")
print("Pool contract generated at: ", targetContractPath)
