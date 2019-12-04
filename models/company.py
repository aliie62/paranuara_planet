import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import get_one_document, save_documents, get_documents

class Company(object):
    
    @staticmethod
    def find_by_name(name:str):
        company = get_one_document('company',{'company':name.upper()})
        if company:
            index = company['index']
            employees_docs = get_documents('people',{'company_id':index})
            employees = [{"index":employee['index'], "name":employee['name']} for employee in employees_docs]
            return {"company": company['company'],"employees":employees}
        else:
            return company