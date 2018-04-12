import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

camera_dataset = pd.read_csv(r"C:\Users\user\Python Programs\April12PythonTest\camera.csv")

camera_dataset = camera_dataset.drop(0)
camera_dataset = camera_dataset.dropna()
print("\nProperties of the dataset are as follows:-")
for i in camera_dataset.columns:
    print(i,end=", ")

print("\n\nData types of the properties are as follows:-")
print(camera_dataset.dtypes)

print("\n\nPrinting the details for first 25 entries")
sub_camera_dataset = camera_dataset.iloc[:25,:]
print(sub_camera_dataset[["Model","Release date","Price"]])

print("\n\nPrinting summary statistics for the dataset")
print(camera_dataset.describe())

print("\n\nPrinting summary statistics for price")
camera_dataset["Price"] = pd.to_numeric(camera_dataset["Price"],errors="coerce")
print(camera_dataset["Price"].describe())

camera_dataset_price_greater = camera_dataset.loc[camera_dataset["Price"] >1000]
plt.figure(figsize=(10,10))
plt.figure()
plt.plot(camera_dataset_price_greater["Release date"],camera_dataset_price_greater["Price"])
plt.savefig("time-series-graph")


cols = camera_dataset.columns.drop(['Model','Price'])
camera_dataset[cols] = camera_dataset[cols].apply(pd.to_numeric, errors='coerce')
print("\n\nCorrelation Matrix:-")
print(camera_dataset.corr())


plt.figure(1)
plt.scatter(camera_dataset["Release date"],camera_dataset["Max resolution"])
plt.title("Max Res vs Release Date")
plt.xlabel("Release Date")
plt.ylabel("Max Resolution")
plt.savefig("ReleaseDate-vs-MaxResolution")

plt.figure(2)
plt.scatter(camera_dataset["Release date"],camera_dataset["Low resolution"])
plt.title("Low Res vs Release Date")
plt.xlabel("Release Date")
plt.ylabel("Low Resolution")
plt.savefig("ReleaseDate-vs-LowResolution")


plt.figure(3)
plt.scatter(camera_dataset["Release date"],camera_dataset["Effective pixels"])
plt.title("Effective Pixels vs Release Date")
plt.xlabel("Release Date")
plt.ylabel("Effective pixels")
plt.savefig("ReleaseDate-vs-EffectivePixels")


plt.figure(5)
plt.scatter(camera_dataset["Max resolution"],camera_dataset["Effective pixels"])
plt.title("Max Res vs Effective Pixels")
plt.xlabel("Max Resolution")
plt.ylabel("Effective Pixels")
plt.savefig("MaxRes-vs-EffectivePixels")

plt.figure(6)
plt.scatter(camera_dataset["Low resolution"],camera_dataset["Effective pixels"])
plt.title("Low Res vs Effective Pixels")
plt.xlabel("Low Resolution")
plt.ylabel("Effective Pixels")
plt.savefig("LowRes-vs-EffectivePixels")

plt.figure(7)
plt.scatter(camera_dataset["Zoom wide (W)"],camera_dataset["Normal focus range"])
plt.title("Zoom wide vs Normal focus range")
plt.xlabel("Zoom wide")
plt.ylabel("Normal focus range")
plt.savefig("ZoomWide-vs-NormalFocusRange")

plt.figure(8)
plt.scatter(camera_dataset["Zoom wide (W)"],camera_dataset["Weight (inc. batteries)"])
plt.title("Zoom wide vs Weight (inc. batteries)")
plt.xlabel("Zoom wide")
plt.ylabel("Weight (inc. batteries)")
plt.savefig("ZoomWide-vs-Weight")

plt.figure(9)
plt.scatter(camera_dataset["Weight (inc. batteries)"],camera_dataset["Dimensions"])
plt.title("Weight (inc. batteries) vs Dimensions")
plt.xlabel("Weight (inc. batteries)")
plt.ylabel("Dimensions")
plt.savefig("Weight-vs-Dimensions")


plt.figure(10)
plt.scatter(camera_dataset["Model"],camera_dataset["Price"])
plt.title("Price vs Model")
plt.xlabel("Model")
plt.ylabel("Price")
plt.savefig("Model-vs-Price")

plt.figure(11)
plt.scatter(camera_dataset["Max resolution"],camera_dataset["Price"])
plt.title("Price vs Max resolution")
plt.xlabel("Max resolution")
plt.ylabel("Price")
plt.savefig("MaxRes-vs-Price")

plt.figure(12)
plt.scatter(camera_dataset["Low resolution"],camera_dataset["Price"])
plt.title("Price vs Low resolution")
plt.xlabel("Low resolution")
plt.ylabel("Price")
plt.savefig("LowRes-vs-Price")


plt.figure(13)
plt.scatter(camera_dataset["Effective pixels"],camera_dataset["Price"])
plt.title("Price vs Effective pixels")
plt.xlabel("Effective Pixels")
plt.ylabel("Price")
plt.savefig("EffectivePix-vs-Price")


plt.figure(14)
plt.scatter(camera_dataset["Zoom wide (W)"],camera_dataset["Price"])
plt.title("Price vs Zoom wide (W)")
plt.xlabel("Zoom wide (W)")
plt.ylabel("Price")
plt.savefig("ZoomW-vs-Price")

plt.figure(15)
plt.scatter(camera_dataset["Weight (inc. batteries)"],camera_dataset["Price"])
plt.title("Price vs Weight (inc. batteries)")
plt.xlabel("Weight (inc. batteries)")
plt.ylabel("Price")
plt.savefig("Weight-vs-Price")



