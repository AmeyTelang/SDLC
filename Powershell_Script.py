import subprocess

powershell_32 = r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe"
ps_script = r"Test-Login-CurrentUser.ps1"
#exe_path = r"C:\Users\KPunjab1\Downloads\ConsoleApp1\ConsoleApp1\bin\debug\ConsoleApp1.exe"

command = [
    powershell_32,
    "-NoProfile",
    "-ExecutionPolicy","ByPass",
    "-File",ps_script
]

result = subprocess.run(command,capture_output=True,text=True)
#result = subprocess.run(exe_path,capture_output=True,text=True)

print("STDOUT:")
print(result.stdout)

print("STDERR:")
print(result.stderr)