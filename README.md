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


#### Install Jupyter Lab

   + Windows
     ```
     py -m pip install jupyterlab
     ```
   + Mac and Linux
     ```
     python3 -m pip install jupyterlab
     ```

          
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
     py -m ipykernel install --user --name .venv --display-name "Python (tp-decoding)"
     ```
   + Mac and Linux
     ```
     python3 -m ipykernel install --user --name .venv --display-name "Python (tp-decoding)"
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


## 🗒️ Open the Notebook

+ Open Jupyter Lab using the shortcut installed on your system.
+ A web page should open with a file browser on the left, navigate to the folder where you downloaded the project.
+ Open `notebook.ipynb` by double clicking on it
+ Check that the correct environment is set up
  ![jupyter_kernel](https://github.com/gaheldev/tp-decoding/assets/78329601/9fb9795b-1591-49a4-a021-3b15149ae07e)

   ➡️ **You're ready to start !**

<br> <br/>

---
## ⌨️ Development

#### Git cheatsheet

| Task | Command |
| --- | :---: |
| View your current modifications | `git status` |
| Remove changes made to a file | `git checkout <file-path>` |
| Remove all changes since last commit | `git checkout .` |
| Remove changes interactively | `git checkout -p` |
| Add a file to your changes you'd like to commit | `git add <file-path>` |
| Add changes to commit interactively | `git add -p` |
| Commit your changes | `git commit -m "<commit-message>"` |
| Get the last changes from the remote repository | `git pull` |
| Push your changes to the remote repository | `git push` |


#### Manage dependencies

When installing new python packages through pip, add them to the `requirements.txt` file with:
```
python3 -m pip freeze > requirements.txt
```
