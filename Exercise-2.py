products = [
    {"category": "cars", "brand": "Porsche", "model": "911 GT"},
    {"category": "phones", "brand": "Apple", "model": "iPhone 13"},
    {"category": "laptops", "brand": "Dell", "model": "XPS 13"},
    {"category": "watches", "brand": "Rolex", "model": "Submariner"},
]

s=[]

for item in products:
    s.append(item)
    
while s:
    print(s[-1])
    s.pop()