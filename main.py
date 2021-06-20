import asai_conversion

def get_input():
  get_string = input("Enter your string: ")
  if(get_string == "exit"):
    exit()
  else:
    get_asai = asai_conversion.get_characters(get_string)
    print(str(get_string)+ ": "str(get_asai))
    get_input()
    
if __name__ == "__main__":
  get_input()
