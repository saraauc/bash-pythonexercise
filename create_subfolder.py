import os

# Get a list of all directories in the current directory
directories = [d for d in os.listdir('.') if os.path.isdir(d)]

# Create the 'migration' subfolder in each directory
for dir in directories:
    migration_path = os.path.join(dir, 'migration')
    os.makedirs(migration_path, exist_ok=True)
    #Good
    #pls add here the code that creates files
