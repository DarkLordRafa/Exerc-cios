primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão da sua P.A.: '))
décimo_termo = primeiro_termo + (10 - 1) * razão
for p in range(primeiro_termo, décimo_termo + razão, razão):
	print(p)
