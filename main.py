import upload
from get_cloud_docs import get_cloud_docs

def main(url):
    file_name = get_cloud_docs(url)

    if file_name.endswith(".txt"):
        upload.upload_txtfile(file_name)
    elif file_name.endswith(".json"):
        upload.upload_jsonfile(file_name)
    elif file_name.endswith(".pdf"):
        upload.convert_pdf_to_text(file_name)
    else:
        print("File type not supported.")

if __name__ == "__main__":
    main("https://www.inegalites.fr/IMG/pdf/note_n9_-_revenus_dans_le_monde_-_observatoire_des_inegalites.pdf")