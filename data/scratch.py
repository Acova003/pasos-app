data = [{"lon":-8.34949261508882,"lat":42.91471685282886,"ele":292},
{"lon":-8.349654721096158,"lat":42.914718613028526,"ele":289}]

print(list(map(lambda row: f'{row["lon"]}, {row["lat"]}', data)))

for row in data:
    print(row)
    print(f'{row["lat"]}, {row["lon"]}')
