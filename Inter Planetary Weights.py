#Inter Planetary Weights 

#Weight = Earth Weight x Surface Gravity Factor

Mercury = 0.38
Venus = 0.91
Moon = 0.165
Mars = 0.38
Jupiter = 2.34
Saturn = 0.93
Uranus = 0.92
Neptune = 1.12
Pluto = 0.066

sName =input('What is your name?')
sWeight =input('What is your Earth weight?')

print(f"{sName}'s Solar System's Weight Chart")

#Use to convert to decimals (float)
fEarthWeight = float(sWeight)

fMercuryWeight = fEarthWeight * Mercury
fVenusWeight = fEarthWeight * Venus
fMoonWeight = fEarthWeight * Moon
fMarsWeight = fEarthWeight * Mars
fJupiterWeight = fEarthWeight * Jupiter
fSaturnWeight = fEarthWeight * Saturn
fUranusWeight = fEarthWeight * Uranus
fNeptuneWeight = fEarthWeight * Neptune
fPlutoWeight = fEarthWeight * Pluto


#Results
print("Mercury  : " + str(fMercuryWeight) + " pounds")
print("Venus    : " + str(fVenusWeight) + " pounds")
print("Moon     : " + str(fMoonWeight) + " pounds")
print("Mars     : " + str(fMarsWeight) + " pounds")
print("Jupiter  : " + str(fJupiterWeight) + " pounds")
print("Saturn   : " + str(fSaturnWeight) + " pounds")
print("Uranus   : " + str(fUranusWeight) + " pounds")
print("Neptune  : " + str(fNeptuneWeight) + " pounds")
print("Pluto    : " + str(fPlutoWeight) + " pounds")




