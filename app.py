from flask import Flask, render_template, request, redirect
import db


app = Flask(__name__)

loggedIn = False
cartDict = {}
total = [0, 0]

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/owner', methods=['GET', 'POST'])
def owner():
    if not loggedIn:
        return render_template('login.html')
    return render_template('owner.html')

@app.route('/login', methods=['POST'])
def login():
    global loggedIn
    username = request.form['username']
    password = request.form['password']

    print(username, password)
    if db.login(username, password):
        loggedIn = True
        return redirect('/owner')

    return redirect('/')

@app.route('/vegetables', methods=['GET', 'POST'])
def vegetables():
    global cartDict, total
    cartDict = {}
    total = [0, 0]
    return render_template('vegetables.html')

@app.route('/vegetablesEdit', methods=['GET', 'POST'])
def vegetablesEdit():
    return render_template('vegetablesEdit.html', content=db.getVegetables())

@app.route('/clothing', methods=['GET', 'POST'])
def clothing():
    global cartDict, total
    cartDict = {}
    total = [0, 0]
    return render_template('clothing.html')

@app.route('/clothingEdit', methods=['GET', 'POST'])
def clothingEdit():
    return render_template('clothingEdit.html',content=db.getClothing())

@app.route('/electronics', methods=['GET', 'POST'])
def electronics():
    global cartDict, total
    cartDict = {}
    total = [0, 0]
    return render_template('electronics.html')

@app.route('/electronicsEdit', methods=['GET', 'POST'])
def electronicsEdit():
    return render_template('electronicsEdit.html', content=db.getElectronics())

@app.route('/cart/<store>/<items>/<quants>', methods=['GET', 'POST'])
def cart(store, items, quants):
    global cartDict, total
    items = items.split(',')
    quants = quants.split(',')

    print(db.getPrice(items[0]))
    for i in range(len(items)):
        total[0] += int(quants[i])
        total[1] += float(db.getPrice(items[i])) * int(quants[i])
        cartDict[items[i]] = [int(quants[i]), float(db.getPrice(items[i].replace(' ', '_')))]

    total[1] = f'{total[1]:.2f}'
    print(cartDict)
    return redirect(f'/invoice/{store}')

@app.route('/invoice/<store>', methods=['GET', 'POST'])
def invoice(store):
    return render_template('invoice.html', content=cartDict, total=total, store=store)

@app.route('/genInvoice/<store>/<name>/<mobile>/<q>/<d>/<total>')
def genInvoice(store, name, mobile, q, d, total):
    q = [x for x in q.split(',') if x]  # Ignore empty strings
    d = [x for x in d.split(',') if x]  # Ignore empty strings
    
    # total = 0
    # for i in range(len(d)):
    #     price = db.getPrice(d[i])
    #     if price is None:
    #         print(f"No price found for {d[i]}")
    #         continue
    #     total += float(price) * int(q[i])
    # total = f'{total:.2f}'

    d = str(d)[1:-1].replace('\'', '')
    q = str(q)[1:-1]
    print(d, q)

    # Store the invoice data in the database
    if store == 'v':
        db.addVegetables(name, mobile, q, d, total)
    elif store == 'c':
        db.addClothing(name, mobile, q, d, total)
    else:
        db.addElectronics(name, mobile, q, d, total)

    # Redirect to the current page or any other page
    return redirect('/')  # replace 'current_page' with the name of your current page


@app.route('/updateVegetables/<inp>/<val>', methods=['GET', 'POST'])
def updateVegetables(inp, val):
    print(inp, val)

    inp = inp.split(',')
    val = val.split(',')
    for i in range(len(inp)):
        db.updateVegetables(inp[i].split(' ')[1], inp[i].split(' ')[0], val[i])

    return redirect('/vegetablesEdit')


@app.route('/updateClothing/<inp>/<val>', methods=['GET', 'POST'])
def updateClothing(inp, val):
    inp = inp.split(',')
    val = val.split(',')
    for i in range(len(inp)):
        db.updateClothing(inp[i].split(' ')[1], inp[i].split(' ')[0], val[i])

    return redirect('/clothingEdit')

@app.route('/updateElectronics/<inp>/<val>', methods=['GET', 'POST'])
def updateElectronics(inp, val):
    inp = inp.split(',')
    val = val.split(',')
    for i in range(len(inp)):
        db.updateElectronics(inp[i].split(' ')[1], inp[i].split(' ')[0], val[i])
    return redirect('/electronicsEdit')

@app.route('/deleteVegetables/<name>', methods=['GET', 'POST'])
def deleteVegetables(name):
    db.deleteVegetables(name)
    return redirect('/vegetablesEdit')

@app.route('/deleteClothing/<name>', methods=['GET', 'POST'])
def deleteClothing(name):
    db.deleteClothing(name)
    return redirect('/clothingEdit')

@app.route('/deleteElectronics/<name>', methods=['GET', 'POST'])
def deleteElectronics(name):
    db.deleteElectronics(name)
    return redirect('/electronicsEdit')

@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    filename = db.pieChart()
    return render_template('graphs.html', filename=filename)

@app.route('/about_us', methods=['GET', 'POST'])
def aboutUs():
    return render_template('about_us.html')


if __name__ == '__main__':
    db.base()
    app.run(debug=True)

