#  Copyright 2020-2022 Robert Bosch GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# --------------------------------------------------------------------------------------------------------------
#
#  PrepareExamples.py
#
#  15.12.2021
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import sys, os
from dotdict import dotdict

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.Utils.CUtils import *

# --------------------------------------------------------------------------------------------------------------

oData = 4
PrettyPrint(oData)
oData = 6.8
PrettyPrint(oData)
oData = "ABC"
PrettyPrint(oData)
oData = True
PrettyPrint(oData)
oData = None
PrettyPrint(oData)

print()

oData = {}
oData['K1'] = 4
oData['K2'] = 6.8
oData['K3'] = "ABC"
oData['K4'] = True
oData['K5'] = None
PrettyPrint(oData)

print()

oData = dotdict(oData)
PrettyPrint(oData)

print()

oData = [4, 6.8, "ABC", True, None]
PrettyPrint(oData)
oData = (4, 6.8, "ABC", True, None)
PrettyPrint(oData)
oData = {4, 6.8, "ABC", True, None}
PrettyPrint(oData)

print()

listData = [1, "A"]
dictData = {}
dictData['K1'] = 2
dictData['K2'] = [3, 'B', (4.5, 'X', False, None)]
dotdictData = dotdict(dictData)
oData = [6, listData, dictData, dotdictData, None]
PrettyPrint(oData)

print()

oData = [4, 6.8, "ABC", True, None]
PrettyPrint(oData, nIndent=2, sPrefix="--PREFIX--")

print()

oData = [4, 6.8, "ABC", True, None, ("A", "B"), ["DE", "FGH"], {"KA":4, "KB":6.8, "KC":"ABC", "KD":True, "KE":None, "KF":[1, "MNO"]}]
PrettyPrint(oData, nIndent=2, sPrefix="--HEX OUTPUT--", bHexFormat=True)




