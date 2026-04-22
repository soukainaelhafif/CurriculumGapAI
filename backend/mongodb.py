from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["curriculumgapai"]

jobs_collection = db["jobs"]
logs_collection = db["logs"]

def save_jobs(jobs_data, keyword):
    document = {
        "keyword": keyword,
        "jobs": jobs_data,
        "anzahl": len(jobs_data) if jobs_data else 0
    }
    jobs_collection.insert_one(document)
    print(f"Jobs gespeichert in MongoDB!")

def save_log(datei_name, gap, matching):
    log = {
        "datei": datei_name,
        "fehlende_skills": gap,
        "vorhandene_skills": matching
    }
    logs_collection.insert_one(log)
    print(f"Log gespeichert!")

if __name__ == "__main__":
    test = {"test": "MongoDB funktioniert"}
    logs_collection.insert_one(test)
    print("MongoDB verbunden und getestet!")