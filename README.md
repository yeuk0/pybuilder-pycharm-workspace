# PyBuilder PyCharm Workspace Plugin

This plugin setups all the necessary configurations to start a new PyCharm project. It sets:

* New Python Interpreter based on `venv/` directory (this virtual environment will be set as project default
 interpreter and should be created before using PyBuilder for the first time)
* New `.idea/` directory to store PyCharm metadata files
  * Custom `.idea/{project_name}.iml` file with project info (previously created Python Interpreted)
  * `.idea/misc.xml` file with Python Interpreter info
  * `.idea/modules.xml` file with IML file name and location
  * `.idea/workspace.xml` with some running configurations ready to be used with virtual environment created to ease
   PyBuilder tasks launching

## How to use pybuilder_pycharm_workspace

> **NOTICE**: This plugin was developed and tested for PyCharm 2019 for Windows only. Using this plugin in other OS
> shall not work properly. Multi-platform support soon.

Add plugin dependency to your `build.py`:

```python
use_plugin('pypi:pybuilder_pycharm_workspace')
```

Configure the plugin within your `init` function:

```python
@init
def initialise(project):
    project.set_property('pycharm_workspace_main_version', '2019')
    project.set_property('pycharm_workspace_project_path', project_path)
```

This will tell the plugin what version of PyCharm will be used to work with the project and which is the project
 location in the filesystem. `pycharm_workspace_project_path` property value should be always the same.

Launch the task with:

```console
(venv) C:\Users\foo\PycharmProjects\bar> pyb_ pycharm_workspace_generate
```

It's recommended to keep PyCharm closed during `pycharm_workspace_generate` task execution to force PyCharm's
 indexing process in order to load new interpreter configuration properly once you open the project .

Not doing this may cause the new interpreter not being recognised by the IDE.

### `build.py` file recommended

This plugin creates some running profiles to use with PyCharm to ease the launching of some common building
 configurations. This implies the need of some custom add-ons on your `build.py` file. As this plugin doesn't include
  this file due to there should be already one at the moment of the execution of `pyb` command, the following template
   can be used along this plugin. Modify as desired.

```python
from pathlib import Path

from pybuilder.core import use_plugin, init, Author


use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')

use_plugin('pypi:pybuilder_pycharm_workspace')

project_path = Path(__file__).resolve().parent

name = project_path.name
authors = [Author("foo", 'bar')]
license = "Apache License, Version 2.0"
version = '1.0.0'


@init
def initialise(project):
    project.set_property('pycharm_workspace_project_path', project_path)


# Most important part of the script below (previous one is just filling code)
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'pycharm_builder':
        from subprocess import run

        pyb_command = ['pyb_'] + sys.argv[2:]
        run(pyb_command)  # Add more complexity here as desired
    else:
        print("Nothing to do here")
```

## Properties

Plugin has next properties with provided defaults

| Name | Type | Default Value | Description |
| --- | --- | --- | --- |
| pycharm_workspace_main_version | string | 2019 | Main version of the PyCharm used to work with the project
| pycharm_workspace_project_path | Path | None | Project's path in filesystem (same as `build.py` file). Mandatory |
