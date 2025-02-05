from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Produkty</h1>
    <div class="product">
      <h2>Produkt 1</h2>
      <p>Cena: 100 PLN</p>
    </div>
    <div class="product">
      <h2>Produkt 2</h2>
      <p>Cena: 200 PLN</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("h2").text
    price = product.find("p").text
    print(f"{name} - {price}")

