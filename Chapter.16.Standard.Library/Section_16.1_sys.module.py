import sys, warnings
if sys.version_info.major < 3:
        warnings.warn("Need python 3.0 for this program to run", \
                        RuntimeWarning)
else:
        print('Proceed as normal')
