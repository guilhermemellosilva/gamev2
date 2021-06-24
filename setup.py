import cx_Freeze
executables = [cx_Freeze.Executable(script="main.py", icon="assets/midoriya.ico")]
cx_Freeze.setup(
    name="My Hero Academia",
    options={"build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
    }},
    executables = executables
)
