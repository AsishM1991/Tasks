message = " Welcome To Python Programming Class "

clean_message=message.strip()
print("Remove Extra spaces: " , clean_message)
print("Type in Lower case: " , clean_message.lower() )
print("Type in Upper case: " , clean_message.upper() )
print("Convert to Title Case: ", clean_message.title() )
print("Replace Python with Advance Python: ", clean_message.replace("Python","Advance Python"))
print("Check Welcome id the First word? : " , clean_message.startswith("Welcome"))
print("Check class is the last word ? :" , clean_message.endswith("Class"))
print("Count occurabnce of o :" , clean_message.count("o"))
print("Find the position of programming :" , clean_message.find("Programming"))
print("Split Words : " , clean_message.split())