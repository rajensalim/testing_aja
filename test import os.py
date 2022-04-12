import os
import shutil
# Define root directory
root_dir = '/tmp/cats-v-dogs'

# Empty directory to prevent FileExistsError is the function is run several times
if os.path.exists(root_dir):
  shutil.rmtree(root_dir)

# GRADED FUNCTION: create_train_test_dirs
def create_train_test_dirs(root_path):
  ### START CODE HERE
  os.makedirs(os.path.join(root_path, 'training'))
  os.makedirs(os.path.join(root_path, 'testing'))
  os.makedirs(os.path.join(root_path, 'testing', 'cats'))
  os.makedirs(os.path.join(root_path, 'testing', 'dogs'))
  os.makedirs(os.path.join(root_path, 'training', 'cats'))
  os.makedirs(os.path.join(root_path, 'training', 'dogs'))

  # HINT:
  # Use os.makedirs to create your directories with intermediate subdirectories
  # Don't hardcode the paths. Use os.path.join to append the new directories to the root_path parameter

  pass

  ### END CODE HERE

  
try:
  create_train_test_dirs(root_path=root_dir)
except FileExistsError:
  print("You should not be seeing this since the upper directory is removed beforehand")