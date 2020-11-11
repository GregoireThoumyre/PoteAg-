from cx_Freeze import setup, Executable

setup(
    name="MonPoteAge",
    version="0.1",
    description="Appli potager",
    executables=[Executable('MonPoteAge.py')]
)