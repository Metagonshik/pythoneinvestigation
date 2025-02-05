import PyPDF2
import json

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        pages = {}
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            
            # Добавляем текст страницы в словарь
            pages[f'Page {page_num+1}'] = text.strip()
        
        return pages

def save_as_json(data, json_path):
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    pdf_path = 'your_pdf_file.pdf'
    json_path = 'extracted_data.json'
    
    extracted_pages = extract_text_from_pdf(pdf_path)
    save_as_json(extracted_pages, json_path)
    
    print(f"Данные из PDF-файла успешно собраны и сохранены в {json_path}.")