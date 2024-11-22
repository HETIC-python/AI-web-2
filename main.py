import upload

def main(url):
    file_name = upload.get_cloud_docs.get_cloud_docs(url)
    try:
        if file_name.endswith(".txt"):
            print("find")
            upload.upload_txtfile(file_name)
        elif file_name.endswith(".json"):
            upload.upload_jsonfile(file_name)
        elif file_name.endswith(".pdf"):
            upload.convert_pdf_to_text(file_name)
        else:
            print("File type not supported.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main("__________")  # Insert a URL to a file you want to download and process

    #https://fr.getsamplefiles.com/download/txt/sample-1.txt
    #https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf