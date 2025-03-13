import requests
import pandas as pd
import re
from typing import List, Dict, Any

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Fetches PubMed papers based on a query.
    Returns a list of paper details.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
    }
    
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Fetches detailed paper information from PubMed.
    """
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json",
    }
    
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    papers = []
    
    for paper_id in paper_ids:
        paper_info = data["result"].get(paper_id, {})
        authors = paper_info.get("authors", [])
        
        # Extract company affiliations
        non_academic_authors, company_affiliations = extract_company_authors(authors)
        
        papers.append({
            "PubmedID": paper_id,
            "Title": paper_info.get("title", "Unknown"),
            "Publication Date": paper_info.get("pubdate", "Unknown"),
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": extract_email(authors),
        })
    
    return papers

def extract_company_authors(authors: List[Dict[str, str]]) -> (List[str], List[str]):
    """
    Extracts non-academic authors and their company affiliations.
    """
    non_academic = []
    companies = []

    for author in authors:
        affiliation = author.get("affiliation", "").lower()
        if affiliation and not re.search(r"university|college|institute|lab", affiliation):
            non_academic.append(author.get("name", "Unknown"))
            companies.append(affiliation)
    
    return non_academic, companies

def extract_email(authors: List[Dict[str, str]]) -> str:
    """
    Extracts the email of the corresponding author if available.
    """
    for author in authors:
        if "@" in author.get("affiliation", ""):
            return author.get("affiliation", "")
    return "Not Available"

def save_to_csv(papers: List[Dict[str, Any]], filename: str):
    """
    Saves the list of papers to a CSV file.
    """
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")
