# 🧪 PubMed Paper Fetcher

## 📌 Overview
This project is a **Python command-line tool** that fetches research papers from **PubMed** based on a user-specified query. It filters papers that have at least one author affiliated with a **pharmaceutical or biotech company** and returns the results as a CSV file.

---

## 🚀 Features
✅ Fetches research papers from the **PubMed API**  
✅ Filters papers with **non-academic (company-affiliated) authors**  
✅ Saves results in a **CSV file** or prints them to the console  
✅ Supports **PubMed’s full query syntax**  
✅ Command-line tool with options for **debugging and output file naming**  

---

## 🛠 Installation

 **1️⃣ Clone the Repository**
```sh
   git clone https://github.com/your-username/PubMedPaperFetcher.git
   cd PubMedPaperFetcher
```
**2️⃣ Install Dependencies Using Poetry**
Make sure you have Python 3.10+ and Poetry installed. Then run:
```sh
   poetry install
```
If you don't have Poetry installed, install it first:
```sh
   pip install poetry
```

**🎯 Usage**
Basic Command (Print to Console)
```sh
   python cli.py "cancer treatment"
```
Save Output to CSV
```sh
   python cli.py "cancer treatment" -f results.csv
```
Enable Debug Mode
```sh
   python cli.py "cancer treatment" -d
```
View Help Options
```sh
   python cli.py --help
```

**📝 How It Works**
1. The program fetches research papers from PubMed using the Entrez API.
2. It filters out non-academic authors by identifying pharma/biotech company affiliations.
3. The filtered data is printed to the console or saved in a CSV file.

**🛠 Tools & Technologies**
1. Python 3.10+
2. PubMed Entrez API (NCBI)
3. Poetry (Dependency management)
4. Git & GitHub (Version control)
