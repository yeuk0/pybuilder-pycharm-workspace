#   Copyright 2020 Diego Barrantes
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pybuilder.core import Author, use_plugin


use_plugin('python.core')
use_plugin('python.distutils')

name = 'pybuilder-pycharm-workspace'
version = '0.1.2'
license = "Apache License, Version 2.0"

authors = [Author("Diego BM", 'diegobm92@gmail.com')]
url = 'https://github.com/yeuk0/pybuilder-pycharm-workspace'
description = "External plugin for PyBuilder integration with PyCharm"
long_description = f"Visit {url} for more information"
summary = "PyBuilder PyCharm Workspaces Plugin"

default_task = ['clean', 'publish']
