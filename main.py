import asai_conversion

def get_input():
  get_string = input("Enter your string: ")
  if(get_string == "exit"):
    exit()
  else:
    get_asai = asai_conversion.word_convert(get_string)
    print("Given string asai is : " +str(get_asai))
    get_input()
    
if __name__ == "__main__":
  get_input()
