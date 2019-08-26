def health_calculator(age,apple_ate,cigs_smoked):
    answer=(100-age)+(apple_ate*3.5)-(cigs_smoked*2)
    print("your health index is:",answer)

buckys_data=[27,20,0]
health_calculator(buckys_data[0],buckys_data[1],buckys_data[2])#this makes program bulky so we use following
health_calculator(*buckys_data)