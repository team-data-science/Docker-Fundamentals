import faker

Faker = faker.Factory().create
fake = Faker()

print(f"Hello {fake.name()} from {fake.state()}")
