from fastapi import FastAPI

app1 = FastAPI()


buyer_name = ""
buyers = []
products = [] 
purchased = []

@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing Here"}

@app1.post("/buyers")
async def addbuyer(name):
    if name in buyers:
        return {"result": "Duplicate entry"}
    else:
        buyers.append(name)
        purchased.append({})
        return {"result": "OK"}

@app1.post("/products")
async def addproduct(name):
    if name in products:
        return {"result": "Duplicate entry"}
    else:
        products.append(name)
        return {"result": "OK"}

@app1.get("/buyers")
async def listbuyers():
    return buyers


@app1.get("/products")
async def listproducts():
    return products

@app1.post("/buyers/{buyer_name}")
async def sellproduct(buyer_name, prod_name):
    if buyer_name in buyers:
        n = buyers.index(buyer_name)
        if prod_name in products:
            if prod_name in purchased[n]:
                c = purchased[n][prod_name]
                purchased[n][prod_name] = c+1;
                return {"result:": "OK"}
            else:
                purchased[n][prod_name] = 1;
                return {"result:": "OK"}
        else:
            msg = f"Error: no product {prod_name}"
            return {"result": msg}
    else:
        msg = f"Error: no buyer {buyer_name}"
        return {"result": msg}

@app1.get("/buyers/{buyer_name}/purchased")
async def purchasedItems(buyer_name):
    if buyer_name in buyers:
        n = buyers.index(buyer_name)
        return {f"{buyer_name}:": purchased[n]}
    else:
        msg = f"Error: no buyer {buyer_name}"
        return {"result": msg}


