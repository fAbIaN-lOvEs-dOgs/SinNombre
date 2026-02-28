from flask import Flask, render_template
import dog

website = Flask(__name__)

@website.route('/')
def start():
    return render_template('website.html')

@website.route('/dog/<breed>')
def doggo(breed):

    country = dog.GetDogBreedCountryOfOrigin(breed)
    fur = dog.GetDogBreedFurColor(breed)
    height = dog.GetDogBreedHeight(breed)
    eye = dog.GetDogBreedEyeColor(breed)
    lifespan = dog.GetDogBreedLifespan(breed)
    traits = dog.GetDogBreedTraits(breed)
    health = dog.GetDogBreedCommonHealthProblems(breed)

    return render_template("breed.html", breed=breed.title(), country=country, fur=fur, height=height, eye=eye, lifespan=lifespan, traits=traits, health=health)

@website.route('/dog/search')
def search():
    breeds = dog.GetAllDogBreeds()
    return render_template("search.html", breeds=breeds)

if __name__ == '__main__':
    website.run(debug=True)
