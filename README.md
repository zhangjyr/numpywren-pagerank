# numpywren-pagerank

## usage:
 - configure AWS credentials
 - install pywren, configure and test with `pywren test_function`
 - install numpywren
 - run numpywren-test.py to test matrix mul
## issues:
 - [x] pywren returns "AccessDenied" on test
    - check your pywren bucket access settings
    - **fix**: use 'us-west-2' config, other runtime buckets don't exist or are private
 
 - [ ] when using numpywren, pywren raises exception on Lambda: `No module named 'aiobotocore'`
    - numpywren excludes all site packages from pywren executor (`numpywren/binops.py`, Line 161)
    - if we remove include, Lambda returns excpetion `No space left on device`
    - tried patching pywren to ignore aiobotocore when removing imports. Still requires `async_generator`. After including that again `No space left on device` (see `executor.py`, `swap.sh`)
    - **possible solution**: build our own pywren runtime with only the libraries we need
    - **fix**: use following config for pywren:
      ```
      runtime:
              s3_bucket: numpywrenpublic
              s3_key: pywren.runtime/pywren_runtime-3.6-numpywren.tar.gz
        ```

## deployment

1. Configure AWS credentials
2. Install pywren (python >= 3.6, but 3.6 is a safe choice)
   ```
   pip3.6 install pywren --user
   ```
   1. Config pywren with `pywren-setup`.
   2. If your aws account id is start with 0, try fix pywren/wrenconfig.py with my version as https://github.com/zhangjyr/pywren/blob/master/pywren/wrenconfig.py#L56
      1. Resume setup with `pywren deploy_lambda`
      2. Run `pywren test_function`
3. Install numpywren using source code.
   1. Run `sudo python3.6 setup.py build`
   2. Run `sudo python3.6 setup.py install`
   3. Modify codes in numpywren/matrix*.py (usually located in /usr/local/lib/python3.6/site-packages/numpywren-0.0.1a0-py3.6.egg/), change
      ```
      xxx.get_session(loop=loop)
      to
      xxx.get_session()
      ```
   4. Modify codes in numpywren/binops.py (Line 161), change
      ```
      futures = pwex.map(pywren_run, c, exclude_modules=["site-packages"])
      to
      futures = pwex.map(pywren_run, c)
   5. Optional, if you want to optimize pwex.map performance later, also in pywren/executor.py (Line 231), add
      ```
      print(mod_paths)
      ```
   6. Manually repackage lambda function as in https://docs.aws.amazon.com/lambda/latest/dg/python-package.html . Add package boto3=1.12.15, botocore=1.15.15, aiohttp, wrapt, astor. Or execute, and upload to lambda.
      ```
      mkdir lambda
      cd lambda
      cp ~/.local/lib/python3.6/site-packages/pywren/wrenutil.py ./
      cp ~/.local/lib/python3.6/site-packages/pywren/wrenconfig.py ./
      cp ~/.local/lib/python3.6/site-packages/pywren/wrenhandler.py ./
      cp ~/.local/lib/python3.6/site-packages/pywren/version.py ./
      cp ~/.local/lib/python3.6/site-packages/pywren/jobrunner/jobrunner.py ./
      cp ~/.local/lib/python3.6/site-packages/pywren/wren.py ./
      mkdir package
      pip3.6 install --upgrade --target ./package boto3==1.12.15
      pip3.6 install --upgrade --target ./package botocore==1.15.15
      pip3.6 install --upgrade --target ./package aiohttp
      pip3.6 install --upgrade --target ./package wrapt
      pip3.6 install --upgrade --target ./package astor
      cd package
      zip -r9 ${OLDPWD}/function.zip .
      cd $OLDPWD
      zip -g function.zip *.py
      ```
4. Run numpywren-test.py to test matrix mul, add packages (numpy, scipy, cloudpickle...) if necessary
   ```
   python3.6 test/numpywren-test.py
   ```
5. For performance, package all dependencies shown in log (see 3.v) to lambda (see 3.vi), and undo 3.iv
