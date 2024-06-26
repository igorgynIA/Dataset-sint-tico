! pip install faker

from faker import Faker
import pandas as pd
import random

fake = Faker("pt_BR")

nomes = []
pais = []
salario = []
cargo = []
idade = []

for i in range(100):
  fake_name = fake.name()
  nomes.append(fake_name)
  city = fake.country()
  pais.append(city)
  dimdim = random.randint(500,2000)
  salario.append(dimdim)
  job = fake.job()
  cargo.append(job)
  old = random.randint(18,80)
  idade.append(old)


data = {"Nome": nomes,
        "Idade": idade,
        "Origem": pais,
        "Cargo": cargo,
        "Salário($)": salario}

df = pd.DataFrame(data)
display(df)

df.to_excel("dataset_sintético.xlsx", index=False)
