
# print(list(map(lambda row: f'#{row"lon"}, #{row"lat"}', data)))
for row in data:
    print(f'{row["lon"]}, {row["lat"]}')