# Translation function: Converts custom language to Python
def translate_to_python(native_code):
    translation = native_code.replace("ถ้า", "if")
    translation = translation.replace("ไม่ใช่แล้ว","elif")  
    translation = translation.replace("ทั้งหมด","else")       # 'if'
    translation = translation.replace("เป็น", "==")       # '=='
    translation = translation.replace("ไม่", "else")      # 'else'
    translation = translation.replace("แสดงผล", "print")
    translation = translation.replace("ระหว่าง", "for") # 'print'
    translation = translation.replace("ใน", "in")
    translation = translation.replace("ช่วง", "range")
    translation = translation.replace("น้อยกว่า", "<")
    translation = translation.replace("มากกว่า", ">")
    translation = translation.replace("รับค่า", "input")
    translation = translation.replace("จำนวนเต็ม", "int")
    translation = translation.replace("ข้อความ", "str")
    translation = translation.replace("ให้", ":")

    return translation

# Read the code from a file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Run the translated code from the file
def run_native_file(filename):
    # Read the code from the file
    native_code = read_file(filename)
    
    # Translate the code into Python syntax
    python_code = translate_to_python(native_code)
    
    # Execute the translated Python code
    exec(python_code)




run_native_file('สวัสดี.ty')
