import json

def load_categories():
    with open("data/category.json",encoding="utf-8") as f:
        cates = json.load(f)
        return cates

def load_products(q=None):
    with open("data/product.json",encoding="utf-8") as f:
        prods=json.load(f)

        if q:
            prods= [p for p in prods if p["name"].find(q)>=0]


        return prods

if __name__=="__main__":
    print(load_products())