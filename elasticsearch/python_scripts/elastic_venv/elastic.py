from elasticsearch import Elasticsearch

CERT_FINGERPRINT = "1C:AD:BA:B4:D0:17:78:F4:C4:74:19:EF:86:5E:7B:80:36:18:1C:6D:81:10:F5:EC:C8:5E:52:AC:AA:35:94:FD"
api_key = "czdsUmVaWUJvZXpNOHl5UFJJMzE6YlFGWTU3cWp0bkY2YmRLbjV1R2FhUQ=="
client = Elasticsearch(
    "https://172.31.31.246:9200",
    ca_certs = "certs/http_ca.crt",
#    ssl_assert_fingerprint = CERT_FINGERPRINT,
#    basic_auth = ("elastic", "EMJPQByQW0eXRiyPLXr+")
    api_key = api_key
)

mappings = {
    "properties": {
        "city": {"type": "text"},
        "country": {
            "type": "text",
            "fields": {
                "english": {
                    "type": "keyword",
                    "ignore_above": 256,
                }
            },
        },
    }
}
#client.get(index="my-index3", id="P9_smEo9R6GmTO94uRRMCQ")
#client.indices.create(index="my-index3", mappings=mappings)
#To start the script 1) . elastic_venv/bin/activate 2) py elastic.py
