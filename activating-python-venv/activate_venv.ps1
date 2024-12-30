# Define the path to your virtual environment folder
$venvPath = "C:\path\to\venv"  # Modify this path to point to your actual venv directory

# Check if the venv folder exists
if (Test-Path "$venvPath\Scripts\Activate.ps1") {
    # Change directory to the project directory
    Set-Location "$venvPath\..\"
    # Activate the virtual environment
    Write-Host "Activating virtual environment..."
    PowerShell -NoExit "$venvPath\Scripts\Activate.ps1"
} else {
    Write-Host "Virtual environment not found at $venvPath"
    Read-Host -Prompt "Press any key to continue "
}
