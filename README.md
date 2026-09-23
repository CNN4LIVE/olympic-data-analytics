# 🥇 Olympic Games Data Analytics & Dashboard

Ein End-to-End-Datenanalyseprojekt zur Auswertung historischer Daten der Olympischen Spiele (1896 – Heute) unter Nutzung von **Python**, **PostgreSQL**, **SQL** und **Streamlit**.

---

## 📌 Projektübersicht

Dieses Projekt umfasst die vollständige Datenpipeline:
1. **Datenbereinigung & ETL**: Extrahieren, Bereinigen und Laden von Rohdaten (CSV) in eine relationale PostgreSQL-Datenbank.
2. **Datenmodellierung**: Relationales Schema mit Primär- und Fremdschlüsseln für Athleten, Ereignisse, Disziplinen und Länder.
3. **SQL-Analyse**: Komplexe analytische Queries zur Auswertung von Medaillenspiegeln, Altersstrukturen und Geschlechterentwicklung.
4. **Interaktives Dashboard**: Visualisierung der Ergebnisse in einem Streamlit-Dashboard mit Plotly-Diagrammen.

---

## 🛠️ Tech Stack & Werkzeuge

* **Sprachen**: Python 3.14+, SQL
* **Datenbank**: PostgreSQL 16+ / pgAdmin 4
* **Python Bibliotheken**:
  * `pandas` & `sqlalchemy` (Datenverarbeitung & DB-Anbindung)
  * `psycopg2-binary` (PostgreSQL Treiber)
  * `streamlit` & `plotly` (Dashboard & Visualisierung)
* **IDE & Tools**: Visual Studio Code, Git & GitHub

---

## 📁 Projektstruktur

```text
olympic-data-analytics/
│
├── data/                  # Rohdaten (athlete_events.csv, noc_regions.csv)
├── sql/                   # SQL-Skripte
│   ├── 01_schema.sql      # Datenbank-Schema & Tabellen
│   └── 02_queries.sql     # Analytische SQL-Abfragen
├── src/                   # Python-Quellcode (ETL & DB)
│   ├── db_connection.py   # PostgreSQL Verbindungs-Setup
│   ├── create_tables.py   # Tabellen-Erstellung via SQLAlchemy
│   └── load_data.py       # ETL-Pipeline zur Befüllung der DB
├── dashboards/            # Visualisierung
│   └── app.py             # Streamlit Dashboard App
├── docs/                  # Dokumentation & ERD-Diagramm
│   └── erd.md             # Entity Relationship Diagramm
├── .gitignore
├── requirements.txt
└── README.md