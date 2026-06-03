# Virtual Environments and Packages - Simplified Explanation

This chapter explains how to isolate Python projects so that each can have its own set of packages, avoiding version conflicts.



## 12.1. Introduction: The Problem of Conflicting Requirements

Different Python projects often need different versions of the same library. For example:

- Project A requires `requests` version 1.0
- Project B requires `requests` version 2.0

Installing both globally is impossible because they conflict. The solution is to create **virtual environments**—isolated Python installations where each project can have its own packages.



## 12.2. Creating Virtual Environments with `venv`

The `venv` module creates a self-contained directory with its own Python interpreter and package folder.

### Create a Virtual Environment

```bash
python -m venv tutorial-env
```

This creates a directory named `tutorial-env` containing a fresh Python installation. A common naming convention is `.venv` (hidden on Unix-like systems).

### Activate the Virtual Environment

**Windows:**
```cmd
tutorial-env\Scripts\activate
```

**Unix / macOS (bash):**
```bash
source tutorial-env/bin/activate
```

After activation, your terminal prompt changes to show the environment name. Running `python` now uses the isolated interpreter.

**Example:** Check the `sys.path` inside an activated environment—it includes the environment's `site-packages` directory.

```python
import sys
print(sys.path)
# ['', '/usr/local/lib/python35.zip', ..., '~/envs/tutorial-env/lib/python3.5/site-packages']
```

### Deactivate

To exit the virtual environment, simply run:

```bash
deactivate
```


## 12.3. Managing Packages with `pip`

`pip` is the package installer for Python. It downloads packages from the Python Package Index (PyPI).

### Install a Package (Latest Version)

```bash
python -m pip install novas
```

### Install a Specific Version

```bash
python -m pip install requests==2.6.0
```

### Upgrade a Package to the Latest Version

```bash
python -m pip install --upgrade requests
```

### Uninstall a Package

```bash
python -m pip uninstall requests
```

### Show Package Information

```bash
python -m pip show requests
```

Output includes version, author, license, and installation location.

### List All Installed Packages

```bash
python -m pip list
```

Example output:
```
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

### Freeze Dependencies for Reproducibility

`pip freeze` outputs installed packages in a format that `pip install` can read. It's common to save this list to `requirements.txt`.

```bash
python -m pip freeze > requirements.txt
cat requirements.txt
```

Content example:
```
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

### Install from a Requirements File

Anyone can recreate the same environment using:

```bash
python -m pip install -r requirements.txt
```

This installs all packages at the specified versions.


## Summary

- **Virtual environments** isolate project dependencies.
- Create one with `python -m venv <name>`.
- Activate it with `source <name>/bin/activate` (Unix/macOS) or `<name>\Scripts\activate` (Windows).
- Use `pip install` to add packages, `pip list` to see them, and `pip freeze` to export the list.
- Use `requirements.txt` to share and replicate environments.


## Confirmation of Coverage

| Section | Covered |
|---------|---------|
| 12.1 Introduction (conflict problem) | Yes |
| 12.2 Creating Virtual Environments | Yes |
| 12.3 Managing Packages with pip (install, upgrade, uninstall, show, list, freeze, requirements.txt) | Yes |

The explanation is complete, uses simple language with practical examples, and is formatted in clean Markdown without emojis.