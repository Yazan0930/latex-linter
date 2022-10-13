
@REM create a folder for the installation files
mkdir C:\Program bin

cd bin

@REM pull code from github "https://github.com/Yazan0930/latex-linter" to the folder
git clone https://github.com/Yazan0930/latex-linter

@REM add the folder to the path
setx path "%path%;C:\Program bin"

@REM add to .profile
echo "export PATH=$PATH:C:\Program Files\bin" >> ~/.profile

@REM add to .zshrc
echo "export PATH=$PATH:C:\Program Files\bin" >> ~/.zshrc

@REM create alias latex-linter to index.py
echo "alias latex-linter='python C:\Program Files\bin\index.py'" >> ~/.profile

@REM  reload bash profile
source ~/.profile

@REM give permission to execute index.py
chmod +x C:\Program Files\bin\index.py

@REM  reload bash profile
source ~/.profile