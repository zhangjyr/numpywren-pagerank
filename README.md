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
