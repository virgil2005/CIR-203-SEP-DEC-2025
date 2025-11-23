routes = ["Nairobi-Mombasa","Kisumu-Nakuru","Nairobi-Kisumu","Nakuru-Eldoret","Mombasa-Malindi","Nairobi-Thika","Garissa-Nairobi","Naanyuki-Meru","Kitale-Bungoma","Nairobi-Naivasha"]
print("Routes:", routes)
routes.append("Lamu-Mombasa")
routes.remove("Kitale-Bungoma")
print("Updated Routers:",routes)
routes.sort()
print("Sorted:",routes)
routes.reverse()
print("Reserved:",routes)
count_N =sum([1 for r in routes if r.startswith("N") ])
print("Routes starting with 'N':",count_N)
long_routes=[r for r in routes if len(r)>10]
print("Routes longer than 10 chars:",long_routes)