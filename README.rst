.. Copyright 2020-2026 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Package Description
===================

The **PythonExtensionsCollection** extends the functionality of Python by some useful functions
that are not available in Python immediately.

How to install
--------------

The **PythonExtensionsCollection** can be installed in two different ways.

1. Installation via PyPi (recommended for users)

   .. code::

      pip install PythonExtensionsCollection

   `PythonExtensionsCollection in PyPi <https://pypi.org/project/PythonExtensionsCollection/>`_

2. Installation via GitHub (recommended for developers)

   * Clone the **python-extensions-collection** repository to your machine.

     .. code::

        git clone https://github.com/test-fullautomation/python-extensions-collection.git

     `PythonExtensionsCollection in GitHub <https://github.com/test-fullautomation/python-extensions-collection>`_

   * Install and configure dependencies

     The installation of **PythonExtensionsCollection** includes to generate the documentation in PDF format. This is done by
     an application called **GenPackageDoc**, that is part of the installation dependencies.

     **GenPackageDoc** uses **LaTeX** to generate the documentation in PDF format. Therefore, **LaTeX** needs to be installed
     (recommended: TeX Live). After this installation, **GenPackageDoc** needs to know where to find **LaTeX**.
     This is defined in the **GenPackageDoc** configuration file

     .. code::

        packagedoc\packagedoc_config.json

     Before you start the installation you have to introduce the following environment variable, that is used in ``packagedoc_config.json``:

     - ``GENDOC_LATEXPATH`` : path to ``pdflatex`` executable


   * Use the following command to install **PythonExtensionsCollection** (executed in repository main folder):

     .. code::

        python -m pip install .

     In case you want to have a really clean installation (without any outdated or not used files left from previous installations),
     extend the installation to:

     .. code::

        python "./cleanup_installation.py"
        python -m pip install .

     ``cleanup_installation.py`` explicitly deletes all files and folders within the component installation folder under
     ``site-packages`` and also deletes local build artefacts.


Package Documentation
---------------------

A detailed documentation of the **PythonExtensionsCollection** can be found here:
`PythonExtensionsCollection.pdf <https://github.com/test-fullautomation/python-extensions-collection/blob/develop/PythonExtensionsCollection/PythonExtensionsCollection.pdf>`_


Feedback
--------

To give us a feedback, you can send an email to `Thomas Pollerspöck <mailto:Thomas.Pollerspoeck@de.bosch.com>`_

In case you want to report a bug or request any interesting feature, please don't hesitate to raise a ticket.

Maintainers
-----------

`Holger Queckenstedt <mailto:Holger.Queckenstedt@de.bosch.com>`_

`Thomas Pollerspöck <mailto:Thomas.Pollerspoeck@de.bosch.com>`_

Contributors
------------

`Holger Queckenstedt <mailto:Holger.Queckenstedt@de.bosch.com>`_

`Thomas Pollerspöck <mailto:Thomas.Pollerspoeck@de.bosch.com>`_

License
-------

Copyright 2020-2026 Robert Bosch GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    |License: Apache v2|

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


.. |License: Apache v2| image:: https://img.shields.io/pypi/l/robotframework.svg
   :target: http://www.apache.org/licenses/LICENSE-2.0.html
