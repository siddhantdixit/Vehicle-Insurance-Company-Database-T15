import faker

fake = faker.Faker('en_IN')

for i in range(10):
    print(fake.name())