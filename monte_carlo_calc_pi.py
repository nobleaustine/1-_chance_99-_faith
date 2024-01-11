# program to demonstrate Monte Carlo Stimulation to calcualte value of pi

# required libraries
# may need to install matplotlib as 'pip install matplotlib'
import random
import matplotlib.pyplot as plt

# generate random points and return them with points inside the circle and inside the inner box
def generate_samples(no_of_samples):
    # creating 2 list of random numbers within the range [-1,1]
    X =[random.uniform(-1,1) for _ in range(no_of_samples)] 
    Y =[random.uniform(-1,1) for _ in range(no_of_samples)] 
    
    # list of 1's for 1 if point lie in the circle with radius 1 and square with length 1
    samples_in_circle = [1 for i in range(no_of_samples) if X[i]**2 + Y[i]**2 <= 1 ]
    samples_in_square = [1 for j in range(no_of_samples) if abs(X[j])<=0.5 and abs(Y[j])<=0.5]

    return X,Y,samples_in_circle,samples_in_square

# main funcion to print N plots with different no of samples
def main(N):
    
    # creating N subplots
    num_plots = N
    fig, axes = plt.subplots(1, num_plots, figsize=(15, 5))

    # calculating plot and pi for N plots
    for i in range(num_plots):
        
        # total number of points
        no_samples = 10000*(10**i)
        
        # getting random points
        X,Y,samples_in_circle,samples_in_square= generate_samples(no_samples)
        # setting red for points in circle and blue for other points
        colors = ['red' if X[i]**2 + Y[i]**2 <= 1  else 'blue' for i in range(no_samples)]
        # setting green for points in inner circle
        final_colors = ["green" if colors[j] == 'red' and abs(X[j])<=0.5 and abs(Y[j])<=0.5 else colors[j] for j in range(no_samples) ]
        
        # calculating areas and value of pi
        area_circle = sum(samples_in_circle)
        area_square = sum(samples_in_square)

        pi1 = round(area_circle/area_square,3)
        pi2 = round(4*area_circle/no_samples,3)
    
        # Creating a scatter plot on the ith subplot
        axes[i].scatter(X, Y, color=final_colors, s=0.01)
        axes[i].set_title(f'Scatter Plot with {no_samples} samples')
        axes[i].text(-0.5, -1.5, f'method 1 pi value: {pi1} ',fontsize=12)
        axes[i].text(-0.5, -1.7, f'method 2 pi value: {pi2}',fontsize=12)

     
    # Adjust layout to prevent clipping of titles and adding texts   
    fig.suptitle('Mote Carlo stimulation to claculate the value of pi')
    fig.text(0.4, .045, f'Method 1 : area[circle](red)/area[inner square](green) pi*R²/R²', va='center', fontsize=8)
    fig.text(0.4, .015, f'Method 2 : 4*area[circle](red)/area[outer square](blue) 4pi*R²/(2*R)²', va='center', fontsize=8)
    plt.tight_layout()
    plt.show()

# calling the main function for 3 subplots 
main(3)