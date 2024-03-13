# ECoG decoding workshop

## ⚙️ Installation

#### Python

For this workshop you will need a working installation of `python3`.
Mac and Linux already come with `python` preinstalled but not necessarily in the latest versions. Run `python3 --version` in a terminal window to check if you have it.

| System | How to install | Additional documentation |
| ---   |  --- | :---: |
| Windows | Download the installer [here](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe) <br/> ⚠️ make sure to select "Add Python to PATH on the first page of the installer| [doc](https://docs.python.org/3/using/windows.html) |
| Mac | Download the universal installer [here](https://www.python.org/ftp/python/3.12.2/python-3.12.2-macos11.pkg) | [doc](https://docs.python.org/3/using/mac.html) |
| Linux | Use your package manager, eg on Ubuntu: `sudo apt install python3` | - |

#### Download the project

*TODO*: use an archive instead

```
git clone git@github.com:gaheldev/tp-decoding.git
cd tp-decoding
```

#### Set up a virtual environment

We're using a virtual environment to manage packages. Virtual environments allow to install python packages inside the project without messing with system-wise dependencies.
This is a good practice so that each of your python projects are isolated from eachother.

To set up the virtual environment, open a terminal window and follow the steps for your system:

1. Create the virtual environment
   + Windows
      ```
      py -m venv .venv
      ```
   + Mac and Linux
     ```
     python3 -m venv .venv
     ```
2. Activate the virtual environment
   + Windows (cmd.exe)
      ```
     .venv\Scripts\activate.bat
      ```
   + Windows (PowerShell)
      ```
     .venv\Scripts\Activate.ps1
      ```
   + Mac and Linux
     ```
     source .venv/bin/activate 
     ```

3. Make the virtual environment accessible to jupyter notebook
   + Windows
     ```
     py -m ipykernel install --user --name .venv --display-name "Python (venv)"
     ```
   + Mac and Linux
     ```
     python3 -m ipykernel install --user --name .venv --display-name "Python (venv)"
     ```
     
> [!NOTE]
> If you work from a jupyter notebook, you won't need to manually activate the virtual environment anymore, just make sure to select the `Python (venv)` kernel

> [!NOTE]
> If you work from a terminal tab, make sure to activate the virtual environment before working on the project <br/>
> Run `deactivate` in your terminal tab to deactivate the virtual environment

#### Install dependencies

   + Windows
     ```
     py -m pip install -r requirements.txt
     ```
   + Mac and Linux
     ```
     python3 -m pip install -r requirements.txt
     ```

## Run the Jupyter Notebook
