# Kenyah Collins
# 11/20/2022
# collins-HealthCalculator.py
# this program will calculate a persons body mass index and 
# calculate the users heart rate at different levels of intensity

print ('*' * 50)
print('\t\tHealth Calculator')
print ('*' * 50)
print('Enter in the following values for the user . . . ')

# bmi will be calculated with user inputs use function

def calc_bmi(weight_kgrams, height_msquared):

    # height = float(height)
    # weight = float(weight)

    height_msquared = (height * .0254) * (height * .0254)
    weight_kgrams = weight * .453592
    bmi = weight_kgrams / height_msquared

    return bmi

# heart rate at specific intensity will be calculated with karvonen formula
def calc_karv(age, rest_hr, intensity):
    karvonen = (((220 - age) - rest_hr) * intensity) + rest_hr

    return karvonen

# four user inputs of height(in) weight(lbs) age and resting HR
if __name__ == '__main__':

    height = float(input('Height in inches: '))
    weight = float(input('Weight in pounds: '))

    age = input('Current age: ')
    rest_hr = input('Resting heart rate: ')

    age = int(age)
    rest_hr = int(rest_hr)

    print('\nResults . . . \t\t')

# bmi categories
    bmi = calc_bmi(height, weight)

    if bmi < 18.5:
        bmi_types = 'underweight'
    elif bmi < 25:
        bmi_types = 'normal weight'
    elif bmi <30:
        bmi_types = 'overweight'
    else:
        bmi_types = 'obese'

    print('your BMI is: {} -- {}'.format(round(bmi, 2), bmi_types))
    print('\nExercise Instensity Heart Rates:')
    print('Intensity\tMax Heart Rate\n')

    # calc max HR with function
    intensity = .50

    for i in range(10):
        karvonen = calc_karv(age, rest_hr, intensity)
        print('{:.2f}\t\t{}'.format(intensity, int(karvonen)))
        intensity += .05
print()     
print ('*' * 50)
