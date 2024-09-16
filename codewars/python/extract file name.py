# Title: extract file name
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# You have to extract a portion of the file name as follows:
# Assume it will start with date represented as long number
# Followed by an underscore
# Youll have then a filename with an extension
# it will always have an extra extension at the end
# Inputs:
# 1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
# 1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
# 1231231223123131_myFile.tar.gz2
# Outputs
# FILE_NAME.EXTENSION
# This_is_an_otherExample.mpg
# myFile.tar
# Acceptable characters for random tests:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789
# The recommend way to solve it is using RegEx and specifically groups.
#
## Solution ##
import re
class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        reg1 = "^\d*_"
        reg2 = "\.{1}(\w|-)*$"
        
        res1 = re.sub(reg1, "", dirty_file_name)
        res2 = re.sub(reg2, "", res1)
        
        return res2
        
## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"),"FILE_NAME.EXTENSION")
Test.assert_equals(FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"),"FILE_NAME.EXTENSION")