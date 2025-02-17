import pyzipper
import hashlib

def create_zip_with_password(file_name, password):
    with pyzipper.AESZipFile(file_name, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode('utf-8'))
        zipf.write('secret.txt', arcname='secret.txt')

def calculate_hash(name):
    return hashlib.md5(name.encode('utf-8')).hexdigest()

def main():
    with open('ListOfNames.txt', 'r') as names_file:
        names = names_file.read().splitlines()

  for name in names:
        password = calculate_hash(name)
        zip_file_name = f"{name}.zip"
        create_zip_with_password(zip_file_name, password)
        print(f"Name of file:-  {zip_file_name} Password is :- {password}")
if __name__ == "__main__":
    main()
