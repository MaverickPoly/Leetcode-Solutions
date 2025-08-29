# Running Python script
Write-Host "Running pre-push Python script..."
python .\Scripts\move_file.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Python script failed. Aborting push."
    exit 1
}

# Git Stuff
Write-Host "Staging changes..."
git add .

$commitMsg = Read-Host "Enter commit message"

Write-Host "Committing..."
git commit -m "$commitMsg"

Write-Host "Pushing to Github..."
git push origin main

Write-Host "✅ Push completed!"
