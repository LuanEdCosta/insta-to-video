from os import path

def create_env_file(file_name: str):
  if(path.exists(file_name)):
    print("The {0} file already exists. Delete it and run the setup again.".format(file_name))
    return

  username = input("Instagram Username: ")
  password = input("Instagram Password: ")

  with open(file_name, "w") as file:
      file.write("INSTAGRAM_USERNAME={0}".format(username))
      file.write("\n")
      file.write("INSTAGRAM_PASSWORD={0}".format(password))

if __name__ == "__main__":
  create_env_file(".env")
