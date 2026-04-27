import pandas as pd

class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True
        print(f"{self.name} has been adopted!")

df_A = pd.read_csv("shelter_A.csv")
df_B = pd.read_csv("shelter_B.csv")

combined = pd.concat([df_A, df_B], ignore_index=True)

print("\nCombined Data:")
print(combined)

clean = combined.dropna(subset=["Pet_Name", "Animal_Type"])

print("\nClean Data:")
print(clean)

dogs = clean[clean["Animal_Type"] == "Dog"]

print("\nDogs Only:")
print(dogs)

if not dogs.empty:
    dog = dogs.iloc[0]   # now safe

    pet = RescuePet(
        dog["Pet_Name"],
        dog["Animal_Type"],
        dog["Age_Years"]
    )

    pet.process_adoption()

    adopted_df = pd.DataFrame([{
        "Pet_Name": pet.name,
        "Animal_Type": pet.species,
        "Age_Years": pet.age,
        "Adopted": pet.is_adopted
    }])

    adopted_df.to_csv(
        "successful_adoptions.csv",
        mode='a',
        header=False,
        index=False
    )

    print("\nSaved to successful_adoptions.csv")

else:
    print("\nNo valid dog found for adoption.")