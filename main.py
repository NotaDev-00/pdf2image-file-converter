from pdf2image import convert_from_path
import os
import time

def main():
    # Change the given path of the poppler_path = to the path of the poppler  Library  bin, where you saved the poppler bin folder.
    
    poppler_path = r"F:\Documents\_Personal Files_\__Web-&-App-Projects__\pdf2image_program_\poppler\poppler-22.12.0\Library\bin"
    print("Take Note: Provide the full and correct path, including the filename of the PDF file.")
    
    time.sleep(3)
    
    pdf_path = input(r"Enter PDF File: ")
    
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    
    print("Take Note: Provide the full and correct path of the folder where you wanted to save the image file.")
    
    time.sleep(3)
    
    saving_folder = input(r"Enter Saving Folder: ")
    
    c = 1
    for page in pages:
        img_name = f"converted-{c}.jpeg"
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        c += 1
    #you can change the image type to, jpeg, png, etc.
    
    
main()