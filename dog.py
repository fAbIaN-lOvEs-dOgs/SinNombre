import numpy as np # Math library
import pandas as pd # Data processing library
from googletrans import Translator # Language translation library
import asyncio # Asynchronous programming library

async def TranslateDataFrame(dataframe):
    translator = Translator() # Initialize the translator
    
    async def _TranslateCell(cell):
        if pd.isna(cell):
            return cell
        result = await translator.translate(str(cell), dest="es") # Translate the cell content to Spanish
        return result.text
    
    dataframe.columns = [await _TranslateCell(column) for column in dataframe.columns] # Translate column names

    tasks = []

    for column in dataframe.columns:
        for index in dataframe.index:
            tasks.append(_TranslateCell(dataframe.at[index, column])) # Create tasks for translating each cell

    translated = await asyncio.gather(*tasks) # Wait for all translation tasks to complete

    i = 0
    for column in dataframe.columns:
        for index in dataframe.index:
            dataframe.at[index, column] = translated[i] # Update the DataFrame with the translated values
            i += 1

    return dataframe # Return the translated DataFrame

async def translate():
    dataframe = pd.read_csv("dog_breeds.csv") # Load the original CSV file into a DataFrame
    translated = await TranslateDataFrame(dataframe) # Translate the DataFrame
    translated.to_csv("dog_breeds_es.csv", index=False) # Save the translated DataFrame to a new CSV file without the index

asyncio.run(translate()) # Run the asynchronous translation function

dogBreedDataFrame = pd.read_csv('dog_breeds_es.csv') # Load the CSV file into a DataFrame

print(dogBreedDataFrame.columns, "\n") # Print the column names to verify loading

def getDogBreedInfo(breedName):
    return dogBreedDataFrame[dogBreedDataFrame["Criar"] == breedName].to_dict(orient='records')[0]

def getDogBreedIndex(breedName):
    return dogBreedDataFrame[dogBreedDataFrame["Criar"] == breedName].index[0]

def getCountryOfOriginAtIndex(index):
    return dogBreedDataFrame.iloc[index]["País natal"]

def getFurColorAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Color de piel"]

def getHeightAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Altura (pulg.)"]

def getEyeColorAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Color de ojos"]

def getLifespanAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Longevidad (años)"]

def getTraitsAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Rasgos de carácter"]

def getCommonHealthProblemsAtIndex(index):
    return dogBreedDataFrame.iloc[index]["Problemas de salud comunes"]

def GetAllDogBreeds():
    return dogBreedDataFrame["Criar"].tolist()

def GetDogBreedCountryOfOrigin(breed):
    index = getDogBreedIndex(breed)
    return getCountryOfOriginAtIndex(index)

def GetDogBreedFurColor(breed):
    index = getDogBreedIndex(breed)
    return getFurColorAtIndex(index)

def GetDogBreedHeight(breed):
    index = getDogBreedIndex(breed)
    return getHeightAtIndex(index)

def GetDogBreedEyeColor(breed):
    index = getDogBreedIndex(breed)
    return getEyeColorAtIndex(index)

def GetDogBreedLifespan(breed):
    index = getDogBreedIndex(breed)
    return getLifespanAtIndex(index)

def GetDogBreedTraits(breed):
    index = getDogBreedIndex(breed)
    return getTraitsAtIndex(index)

def GetDogBreedCommonHealthProblems(breed):
    index = getDogBreedIndex(breed)
    return getCommonHealthProblemsAtIndex(index)