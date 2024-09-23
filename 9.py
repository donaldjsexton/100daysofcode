print("🚨Generation Detector🚨")
print()
year = int(input("What year were you born? "))
if year >= 1883 and year <= 1900:
  print("You are part of the Lost Generation")
elif year >= 1901 and year <= 1927:
  print("You are part of the Greatest Generation")
elif year >= 1928 and year <= 1945:
  print("You are part of the Silent Generation")
elif year >= 1946 and year <= 1964:
  print("You are part of the Baby Boomers")
elif year >= 1965 and year <= 1980:
  print("You are part of Generation X")
elif year >= 1981 and year <= 1996:
  print("You are part of the Millennials")
elif year >= 1997 and year <= 2012:
  print("You are part of Generation Z")
elif year >= 2012 and year <= 2024:
  print("You are part of Generation Alpha")
else:
  print("You are either too old or too young to be alive")