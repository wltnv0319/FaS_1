# ZIP 파일 파싱 프로그램 (내부파일명 / 파일의 데이터 시작 offset / 데이터 저장)

import os
import sys


# 파일 열기
zipfile = open("/Users/wltnv/Desktop/TEST.zip", 'rb')

# offset찾기
zipfile.seek(-12,2)
file_number = zipfile.read(2)
number = (int.from_bytes(file_number, byteorder="little"))
zipfile.seek(0)


# 파일 수만큼 반복하여 정보 찾기 (이름, offset)
for i in range(0, number):
    if i == 0:
        Local_Header = zipfile.read(18)
    if i != 0:
        Local_Signature = zipfile.read(4)
        if(Local_Signature[0] == 0x50 and Local_Signature[1] == 0x4B and Local_Signature[2] == 0x03 and Local_Signature[3] == 0x04):
            Local_Header = zipfile.read(14)
        else:
            break
    
    Compresse_Size = zipfile.read(4)
    Data_Size = (int.from_bytes(Compresse_Size, byteorder="little"))
    
    Uncompressed_Size = zipfile.read(4)
    
    Name_Size = zipfile.read(2)
    Name_Size_int = (int.from_bytes(Name_Size, byteorder="little"))
    
    Extra_Field_Size = zipfile.read(2)
    Extra_Field_Size_int = (int.from_bytes(Extra_Field_Size, byteorder="little"))
    
    File_Name = zipfile.read(Name_Size_int)
    print("File ", (i+1), " Name : ", File_Name)
    
    Data_Offset = zipfile.tell()
    print("File ", (i+1), " Offset : ", hex(Data_Offset))
    
    Data = zipfile.read(Data_Size)
    
    Extra_Field = zipfile.read(Extra_Field_Size_int)
    
    
    
# 데이터 저장
zipfile.seek(0,0)
zipfile.seek(45)
File_1 = zipfile.read(26)

File_One = open("Programmning.txt", 'wb')
File_One.write(File_1)


zipfile.seek(0,0)
zipfile.seek(110)
File_2 = zipfile.read(6)

File_One = open("Programmning.txt", 'wb')
File_One.write(File_2)


zipfile.seek(0,0)
zipfile.seek(154)
File_3 = zipfile.read(17)

File_One = open("Programmning.txt", 'wb')
File_One.write(File_3)
    
    
    
    
    
    
    
    
    
    