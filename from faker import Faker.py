from faker import Faker

fake = Faker()

# Generate and save dummy data to a text file
with open("dummy_data.txt", "w") as file:
    for _ in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()
        file.write(f"First Name: {first_name}, Last Name: {last_name}, Phone No: {phone_number}, Email Address: {email}\n")