# importing required modules
import PyPDF2
import os

""""
real_path = os.path.realpath(__file__)
print(real_path)
dir_path = os.path.dirname(real_path)
print(dir_path)
listOfDir = os.listdir(dir_path)
print(listOfDir)
"""


def findingFiles(word, path = os.path.dirname(os.path.realpath(__file__))):
    walkResult = os.walk(path, topdown=False)
    foundFiles = []
    for root, dirs, files in walkResult:
        for name in files:
            if name.endswith(".pdf"):

                filePath = os.path.join(root, name)
                print("analysing: " + filePath)
                # creating a pdf file object
                pdfFileObj = open(filePath, 'rb')

                # creating a pdf reader object
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                # printing number of pages in pdf file
                #print(pdfReader.numPages)

                pdfText = ""

                for page in range(pdfReader.numPages):
                    # creating a page object
                    pageObj = pdfReader.getPage(page)

                    # extracting text from page
                    # print(pageObj.extractText())
                    pdfText += " " + pageObj.extractText()

                # closing the pdf file object
                pdfFileObj.close()
                pdfText = pdfText.lower()
                if pdfText.find(word.lower()) > -1:
                    foundFiles.append(filePath)
                    print("Key word found in archive: " + filePath)

    if len(foundFiles) > 0:
        print("\n\nFinished! Key word found in following files: ")
        for foundFile in foundFiles:
            print(foundFile)
    else:
        print("\n\nFinished! Not found key word in any file :(")


while True:
    word = input("Type the key word: ")
    path = input("Type the initial directory (or blank to start in the current directory): ")
    # word = "javascript"
    # path = "C:/Users/danie/Documents/Certificados"
    if len(path) > 0:
        findingFiles(word, path)
    else:
        findingFiles(word)
    answer = input("Keep searching?[Y/N] ")
    if answer.lower() != 'y':
        break
